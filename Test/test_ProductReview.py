from selenium import webdriver
import time
import pytest

from Actions.LoginActions import LoginActions
from Actions.CartAction import CartAction
from Actions.ProductReviewAction import ProductreviewAction
from Utilities.configReader import ReadConfig
from Utilities.logCreator import get_logger


@pytest.mark.usefixtures("setup_and_teardown")
class TestProductReview:

    log = get_logger()

    @pytest.mark.Jeeva
    def test_productReview_with_login(self):

        self.log.info("Product Review Test With Login Started")

        actions = LoginActions(self.driver)

        actions.click_login_link()
        actions.enter_email(ReadConfig.get_email())
        actions.enter_password(ReadConfig.get_password())
        actions.click_login_button()

        assert actions.get_user_account_name() is not None
        self.log.info("Login Successful")

        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()

        review = ProductreviewAction(self.driver)
        review.Review_click()

        act = review.review_Page()
        assert "Product reviews" in act
        self.log.info("Product Review Page Displayed")

        review.review_Title()
        review.review_Con()
        review.review_submit()

        act = review.review_Display()
        assert "review is successfully" in act
        self.log.info("Product Review Added Successfully")

        print("Product review is successfully added.")
        self.log.info("Product Review Test With Login Passed")

        time.sleep(5)

    @pytest.mark.Jeeva
    def test_productReview_without_login(self):

        self.log.info("Product Review Test Without Login Started")

        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()

        review = ProductreviewAction(self.driver)
        review.Review_click()

        act = review.review_Page()
        assert "Product reviews" in act
        print("Product reviews is Display")
        self.log.info("Product Review Page Displayed")

        act = review.review_failedText()

        assert "Only registered users can write reviews" == act
        print("Only registered users can write reviews")
        self.log.info("Review Restriction Message Verified")

        self.log.info("Product Review Test Without Login Passed")
        time.sleep(5)