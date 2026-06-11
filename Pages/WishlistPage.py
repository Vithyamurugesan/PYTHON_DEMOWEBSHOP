from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class WishlistPage:

    def __init__(self):
        
        self.__addToWishlistButton=(By.XPATH,"//input[@value='Add to wishlist']")
        self.__successMessage=(By.XPATH,"//p[@class='content']")
        self.__wishlistLink=(By.LINK_TEXT,"Wishlist")
        self.__wishlistProducts=(By.XPATH,"//table[@class='cart']//td[@class='product']/a")
        self.__updateWishlistButton=(By.NAME,"updatecart")
        self.__emptyWishlistMessage=(By.XPATH,"//div[@class='wishlist-content']")
        self.__addToCartButton=(By.NAME,"addtocartbutton")
        self.__shoppingCartLink=(By.LINK_TEXT,"Shopping cart")
        self.__cartProduct=(By.XPATH,"//td[@class='product']/a")

    
    def get_addToWishlistButton(self):
        return self.__addToWishlistButton
    
    def get_successMessage(self):
        return self.__successMessage
    
    def get_wishlistLink(self):
        return self.__wishlistLink
    
    def get_wishlistProducts(self):
        return self.__wishlistProducts
    
    def get_updateWishlistButton(self):
        return self.__updateWishlistButton
    
    def get_emptyWishlistMessage(self):
        return self.__emptyWishlistMessage
    
    def get_addToCartButton(self):
        return self.__addToCartButton
    
    def get_shoppingCartLink(self):
        return self.__shoppingCartLink
    
    def get_cartProduct(self):
        return self.__cartProduct
    





