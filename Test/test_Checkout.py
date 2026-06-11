from selenium import webdriver
import time
from Actions.CheckoutAction import checkoutAction
import pytest
from Actions.LoginActions import LoginActions
from Utilities.excelReader import get_data
from Configuration.configReader import ReadConfig
from Actions.CartAction import CartAction

class TestCheckout:
    
    
    @pytest.mark.usefixtures("setup_and_teardown")
    def test_Checkout_RegisterUser(self):
        actions = LoginActions(self.driver)

        actions.click_login_link()
        actions.enter_email(ReadConfig.get_email())
        actions.enter_password(ReadConfig.get_password())
        actions.click_login_button()
        assert actions.get_user_account_name() is not None
       
        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        cart.open_shopping_cart()
        cart.Click_checkout()
      
        # Cart()

        checkout=checkoutAction(self.driver)
        checkout.form_fill()
        time.sleep(5)
        act = checkout.shippingText()
        exp="Select a shipping address from your address book or enter a new address."
        assert act==exp,"assert is get error"
        time.sleep(10)