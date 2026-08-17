import pytest

from Actions.SearchAction import SearchAction
from Utilities import excelReader
from Utilities.logCreator import get_logger


logger = get_logger()


@pytest.mark.Vetri
@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:


    @pytest.mark.parametrize("product", excelReader.get_data("TestData/TestData.xlsx","ValidSearchProducts"))
    def test_valid_search(self, product):

        logger.info(f"Starting valid search test for product: {product}")

        search = SearchAction(self.driver)

        search.searchProduct(product)
        logger.info(f"Entered search product: {product}")

        search.clickSearch()
        logger.info("Clicked search button")

        assert search.verifySearchRedirect()
        logger.info("Search redirect verified successfully")



    @pytest.mark.parametrize("product", excelReader.get_data("TestData/TestData.xlsx","InvalidSearchProducts"))
    def test_invalid_search(self, product):

        logger.info(f"Starting invalid search test for product: {product}")

        search = SearchAction(self.driver)

        search.searchProduct(product)
        logger.info(f"Entered invalid search product: {product}")

        search.clickSearch()
        logger.info("Clicked search button")

        assert search.verify_no_product_message(),"No product message is not displayed"
        logger.info("No product message verified successfully")



    def test_search_without_keyword(self):

        logger.info("Starting search without keyword test")

        search = SearchAction(self.driver)

        search.clickSearch()
        logger.info("Clicked search button without entering keyword")

        assert search.is_alert_present(),"Warning message is not displayed"
        logger.info("Warning alert message verified")

        search.accept_alert()
        logger.info("Alert accepted successfully")