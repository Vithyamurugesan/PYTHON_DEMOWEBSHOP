from selenium.webdriver.common.by import By
class RecentlyViewedProductsPage:

    def __init__(self):
        self.__category_link = lambda cat: (By.LINK_TEXT, cat)
        self.__product_link = lambda name: (By.LINK_TEXT, name)
        self.__recently_viewed_products_link = (By.LINK_TEXT, "Recently viewed products")
        self.__page_title = (By.XPATH, "//div[@class='page-title']/h1")
        self.__product_items = (By.XPATH, "//div[contains(@class,'product-item')]")
        self.__product_titles = (By.XPATH, "//div[contains(@class,'product-item')]//h2[@class='product-title']/a")

    def get_category_link(self, category):
        return self.__category_link(category)

    def get_product_link(self, name):
        return self.__product_link(name)

    def get_recently_viewed_products_link(self):
        return self.__recently_viewed_products_link

    def get_page_title(self):
        return self.__page_title

    def get_product_items(self):
        return self.__product_items

    def get_product_titles(self):
        return self.__product_titles
