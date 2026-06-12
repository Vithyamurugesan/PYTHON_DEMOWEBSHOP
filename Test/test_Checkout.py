from tabnanny import check

from selenium import webdriver
import time
from Actions.CheckoutAction import checkoutAction
import pytest
from Actions.LoginActions import LoginActions
from Utilities.excelReader import get_data
from Configuration.configReader import ReadConfig
from Actions.CartAction import CartAction
from Actions.RegisterAction import RegisterAction


@pytest.mark.usefixtures("setup_and_teardown")
class TestCheckout:

    @pytest.mark.Jeeva
    @pytest.mark.order(1)
    def test_checkout_withRegestion(self):

        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        cart.open_shopping_cart()
        cart.click_checkout()

        checkout = checkoutAction(self.driver)
        checkout.registrion_click()

    @pytest.mark.Jeeva
    @pytest.mark.order(2)
    def test_checkout_withlogin(self):

        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        cart.open_shopping_cart()
        cart.click_checkout()

        actions = LoginActions(self.driver)
        actions.enter_email(ReadConfig.get_email())
        actions.enter_password(ReadConfig.get_password())
        actions.click_login_button()

        assert actions.get_user_account_name() is not None

        checkout = checkoutAction(self.driver)
        act = checkout.checkout_Text()
        print(act)

    @pytest.mark.Jeeva
    @pytest.mark.order(3)
    def test_checkout_withGuest(self):

        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        cart.open_shopping_cart()
        cart.click_checkout()

        checkout = checkoutAction(self.driver)
        checkout.guest_checkout()

        act = checkout.checkout_Text()
        exp = "Checkout"

        print(act)
        assert act == exp

    @pytest.mark.Jeeva
    @pytest.mark.order(4)
    def test_Checkout_fill_form(self):

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
        cart.click_checkout()

        checkout = checkoutAction(self.driver)
        checkout.form_fill()

        time.sleep(5)

        act = checkout.shippingText()
        exp = "Select a shipping address from your address book or enter a new address."

        assert act == exp, "Shipping address text mismatch"

        time.sleep(10)