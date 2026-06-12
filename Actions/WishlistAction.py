from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

        product_locator=(By.XPATH,f"//h2[@class='product-title']/a[contains(text(),'{product}')]")

        self.click(product_locator)
        self.click(self.wishlist_page.get_addToWishlistButton())

    def verifySuccessMessage(self, expected_message):
        actual_message = self.get_text(self.wishlist_page.get_successMessage())
        return expected_message.lower() in actual_message.lower()

    def navigateToWishlist(self):
        self.click(self.wishlist_page.get_wishlistLink())

    def verifyProductInWishlist(self, product):
        products=self.driver.find_elements(*self.wishlist_page.get_wishlistProducts())

        for item in products:
            if product.lower() in item.text.lower():
                return True

        return False

    def removeProductFromWishlist(self):

        self.navigateToWishlist()

        checkboxes=self.driver.find_elements(By.NAME,"removefromcart")

        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()

        self.click(self.wishlist_page.get_updateWishlistButton())

    def verifyEmptyWishlistMessage(self):

        return "wishlist is empty" in self.get_text(self.wishlist_page.get_emptyWishlistMessage()).lower()

    def moveWishlistProductToCart(self):

        self.navigateToWishlist()

        add_to_cart_checkboxes = self.driver.find_elements(By.NAME,"addtocart")

        if add_to_cart_checkboxes:
            checkbox = add_to_cart_checkboxes[0]
            if not checkbox.is_selected():
                checkbox.click()

        self.click(self.wishlist_page.get_addToCartButton())

    def verifyProductInCart(self, product):

        self.click(self.wishlist_page.get_shoppingCartLink())

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.wishlist_page.get_cartProduct()))
        except Exception:
            return False

        products = self.driver.find_elements(*self.wishlist_page.get_cartProduct())

        for item in products:
            if product.lower() in item.text.lower():
                return True

        return False

    def clearWishlist(self):

        self.navigateToWishlist()

        checkboxes = self.driver.find_elements(By.NAME,"removefromcart")

        if len(checkboxes) > 0:

            for checkbox in checkboxes:
                if not checkbox.is_selected():
                    checkbox.click()

            self.click(self.wishlist_page.get_updateWishlistButton())