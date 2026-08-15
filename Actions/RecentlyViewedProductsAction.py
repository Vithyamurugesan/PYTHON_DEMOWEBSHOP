from Actions.BaseAction import BaseAction
from Pages.RecentlyViewedProductsPage import RecentlyViewedProductsPage
from Utilities.CsvReader import CsvReader
from Utilities.configReader import ReadConfig


class RecentlyViewedProductsAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.recently_viewed_page = RecentlyViewedProductsPage()
        self.visited_products = []

    def open_category(self, category):
        self.click(self.recently_viewed_page.get_category_link(category))

    def open_product(self, product):
        self.click(self.recently_viewed_page.get_product_link(product))

    def open_recently_viewed_products_page(self):
        self.click(self.recently_viewed_page.get_recently_viewed_products_link())

    def is_recently_viewed_products_page_opened(self):
        return self.wait_for_visible(self.recently_viewed_page.get_page_title()).is_displayed()

    def open_first_product_from_csv(self, file_path):
        data = CsvReader.get_recently_viewed_data(file_path)
        row = data[0]

        self.visited_products = []
        self.open_url(ReadConfig.get_base_url())
        self.open_category(row["category"])
        self.open_product(row["product"])
        self.visited_products.append(row["product"])

    def open_all_products_from_csv(self, file_path):
        data = CsvReader.get_recently_viewed_data(file_path)
        self.visited_products = []

        for row in data:
            self.open_url(ReadConfig.get_base_url())
            self.open_category(row["category"])
            self.open_product(row["product"])
            self.visited_products.append(row["product"])

    def get_displayed_product_titles(self):
        elements = self.find_all(self.recently_viewed_page.get_product_titles())
        return [element.text.strip() for element in elements]

    def is_product_displayed(self, product):
        return product in self.get_displayed_product_titles()

    def are_all_products_displayed(self, products):
        titles = self.get_displayed_product_titles()
        return all(product in titles for product in products)

    def is_first_visited_product_displayed(self):
        if not self.visited_products:
            return False
        return self.is_product_displayed(self.visited_products[0])

    def are_all_visited_products_displayed(self):
        return self.are_all_products_displayed(self.visited_products)
