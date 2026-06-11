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
        # Wait for Add to Cart button, click it, then wait for page to settle
        self.wait_for_clickable(self.cart_page.get_add_to_cart_button())
        self.click(self.cart_page.get_add_to_cart_button())
        time.sleep(2)  # wait for cart count to update in header

    def check_cart(self):
        try:
            # Re-locate the shopping cart link fresh after add-to-cart page update
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

            # Go back to home page for each product
            self.driver.get(base_url)

            self.send_keys(search_box, product_name)
            self.click(search_btn)

            # Wait for search results to fully load before clicking product
            wait = WebDriverWait(self.driver, 10)
            product_link = (By.PARTIAL_LINK_TEXT, product_name)
            wait.until(EC.presence_of_element_located(product_link))

            # Re-find element right before clicking to avoid stale reference
            self.driver.find_element(*product_link).click()

            # Wait for product page to load, then click Add to Cart
            self.wait_for_clickable(self.cart_page.get_add_to_cart_button())
            self.click(self.cart_page.get_add_to_cart_button())
            time.sleep(1)  # brief pause after each add

    def open_shopping_cart(self):
        self.click(self.cart_page.get_shopping_cart())

    def verify_products_displayed(self):
        products = self.driver.find_elements(*self.cart_page.get_product_list())
        return len(products) > 0
    
    def Click_checkout(self):
        self.click(self.cart_page.get_checkbox())
        self.click(self.cart_page.get_click_checkout())
