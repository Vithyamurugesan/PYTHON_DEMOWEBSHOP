from selenium import webdriver
import time
from Actions.CheckoutAction import checkoutAction

class TestCheckout:
    
    def test_Checkout_RegisterUser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/onepagecheckout")

        checkout=checkoutAction(driver)
        checkout.form_fill()
        time.sleep(10)