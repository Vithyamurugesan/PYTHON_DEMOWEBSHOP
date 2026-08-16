import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from Actions.RecentlyViewedProductsAction import RecentlyViewedProductsAction

RECENTLY_VIEWED_CSV = "TestData/RecentlyViewedProductsData.csv"

@pytest.mark.usefixtures("setup_and_teardown")
class TestRecentlyViewedProducts:
    driver: WebDriver

    def test_recently_viewed_products_page_opens(self):
        recently_viewed = RecentlyViewedProductsAction(self.driver)
        recently_viewed.open_recently_viewed_products_page()
        assert recently_viewed.is_recently_viewed_products_page_opened(), \
            "Recently Viewed Products page did not open"

    def test_viewed_product_is_displayed(self):
        recently_viewed = RecentlyViewedProductsAction(self.driver)
        recently_viewed.open_first_product_from_csv(RECENTLY_VIEWED_CSV)
        recently_viewed.open_recently_viewed_products_page()
        assert recently_viewed.is_first_visited_product_displayed(), \
            "Viewed product is not displayed in Recently Viewed Products"

    def test_multiple_viewed_products_are_displayed(self):
        recently_viewed = RecentlyViewedProductsAction(self.driver)
        recently_viewed.open_all_products_from_csv(RECENTLY_VIEWED_CSV)
        recently_viewed.open_recently_viewed_products_page()
        assert recently_viewed.are_all_visited_products_displayed(), \
            "All viewed products are not displayed in Recently Viewed Products"
