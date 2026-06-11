import pytest
from Actions.CartAction import CartAction
from Utilities.excelReader import get_data
from Configuration.configReader import ReadConfig

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
        cart.add_products_from_excel("TestData/TestData.xlsx", "CartProducts")
        cart.open_shopping_cart()
        assert cart.verify_products_displayed(), "Products are not displayed in shopping cart"

    def test_cart_total_amount(self):
        cart = CartAction(self.driver)
        cart.add_products_from_excel("TestData/TestData.xlsx", "CartProducts")
        cart.open_shopping_cart()
        assert cart.verify_products_displayed(), "Products are not displayed in shopping cart"
        assert cart.verify_subtotal_displayed(), "Cart subtotal and total amount is not displayed"
 
    def test_empty_cart_message(self):
        cart = CartAction(self.driver)
        cart.open_empty_cart()
        assert ReadConfig.get_empty_cart_msg() in cart.get_empty_cart_message(), "Empty cart message is not displayed"

 
    @pytest.mark.parametrize("coupon", ["asdfg123", "1234567"])
    def test_invalid_coupon_code(self, coupon):
        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        cart.open_shopping_cart()
        cart.enter_coupon_code(coupon)
        cart.click_apply_coupon()
        assert ReadConfig.get_invalid_coupon_msg() in cart.get_validation_message(), \
            "Invalid coupon message is not displayed"
 

    @pytest.mark.parametrize("giftcard", ["gift1234", "giftcard123"])
    def test_invalid_gift_card_code(self, giftcard):
        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        cart.open_shopping_cart()
        cart.enter_gift_card_code(giftcard)
        cart.click_apply_gift_card()
        assert ReadConfig.get_invalid_coupon_msg() in cart.get_validation_message(), \
            "Invalid gift card message is not displayed"
 

    def test_update_cart_quantity(self):
        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        cart.open_shopping_cart()
        cart.update_quantity(ReadConfig.get_updated_quantity())
        cart.click_update_shopping_cart()
        assert cart.verify_updated_quantity(ReadConfig.get_updated_quantity()), \
            "Cart quantity was not updated"
 
    def test_remove_product_from_cart(self):
        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()
        cart.add_to_cart()
        cart.open_shopping_cart()
        cart.remove_product()
        cart.click_update_shopping_cart()
        assert cart.verify_removed_product(), "Product was not removed from shopping cart"