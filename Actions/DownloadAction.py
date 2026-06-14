from Actions.BaseAction import BaseAction
from Pages.DownloadPage import DownloadPage

class DownloadAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.page = DownloadPage()

    def click_my_account(self):
        self.click(self.page.get_my_account_link())

    def click_downloadable_products(self):
        self.click(self.page.get_download_product_link())

    def get_downloaded_product_count(self):
        products = self.find_all(
            self.page.get_product_count()
        )
        return len(products)

    def get_all_product_names(self):

        products = self.find_all(
            self.page.get_product_name()
        )

        product_list = []

        for product in products:
            product_list.append(product.text)

        return product_list
    def get_internal_error_message(self):
        return self.get_text(
        self.page.get_internal_error_message()
    )