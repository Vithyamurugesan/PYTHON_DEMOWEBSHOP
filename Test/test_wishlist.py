import pytest
from Actions.WishlistAction import WishlistAction
from Utilities.CsvReader import CsvReader

@pytest.mark.Vetri
@pytest.mark.usefixtures("setup_and_teardown")
class TestWishlist:

    @pytest.mark.parametrize("product",CsvReader.get_wishlist_data("TestData/WishlistTestData.csv","addWishlist"))
    def test_add_product_to_wishlist(self, product):

        wishlist = WishlistAction(self.driver)

        wishlist.clearWishlist()

        wishlist.addProductToWishlist(product)

        assert wishlist.verifySuccessMessage("The product has been added to your wishlist")

        wishlist.navigateToWishlist()

        assert wishlist.verifyProductInWishlist(product)

    @pytest.mark.parametrize("product",CsvReader.get_wishlist_data("TestData/WishlistTestData.csv","removeWishlist"))
    def test_remove_product_from_wishlist(self, product):

        wishlist = WishlistAction(self.driver)

        wishlist.clearWishlist()

        wishlist.addProductToWishlist(product)

        wishlist.removeProductFromWishlist()

        assert wishlist.verifyEmptyWishlistMessage()

    @pytest.mark.parametrize("product",CsvReader.get_wishlist_data("TestData/WishlistTestData.csv","wishlistToCart"))
    def test_move_wishlist_product_to_cart(self, product):

        wishlist = WishlistAction(self.driver)

        wishlist.clearWishlist()

        wishlist.addProductToWishlist(product)

        assert wishlist.verifySuccessMessage("The product has been added to your wishlist")

        wishlist.moveWishlistProductToCart()

        assert wishlist.verifyProductInCart(product)

    @pytest.mark.parametrize("product",CsvReader.get_wishlist_data("TestData/WishlistTestData.csv","displayWishlist"))
    def test_verify_product_displayed_in_wishlist(self, product):

        wishlist = WishlistAction(self.driver)

        wishlist.clearWishlist()

        wishlist.addProductToWishlist(product)

        wishlist.navigateToWishlist()

        assert wishlist.verifyProductInWishlist(product)