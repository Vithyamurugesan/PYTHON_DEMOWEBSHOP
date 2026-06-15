from tabnanny import check
from selenium import webdriver
import time
import pytest

from Actions.CheckoutAction import checkoutAction
from Actions.LoginActions import LoginActions
from Actions.CartAction import CartAction
from Actions.RegisterAction import RegisterAction

from Utilities.excelReader import get_data
from Utilities.CsvReader import CsvReader
from Utilities.configReader import ReadConfig
from Utilities.logCreator import get_logger


@pytest.mark.usefixtures("setup_and_teardown")
class TestCheckout:

    log = get_logger()

    @pytest.mark.Jeeva
    @pytest.mark.order(1)
    def test_checkout_withRegestion(self):

        self.log.info("Checkout Registration Test Started")

        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        cart.open_shopping_cart()
        cart.click_checkout()

        checkout = checkoutAction(self.driver)
        checkout.registrion_click()

        register = RegisterAction(self.driver)
        data = get_data("TestData/TestData.xlsx", "Register")

        row = data[0]

        register.click_register_link()
        register.enter_first_name(row[0])
        register.enter_last_name(row[1])
        register.enter_email(row[2])
        register.enter_password(str(row[3]))
        register.enter_confirm_password(str(row[4]))
        register.click_register_button()

        assert register.get_success_message() == "Your registration completed"

        self.log.info("Registration Completed Successfully")

    @pytest.mark.Jeeva
    @pytest.mark.order(2)
    def test_checkout_withlogin(self):

        self.log.info("Checkout Login Test Started")

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

        self.log.info("Login Successful")

        checkout = checkoutAction(self.driver)
        act = checkout.checkout_Text()
        print(act)

        self.log.info("Checkout Page Opened Successfully")

    @pytest.mark.Jeeva
    @pytest.mark.order(3)
    def test_checkout_withGuest(self):

        self.log.info("Guest Checkout Test Started")

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

        self.log.info("Guest Checkout Successful")

    @pytest.mark.Jeeva
    @pytest.mark.order(4)
    @pytest.mark.parametrize(
    "Firstname,Lastname,Email,Company,Country,City,Address1,Address2,postalcode,Phonenumber,Faxnumber",
    get_data("TestData/TestData.xlsx", "billingForm")
)
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

        checkout.form_fill(
            Firstname, Lastname, Email, Company,
            Country, City, Address1, Address2,
            postalcode, Phonenumber, Faxnumber
        )

        time.sleep(5)

        act = checkout.shippingText()
        exp = "Select a shipping address from your address book or enter a new address."

        assert act == exp, "Shipping address text mismatch"

        self.log.info("Billing Address Form Submitted Successfully")

        time.sleep(10)

    @pytest.mark.Jeeva
    @pytest.mark.order(5)
    @pytest.mark.parametrize(
    "Firstname,Lastname,Company,Country,City,Address1,Address2,postalcode,Phonenumber,Faxnumber",
    CsvReader.get_data("TestData/CheckoutTestData.csv")
)
    def test_Checkout_Invalid_fill_form(self,Firstname,Lastname,Company,Country,City,Address1,Address2,\
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

        checkout.invalid_form_fill(
            Firstname, Lastname, Company,
            Country, City, Address1, Address2,
            postalcode, Phonenumber, Faxnumber
        )

        time.sleep(5)

        act = checkout.email_require_Text()
        exp = "required."

        assert exp in act

        print("Email is required")

        self.log.info("Email Required Validation Verified")

    @pytest.mark.Jeeva
    def test_click_in_store_pickup(self):

        self.log.info("In Store Pickup Test Started")

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

        checkout.click_the_bill_continue()
        checkout.click_skipping_checkbox()
        checkout.click_skipping()

        act = checkout.CocText()
        print(act)

        exp = "Cash"
        assert exp in act

        print("Payment page is opened")

        self.log.info("Cash Payment Page Opened Successfully")

        time.sleep(10)
