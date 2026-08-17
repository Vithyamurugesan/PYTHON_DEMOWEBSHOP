import pytest

from Actions.WishlistAction import WishlistAction
from Utilities.CsvReader import CsvReader
from Utilities.logCreator import get_logger


logger = get_logger()


@pytest.mark.Vetri
@pytest.mark.usefixtures("setup_and_teardown")
class TestWishlist:


    @pytest.mark.parametrize("product",CsvReader.get_wishlist_data("TestData/WishlistTestData.csv","addWishlist"))
    def test_add_product_to_wishlist(self, product):

        logger.info(f"Starting add product to wishlist test for product: {product}")

        wishlist = WishlistAction(self.driver)

        wishlist.clearWishlist()
        logger.info("Wishlist cleared successfully")

        wishlist.addProductToWishlist(product)
        logger.info(f"Product added to wishlist: {product}")

        assert wishlist.verifySuccessMessage("The product has been added to your wishlist")
        logger.info("Wishlist success message verified")

        wishlist.navigateToWishlist()
        logger.info("Navigated to wishlist page")

        assert wishlist.verifyProductInWishlist(product)
        logger.info(f"Product verified in wishlist: {product}")



    @pytest.mark.parametrize("product",CsvReader.get_wishlist_data("TestData/WishlistTestData.csv","removeWishlist"))
    def test_remove_product_from_wishlist(self, product):

        logger.info(f"Starting remove product from wishlist test for product: {product}")

        wishlist = WishlistAction(self.driver)

        wishlist.clearWishlist()
        logger.info("Wishlist cleared successfully")

        wishlist.addProductToWishlist(product)
        logger.info(f"Product added to wishlist before removal: {product}")

        wishlist.removeProductFromWishlist()
        logger.info("Product removed from wishlist")

        assert wishlist.verifyEmptyWishlistMessage()
        logger.info("Empty wishlist message verified")



    @pytest.mark.parametrize("product",CsvReader.get_wishlist_data("TestData/WishlistTestData.csv","wishlistToCart"))
    def test_move_wishlist_product_to_cart(self, product):

        logger.info(f"Starting move wishlist product to cart test for product: {product}")

        wishlist = WishlistAction(self.driver)

        wishlist.clearWishlist()
        logger.info("Wishlist cleared successfully")

        wishlist.addProductToWishlist(product)
        logger.info(f"Product added to wishlist: {product}")

        assert wishlist.verifySuccessMessage("The product has been added to your wishlist")
        logger.info("Wishlist add success message verified")

        wishlist.moveWishlistProductToCart()
        logger.info("Wishlist product moved to cart")

        assert wishlist.verifyProductInCart(product)
        logger.info(f"Product verified in cart: {product}")



    @pytest.mark.parametrize("product",CsvReader.get_wishlist_data("TestData/WishlistTestData.csv","displayWishlist"))
    def test_verify_product_displayed_in_wishlist(self, product):

        logger.info(f"Starting verify wishlist product display test for product: {product}")

        wishlist = WishlistAction(self.driver)

        wishlist.clearWishlist()
        logger.info("Wishlist cleared successfully")

        wishlist.addProductToWishlist(product)
        logger.info(f"Product added to wishlist: {product}")

        wishlist.navigateToWishlist()
        logger.info("Navigated to wishlist page")

        assert wishlist.verifyProductInWishlist(product)
        logger.info(f"Product displayed successfully in wishlist: {product}")