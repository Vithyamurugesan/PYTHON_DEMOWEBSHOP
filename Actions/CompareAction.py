from Actions.BaseAction import BaseAction
from Pages.ComparePage import ComparePage
from Utilities.excelReader import get_data
from Utilities.configReader import ReadConfig


class CompareAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.compare_page = ComparePage()

    def open_jewelry_page(self):
        self.click(self.compare_page.get_jewelry_link())

    def open_product(self, product):
        self.click(self.compare_page.get_product_link(product))

    def click_add_to_compare(self):
        self.click(self.compare_page.get_add_to_compare_btn())

    def open_compare_products_page(self):
        self.open_url(ReadConfig.get_base_url() + "compareproducts")

    def verify_compare_page(self):
        return "compareproducts" in self.get_url()

    def verify_compared_products(self):
        products = self.find_all(self.compare_page.get_compare_products())
        return len(products) > 0

    def add_products_from_excel(self, file_path, sheet_name):
        rows = get_data(file_path, sheet_name)
        for row in rows:
            self.open_url(ReadConfig.get_base_url() + "jewelry")
            self.open_product(row[0])
            self.click_add_to_compare()
            self.driver.back()

    def add_single_product(self, product):
        self.open_product(product)
        self.click_add_to_compare()

    def remove_product_by_index(self, index):
        remove_buttons = self.find_all(self.compare_page.get_remove_buttons())
        remove_buttons[index].click()
        self.open_url(ReadConfig.get_base_url() + "compareproducts")

    def verify_product_removed(self):
        remove_buttons = self.find_all(self.compare_page.get_remove_buttons())
        return len(remove_buttons) == 1

    def verify_remaining_product(self):
        remove_buttons = self.find_all(self.compare_page.get_remove_buttons())
        return len(remove_buttons) >= 1

    def clear_compare_list(self):
        self.click(self.compare_page.get_clear_list_btn())

    def verify_empty_compare_list(self):
        return ReadConfig.get_empty_compare_msg().lower() in self.get_text(
            self.compare_page.get_empty_compare_msg()).lower()