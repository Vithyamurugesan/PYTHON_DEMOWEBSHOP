from selenium.webdriver.common.by import By


class ProductDetailPage:

    def __init__(self):
        self.__category_link        = lambda cat: (By.LINK_TEXT, cat)
        self.__product_link         = lambda name: (By.LINK_TEXT, name)
        self.__product_name         = (By.XPATH, "//div[@class='product-name']/h1")
        self.__product_price        = (By.XPATH, "//div[@class='product-price']//span")
        self.__product_description  = (By.XPATH, "//div[@class='full-description']")
        self.__product_image        = (By.XPATH, "//div[@class='picture']//img")
        self.__availability_label   = (By.XPATH, "//span[@class='label']")
        self.__availability_value   = (By.XPATH, "//span[@class='value']")
        self.__quantity_box         = (By.CSS_SELECTOR, "input.qty-input")
        self.__add_to_cart_button   = (By.XPATH, "//input[@value='Add to cart']")
        self.__notification_message = (By.CSS_SELECTOR, ".bar-notification")

    def get_category_link(self, category):
        return self.__category_link(category)

    def get_product_link(self, name):
        return self.__product_link(name)

    def get_product_name(self):
        return self.__product_name

    def get_product_price(self):
        return self.__product_price

    def get_product_description(self):
        return self.__product_description

    def get_product_image(self):
        return self.__product_image

    def get_availability_label(self):
        return self.__availability_label

    def get_availability_value(self):
        return self.__availability_value

    def get_quantity_box(self):
        return self.__quantity_box

    def get_add_to_cart_button(self):
        return self.__add_to_cart_button

    def get_notification_message(self):
        return self.__notification_message