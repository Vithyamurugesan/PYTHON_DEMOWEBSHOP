import pytest
from Actions.ProductDetailAction import ProductDetailAction
from Utilities.CsvReader import CsvReader
from Configuration.configReader import ReadConfig

PRODUCT_CSV = "TestData/productDetailData.csv"


@pytest.mark.usefixtures("setup_and_teardown")
class TestProductDetail:

    @pytest.mark.parametrize("row", CsvReader.get_data(PRODUCT_CSV))
    def test_product_details_page(self, row):
        product_detail = ProductDetailAction(self.driver)
        product_detail.open_category(row["category"])
        product_detail.select_product(row["product"])
        assert product_detail.is_product_page_opened(),"Product details page did not open"
        assert product_detail.is_product_name_displayed(),"Product name is not displayed"
        assert product_detail.is_product_price_displayed(),"Product price is not displayed"
        assert product_detail.is_product_description_displayed(),"Product description is not displayed"
        assert product_detail.is_product_image_displayed(),"Product image is not displayed"

    @pytest.mark.parametrize("row", CsvReader.get_data(PRODUCT_CSV))
    def test_product_availability(self, row):
        product_detail = ProductDetailAction(self.driver)
        product_detail.open_category(row["category"])
        product_detail.select_product(row["product"])
        assert product_detail.get_availability_label() == ReadConfig.get_availability_label(), \
            "Availability label mismatch"
        assert product_detail.get_availability_value() == row["availability"], \
            f"Expected '{row['availability']}' but got '{product_detail.get_availability_value()}'"


    @pytest.mark.parametrize("row", CsvReader.get_data(PRODUCT_CSV))
    def test_invalid_quantity_validation(self, row):
        if not row["qty"]:
            pytest.skip("No quantity data for this row")
        product_detail = ProductDetailAction(self.driver)
        product_detail.open_category(row["category"])
        product_detail.select_product(row["product"])
        product_detail.enter_quantity(row["qty"])
        product_detail.click_add_to_cart()
        assert ReadConfig.get_invalid_qty_msg() in product_detail.get_notification_message(), \
            "Quantity validation message is not displayed"