from tabnanny import check

from selenium import webdriver
import time
from Actions.CheckoutAction import checkoutAction
import pytest
from Actions.LoginActions import LoginActions
from Utilities.excelReader import get_data
from Utilities.configReader import ReadConfig
from Actions.CartAction import CartAction
from Actions.RegisterAction import RegisterAction


@pytest.mark.usefixtures("setup_and_teardown")
class TestCheckout:

    #@pytest.mark.Jeeva
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
        register = RegisterAction(self.driver)
        data = get_data("TestData/TestData.xlsx","Register")

        row = data[0]

        register.click_register_link()

        register.enter_first_name(row[0])

        register.enter_last_name(row[1])

        register.enter_email(row[2])

        register.enter_password(str(row[3]))

        register.enter_confirm_password(str(row[4]))

        register.click_register_button()

        assert register.get_success_message() == "Your registration completed"

    #@pytest.mark.Jeeva
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

    #@pytest.mark.Jeeva
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
    @pytest.mark.parametrize("Firstname,Lastname\
            ,Email,Company,Country,City,Address1,Address2,\
            postalcode,Phonenumber,Faxnumber", get_data(r"D:\PYTHON_DEMOWEBSHOP\TestData\TestData.xlsx","billingForm"))
    def test_Checkout_fill_form(self,Firstname,Lastname,Email,Company,Country,City,Address1,Address2,\
                  postalcode,Phonenumber,Faxnumber):

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
        checkout.form_fill(Firstname,Lastname,Email,Company,\
                        Country,City,Address1,Address2,\
                  postalcode,Phonenumber,Faxnumber)

        time.sleep(5)

        act = checkout.shippingText()
        exp = "Select a shipping address from your address book or enter a new address."

        assert act == exp, "Shipping address text mismatch"

        time.sleep(10)