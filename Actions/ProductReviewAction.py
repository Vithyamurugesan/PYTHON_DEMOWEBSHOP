import time
from webbrowser import get
import pytest
from Actions.BaseAction import BaseAction
from Pages.ProductReviewPage import ProductReview
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductreviewAction (BaseAction):
    
    PR=ProductReview()

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def Review_click(self):
        self.click(self.PR.get_reviw_BTN())
    def review_Page(self):
        return self.get_text(self.PR.get_review_Text())
    
    def review_Title(self):
        self.send_keys(self.PR.get_review_title(),"jeeva")

    def review_Con(self):
        self.send_keys(self.PR.get_review_GText(),"good boi")

    def review_submit(self):
        self.js_click(self.PR.get_review_submit())

    def review_Display(self):
        return self.get_text(self.PR.get_review_display())
    
    def review_failedText(self):
        return self.get_text(self.PR.get_review_failed())
