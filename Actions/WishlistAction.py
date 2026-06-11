from selenium.webdriver.common.by import By
from Actions.BaseAction import BaseAction
from Pages.WishlistPage import WishlistPage
from Actions.SearchAction import SearchAction


class WishlistAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.wishlist_page = WishlistPage()
        self.search_action = SearchAction(driver)

    def addProductToWishlist(self, product):

        self.search_action.searchProduct(product)
        self.search_action.clickSearch()

        self.driver.find_element(By.XPATH,f"//a[contains(text(),'{product}')]").click()

        self.click(self.wishlist_page.get_addToWishlistButton())

    def verifySuccessMessage(self, expected_message):
        actual_message=self.get_text(self.wishlist_page.get_successMessage())
        return expected_message.lower() in actual_message.lower()

    def navigateToWishlist(self):
        self.click(self.wishlist_page.get_wishlistLink())

    def verifyProductInWishlist(self, product):

        self.navigateToWishlist()

        products=self.driver.find_elements(*self.wishlist_page.get_wishlistProducts())

        for item in products:
            if product.lower() in item.text.lower():
                return True

        return False

    def removeProductFromWishlist(self):

        self.navigateToWishlist()
        self.driver.find_element(By.NAME,"removefromcart").click()
        self.click(self.wishlist_page.get_updateWishlistButton())

    def verifyEmptyWishlistMessage(self):
        return "wishlist is empty" in self.get_text(self.wishlist_page.get_emptyWishlistMessage()).lower()

    def moveWishlistProductToCart(self):

        self.navigateToWishlist()
        self.driver.find_element(By.NAME,"addtocart").click()
        self.click(self.wishlist_page.get_addToCartButton())

    def verifyProductInCart(self, product):

        self.click(self.wishlist_page.get_shoppingCartLink())

        products=self.driver.find_elements(*self.wishlist_page.get_cartProduct())

        for item in products:
            if product.lower() in item.text.lower():
                return True

        return False