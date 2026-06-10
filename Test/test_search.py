import pytest
from Actions.SearchAction import SearchAction


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_valid_search(self):

        search = SearchAction(self.driver)

        search.searchProduct("computer")
        search.clickSearch()

        assert search.verifySearchRedirect()

    def test_invalid_search(self):

        search = SearchAction(self.driver)

        search.searchProduct("xyz123invalid")
        search.clickSearch()

        assert search.verify_no_product_message(),"No product message is not displayed"
    

    def test_search_without_keyword(self):

        search = SearchAction(self.driver)
        search.clickSearch()

        assert search.is_alert_present(),"Warning message is not displayed"

        search.accept_alert()