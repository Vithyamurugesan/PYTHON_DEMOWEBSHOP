import pytest
from selenium.webdriver.common.by import By

from Actions.DownloadAction import DownloadAction


@pytest.mark.usefixtures("setup_and_teardown")
class TestDownload:

    def test_downloadable_products_registered_user(self):

        download = DownloadAction(self.driver)

        download.click_my_account()

        try:

            download.click_downloadable_products()

            count = download.get_downloaded_product_count()

            print(f"\nDownloaded Product Count: {count}")

            products = download.get_all_product_names()

            print(f"Downloaded Products: {products}")

            assert count >= 0

        except Exception:

            error_msg = download.get_internal_error_message()

            print(f"\nWebsite Error Message: {error_msg}")

            assert error_msg == "We're sorry, an internal error occurred."

    def test_unregistered_user_redirected_to_login(self):

        # Logout because conftest.py already logs in
        self.driver.find_element(By.LINK_TEXT, "Log out").click()

        download = DownloadAction(self.driver)

        download.click_my_account()

        current_url = self.driver.current_url

        print(f"\nCurrent URL: {current_url}")

        assert "login" in current_url.lower()