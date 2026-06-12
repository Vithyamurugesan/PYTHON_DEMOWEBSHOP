from Actions.BaseAction import BaseAction
from Pages.ProductDetailPage import ProductDetailPage


class ProductDetailAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.product_page = ProductDetailPage()

    def open_category(self, category):
        self.click(self.product_page.get_category_link(category))

    def select_product(self, product_name):
        self.click(self.product_page.get_product_link(product_name))

    def is_product_page_opened(self):
        return self.wait_for_visible(self.product_page.get_product_name()).is_displayed()

    def is_product_name_displayed(self):
        return self.wait_for_visible(self.product_page.get_product_name()).is_displayed()

    def is_product_price_displayed(self):
        return self.wait_for_visible(self.product_page.get_product_price()).is_displayed()

    def is_product_description_displayed(self):
        return self.wait_for_visible(self.product_page.get_product_description()).is_displayed()

    def is_product_image_displayed(self):
        return self.wait_for_visible(self.product_page.get_product_image()).is_displayed()

    def get_availability_label(self):
        return self.get_text(self.product_page.get_availability_label())

    def get_availability_value(self):
        return self.get_text(self.product_page.get_availability_value())

    def enter_quantity(self, qty):
        self.find(self.product_page.get_quantity_box()).clear()
        self.send_keys(self.product_page.get_quantity_box(), qty)

    def click_add_to_cart(self):
        self.click(self.product_page.get_add_to_cart_button())

    def get_notification_message(self):
        return self.get_text(self.product_page.get_notification_message())