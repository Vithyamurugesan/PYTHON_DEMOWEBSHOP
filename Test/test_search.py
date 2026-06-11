import pytest
from Actions.SearchAction import SearchAction
from Utilities import excelReader

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    @pytest.mark.parametrize("product", excelReader.get_data("TestData/TestData.xlsx","ValidSearchProducts"))
    def test_valid_search(self, product):

        search = SearchAction(self.driver)

        search.searchProduct(product)
        search.clickSearch()

        assert search.verifySearchRedirect()


    @pytest.mark.parametrize("product", excelReader.get_data("TestData/TestData.xlsx","InvalidSearchProducts"))
    def test_invalid_search(self, product):

        search = SearchAction(self.driver)

        search.searchProduct(product)
        search.clickSearch()

        assert search.verify_no_product_message(),"No product message is not displayed"
    

    def test_search_without_keyword(self):

        search = SearchAction(self.driver)
        search.clickSearch()

        assert search.is_alert_present(),"Warning message is not displayed"

        search.accept_alert()