import pytest
from Actions.CompareAction import CompareAction
from Utilities.excelReader import get_data
from Utilities.configReader import ReadConfig

COMPARE_EXCEL = "TestData/compareProductsData.xlsx"
COMPARE_SHEET = "CompareProducts"


@pytest.mark.usefixtures("setup_and_teardown")
class TestCompare:

    # @AddSingleCompareProduct
    def test_add_single_product_to_compare(self):
        compare = CompareAction(self.driver)
        compare.open_jewelry_page()
        compare.open_product(ReadConfig.get_compare_product())
        compare.click_add_to_compare()
        compare.open_compare_products_page()
        assert compare.verify_compare_page(),      "User did not navigate to compare products page"
        assert compare.verify_compared_products(), "Product is not displayed in compare products page"

    # @AddMultipleCompareProducts
    def test_add_multiple_products_to_compare(self):
        compare = CompareAction(self.driver)
        compare.add_products_from_excel(COMPARE_EXCEL, COMPARE_SHEET)
        compare.open_compare_products_page()
        assert compare.verify_compare_page(),      "User did not navigate to compare products page"
        assert compare.verify_compared_products(), "Products are not displayed in compare products page"

    # @RemoveCompareProduct
    def test_remove_compare_product(self):
        compare = CompareAction(self.driver)
        compare.open_jewelry_page()
        compare.open_product(ReadConfig.get_compare_product())
        compare.click_add_to_compare()
        compare.open_url(ReadConfig.get_base_url() + "jewelry")
        compare.open_product(ReadConfig.get_compare_product_two())
        compare.click_add_to_compare()
        compare.open_compare_products_page()
        compare.remove_product_by_index(1)
        assert compare.verify_product_removed(),   "Product was not removed from compare list"
        assert compare.verify_remaining_product(), "Remaining product is not displayed"

    # @ClearCompareList
    @pytest.mark.parametrize("row", get_data("TestData/compareProductsData.xlsx", "CompareProducts"))
    def test_clear_compare_list(self, row):
        compare = CompareAction(self.driver)
        compare.open_jewelry_page()
        compare.open_product(row[0])
        compare.click_add_to_compare()
        compare.open_compare_products_page()
        compare.clear_compare_list()
        assert compare.verify_empty_compare_list(), "Compare list is not empty after clearing"