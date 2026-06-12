import pytest
from Actions.LoginActions import LoginActions
from Actions.DownloadAction import DownloadAction
from Utilities.configReader import ReadConfig


@pytest.mark.usefixtures("setup_and_teardown")
class TestDownload:

    def test_downloadable_products_registered_user(self):

        login = LoginActions(self.driver)
        download = DownloadAction(self.driver)
        login.click_login_link()
        login.enter_email(ReadConfig.get_email())
        login.enter_password(ReadConfig.get_password())
        login.click_login_button()
        download.click_my_account()
        download.click_downloadable_products()
        count = download.get_downloaded_product_count()
        print(f"\nDownloaded Product Count: {count}")

        products = download.get_all_product_names()
        print(f"Downloaded Products: {products}")

        assert count >= 0

    def test_unregistered_user_redirected_to_login(self):

        download = DownloadAction(self.driver)
        download.click_my_account()
        current_url = self.driver.current_url
        print(f"\nCurrent URL: {current_url}")
        assert "login" in current_url.lower()