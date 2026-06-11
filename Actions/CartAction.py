import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Actions.BaseAction import BaseAction
from Pages.CartPage import CartPage
from Utilities.excelReader import get_data
from Configuration.configReader import ReadConfig


class CartAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.cart_page = CartPage()

    def open_books_page(self):
        self.click(self.cart_page.get_books())

    def open_computing_book_page(self):
        self.click(self.cart_page.get_computing_book())

    def add_to_cart(self):
        self.wait_for_clickable(self.cart_page.get_add_to_cart_button())
        self.click(self.cart_page.get_add_to_cart_button())
        time.sleep(2)

    def check_cart(self):
        try:
            cart_link = self.wait_for_clickable(self.cart_page.get_shopping_cart())
            cart_link.click()
            return self.wait_for_visible(self.cart_page.get_cart_table()).is_displayed()
        except Exception as e:
            print(f"Cart verification failed: {e}")
            return False

    def add_products_from_excel(self, file_path, sheet_name):
        products = get_data(file_path, sheet_name)
        base_url = ReadConfig.get_base_url()

        search_box = (By.ID, "small-searchterms")
        search_btn = (By.XPATH, "//input[@value='Search']")

        for row in products:
            product_name = row[0]
            self.open_url(base_url)

            self.send_keys(search_box, product_name)
            self.click(search_btn)

            product_link = (By.PARTIAL_LINK_TEXT, product_name)
            self.click(product_link)

            self.wait_for_clickable(self.cart_page.get_add_to_cart_button())
            self.click(self.cart_page.get_add_to_cart_button())
            time.sleep(1)

    def open_shopping_cart(self):
        self.click(self.cart_page.get_shopping_cart())

    def verify_products_displayed(self):
        products = self.find_all(self.cart_page.get_product_list())
        return len(products) > 0

    def click_checkout(self):
        self.click(self.cart_page.get_checkbox())
        self.click(self.cart_page.get_click_checkout())

    def verify_subtotal_displayed(self):
        return self.wait_for_visible(self.cart_page.get_subtotal()).is_displayed()

    def open_empty_cart(self):
        self.open_url(ReadConfig.get_base_url() + "cart")

    def get_empty_cart_message(self):
        try:
            return self.get_text(self.cart_page.get_empty_cart_msg()).strip()
        except Exception as e:
            print(f"Empty cart message not found: {e}")
            return ""

    def enter_coupon_code(self, code):
        self.send_keys(self.cart_page.get_coupon_box(), code)

    def click_apply_coupon(self):
        self.click(self.cart_page.get_coupon_button())

    def enter_gift_card_code(self, code):
        self.wait_for_visible(self.cart_page.get_gift_card_box())
        self.send_keys(self.cart_page.get_gift_card_box(), code)

    def click_apply_gift_card(self):
        self.wait_for_clickable(self.cart_page.get_gift_card_button())
        self.click(self.cart_page.get_gift_card_button())

    def get_validation_message(self):
        return self.get_text(self.cart_page.get_message())

    def update_quantity(self, quantity):
        self.find(self.cart_page.get_quantity_box()).clear()
        self.send_keys(self.cart_page.get_quantity_box(), quantity)

    def click_update_shopping_cart(self):
        self.click(self.cart_page.get_update_cart_button())

    def verify_updated_quantity(self, expected_qty):
        actual_qty = self.find(self.cart_page.get_quantity_box()).get_attribute("value")
        return actual_qty == expected_qty

    def remove_product(self):
        self.click(self.cart_page.get_remove_check_box())

    def verify_removed_product(self):
        try:
            return ReadConfig.get_empty_cart_msg() in self.get_text(self.cart_page.get_empty_cart_msg())
        except Exception as e:
            print(f"Removed product validation failed: {e}")
            return False