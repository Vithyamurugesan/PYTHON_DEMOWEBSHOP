import pytest
import time

from Actions.LoginActions import LoginActions
from Actions.SearchAction import SearchAction
from Actions.CartAction import CartAction
from Actions.CheckoutAction import checkoutAction


@pytest.mark.usefixtures("setup_and_teardown")
class TestE2ESmoke:

    #E2E Smoke Test — Login → Search → Add to Cart → Checkout (billing step).
    def test_user_purchase_flow(self):

        #1.LOGIN 
        login = LoginActions(self.driver)
        login.click_login_link()
        login.enter_email("2k22cse@kiot.ac.in")
        login.enter_password("Vetri@1234")
        login.click_login_button()

        account=login.get_user_account_name()
        assert account is not None, "Login failed – account name not visible in the header"

        #2.SEARCH PRODUCT
        search=SearchAction(self.driver)
        search.searchProduct("book")
        search.clickSearch()

        assert search.verifySearchRedirect(), "Search did not redirect to the /search results page"

        #3.ADD PRODUCT TO CART
        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        cart.open_shopping_cart()

        assert cart.check_cart(), \
            "Product was not found in the shopping cart after adding"

        #4.PROCEED TO CHECKOUT
        cart.click_checkout()

        checkout = checkoutAction(self.driver)

        page_title=checkout.checkout_Text()
        assert page_title == "Checkout", f"Expected page title 'Checkout' but got '{page_title}'"

        #5.FILL BILLING FORM
        checkout.form_fill(
            "John",                         # First name
            "Tester",                       # Last name
            "2k22cse@kiot.ac.in",           # Email (must match logged-in account)
            "Test Company",                 # Company
            "United States",               # Country
            "New York",                     # City
            "123 Main Street",             # Address 1
            "Suite 1",                      # Address 2
            "10001",                        # Postal code
            "1234567890",                   # Phone
            "123456"                        # Fax
        )

        #6.VERIFY SHIPPING STEP IS REACHED
        time.sleep(3)

        shipping_label = checkout.shippingText()
        expected_label = (
            "Select a shipping address from your address book "
            "or enter a new address."
        )
        assert shipping_label == expected_label, f"Shipping step not reached.\nExpected: '{expected_label}'\nGot:      '{shipping_label}'"