import pytest
from Actions.SearchAction import SearchAction


@pytest.mark.usefixtures("driver")
class TestSearch:

    def test_valid_search(self):

        search = SearchAction(self.driver)

        search.search_product("computer")
        search.click_search()

        assert search.verify_search_redirect(), "User is not redirected to search results page"

    def test_invalid_search(self):

        search = SearchAction(self.driver)

        search.search_product("xyz123invalid")
        search.click_search()

        assert search.verify_no_product_message(), "No product message is not displayed"