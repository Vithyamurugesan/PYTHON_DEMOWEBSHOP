from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self):
        self.__books = (By.LINK_TEXT, "Books")
        self.__computingAndInternetBook = (By.XPATH, "//h2[@class='product-title']/child::a[normalize-space()='Computing and Internet']")
        self.__shoppingCart = (By.XPATH, "//span[text()='Shopping cart']/ancestor::a")
        self.__addToCartButton = (By.XPATH, "//input[contains(@value,'Add to cart')]")
        self.__cartTable = (By.XPATH, "//form[@action='/cart']/descendant::table")
        self.__productList = (By.XPATH, "//table/descendant::tbody/child::tr/child::td[@class='product']")
        self.__subtotal = (By.XPATH, "//span[contains(@class,'product-price')]")
        self.__emptyCartMsg = (By.CSS_SELECTOR, ".order-summary-content")

    def get_books(self):
        return self.__books

    def get_computing_book(self):
        return self.__computingAndInternetBook

    def get_shopping_cart(self):
        return self.__shoppingCart

    def get_add_to_cart_button(self):
        return self.__addToCartButton

    def get_cart_table(self):
        return self.__cartTable

    def get_product_list(self):
        return self.__productList

    def get_subtotal(self):
        return self.__subtotal

    def get_empty_cart_msg(self):
        return self.__emptyCartMsg