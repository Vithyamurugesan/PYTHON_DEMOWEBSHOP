import pytest
from Actions.CartAction import CartAction
from Utilities.excelReader import get_data


@pytest.mark.usefixtures("setup_and_teardown")
class TestCart:

    def test_add_to_cart(self):
        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        assert cart.check_cart(), "Product was not added to shopping cart"

    def test_add_multiple_products_to_cart(self):
        cart = CartAction(self.driver)
        cart.add_products_from_excel("TestData/cartData.xlsx", "CartProducts")
        cart.open_shopping_cart()
        assert cart.verify_products_displayed(), "Products are not displayed in shopping cart"
