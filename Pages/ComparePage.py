from selenium.webdriver.common.by import By


class ComparePage:

    def __init__(self):
        self.__jewelry_link         = (By.LINK_TEXT, "Jewelry")
        self.__add_to_compare_btn   = (By.XPATH, "//input[contains(@value,'Add to compare list')]")
        self.__clear_list_btn       = (By.LINK_TEXT, "Clear list")
        self.__compare_products     = (By.XPATH, "//table[contains(@class,'compare-products')]//a")
        self.__empty_compare_msg    = (By.CSS_SELECTOR, ".page-body")
        self.__remove_buttons       = (By.XPATH, "//tr[@class='overview']//input[@value='Remove']")

    def get_jewelry_link(self):
        return self.__jewelry_link

    def get_add_to_compare_btn(self):
        return self.__add_to_compare_btn

    def get_clear_list_btn(self):
        return self.__clear_list_btn

    def get_compare_products(self):
        return self.__compare_products

    def get_empty_compare_msg(self):
        return self.__empty_compare_msg

    def get_remove_buttons(self):
        return self.__remove_buttons

    def get_product_link(self, product):
        return (By.LINK_TEXT, product)