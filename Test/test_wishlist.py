import pytest
from Actions.WishlistAction import WishlistAction


@pytest.mark.usefixtures("setup_and_teardown")
class TestWishlist:

    def test_add_product_to_wishlist(self):

        wishlist=WishlistAction(self.driver)

        product="Health Book"

        wishlist.addProductToWishlist(product)

        assert wishlist.verifySuccessMessage("The product has been added to your wishlist")
        assert wishlist.verifyProductInWishlist(product)

    def test_remove_product_from_wishlist(self):

        wishlist = WishlistAction(self.driver)
        wishlist.addProductToWishlist("Health Book")
        wishlist.removeProductFromWishlist()

        assert wishlist.verifyEmptyWishlistMessage()

    def test_move_wishlist_product_to_cart(self):

        wishlist = WishlistAction(self.driver)
        product = "Health Book"
        wishlist.addProductToWishlist(product)

        assert wishlist.verifySuccessMessage("The product has been added to your wishlist")

        wishlist.moveWishlistProductToCart()
        assert wishlist.verifyProductInCart(product)

    @pytest.mark.parametrize("product",[("Health Book")])
    def test_verify_product_displayed_in_wishlist(self, product):

        wishlist = WishlistAction(self.driver)
        wishlist.addProductToWishlist(product)

        assert wishlist.verifyProductInWishlist(product)