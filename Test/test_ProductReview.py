from selenium import webdriver
import time
from Actions import ProductReviewAction
from Actions.CheckoutAction import checkoutAction
import pytest
from Actions.LoginActions import LoginActions
from Utilities.excelReader import get_data
from Utilities.CsvReader import CsvReader
from Utilities.configReader import ReadConfig
from Actions.CartAction import CartAction
from Actions.RegisterAction import RegisterAction
from Actions.ProductReviewAction import ProductreviewAction


@pytest.mark.usefixtures("setup_and_teardown")
class TestProductReview:

    def test_productReview_with_login(self):
        actions = LoginActions(self.driver)

        actions.click_login_link()
        actions.enter_email(ReadConfig.get_email())
        actions.enter_password(ReadConfig.get_password())
        actions.click_login_button()

        assert actions.get_user_account_name() is not None


        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()

        review = ProductreviewAction(self.driver)
        review.Review_click()
        act =review.review_Page()
        assert "Product reviews" in act
        print("Product reviews is Display")
        review.review_Title()
        review.review_Con()
        review.review_submit()
        act=review.review_Display()
        
        assert "review is successfully"in act
        print("Product review is successfully added.")
        time.sleep(5)

    @pytest.mark.Jeeva
    def test_productReview_without_login(self):
        
        cart = CartAction(self.driver)
        cart.open_books_page()
        cart.open_computing_book_page()

        review = ProductreviewAction(self.driver)
        review.Review_click()
        act =review.review_Page()
        assert "Product reviews" in act
        print("Product reviews is Display")

        act =review.review_failedText()

        assert "Only registered users can write reviews"==act
        print("Only registered users can write reviews")
        time.sleep(5)
