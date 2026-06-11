

import time

from Actions.BaseAction import BaseAction
from Pages.CheckoutPage import CheckoutPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class checkoutAction(BaseAction):
    checkout=CheckoutPage()

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def form_fill(self):
        self.select_dropdown(self.checkout.get_exist_address(),"New Address")
        self.clear(self.checkout.get_bill_first_name())
        self.send_keys(self.checkout.get_bill_first_name(),"Jeeva")
        self.clear(self.checkout.get_bill_last_name())
        self.send_keys(self.checkout.get_bill_last_name(),"Pranesh")
        self.clear(self.checkout.get_bill_email())
        self.send_keys(self.checkout.get_bill_email(),"Jeeva@gmail.com")
        self.select_dropdown(self.checkout.get_bill_country(),"American Samoa")
        self.send_keys(self.checkout.get_bill_city(),"salem")
        self.send_keys(self.checkout.get_bill_address1(),"sivaji nagar")
        self.send_keys(self.checkout.get_bill_address2(),"sivaji nagar1")
        self.send_keys(self.checkout.get_bill_zip(),"87654")
        self.send_keys(self.checkout.get_bill_number(),"987654323456")
        self.send_keys(self.checkout.get_bill_fax(),"34567876")
        self.js_click(self.checkout.get_bill_continue())

    def shippingText(self):
        return self.get_text(self.checkout.get_shipping_text())
    
    def guest_checkout(self):
        self.js_click(self.checkout.get_guest_checkout())
    
    def checkout_Text(self):
        return self.get_text(self.checkout.get_checkoutText())

    def registrion_click(self):
        self.js_click(self.checkout.get_registration())





