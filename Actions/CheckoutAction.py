import time
import pytest
from Actions.BaseAction import BaseAction
from Pages.CheckoutPage import CheckoutPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from Utilities.excelReader import get_data

class checkoutAction(BaseAction):
    checkout=CheckoutPage()

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
  
    def form_fill(self,Firstname,Lastname,Email,Company,Country,City,Address1,Address2,\
                  postalcode,Phonenumber,Faxnumber):
        self.select_dropdown(self.checkout.get_exist_address(),"New Address")
        self.clear(self.checkout.get_bill_first_name())
        self.send_keys(self.checkout.get_bill_first_name(),Firstname)
        self.clear(self.checkout.get_bill_last_name())
        self.send_keys(self.checkout.get_bill_last_name(),Lastname)
        self.clear(self.checkout.get_bill_email())
        self.send_keys(self.checkout.get_bill_email(),Email)
        self.send_keys(self.checkout.get_bill_company(),Company)
        self.select_dropdown(self.checkout.get_bill_country(),Country)
        self.send_keys(self.checkout.get_bill_city(),City)
        self.send_keys(self.checkout.get_bill_address1(),Address1)
        self.send_keys(self.checkout.get_bill_address2(),Address2)
        self.send_keys(self.checkout.get_bill_zip(),postalcode)
        self.send_keys(self.checkout.get_bill_number(),Phonenumber)
        self.send_keys(self.checkout.get_bill_fax(),Faxnumber)
        self.js_click(self.checkout.get_bill_continue())

    def click_the_bill_continue(self):
        self.js_click(self.checkout.get_bill_continue())

    def invalid_form_fill(self,Firstname,Lastname,Company,Country,City,Address1,Address2,\
                  postalcode,Phonenumber,Faxnumber):
        self.select_dropdown(self.checkout.get_exist_address(),"New Address")
        self.clear(self.checkout.get_bill_first_name())
        self.send_keys(self.checkout.get_bill_first_name(),Firstname)
        self.clear(self.checkout.get_bill_last_name())
        self.send_keys(self.checkout.get_bill_last_name(),Lastname)
        self.clear(self.checkout.get_bill_email())
        #self.send_keys(self.checkout.get_bill_email(),Email)
        self.send_keys(self.checkout.get_bill_company(),Company)
        self.select_dropdown(self.checkout.get_bill_country(),Country)
        self.send_keys(self.checkout.get_bill_city(),City)
        self.send_keys(self.checkout.get_bill_address1(),Address1)
        self.send_keys(self.checkout.get_bill_address2(),Address2)
        self.send_keys(self.checkout.get_bill_zip(),postalcode)
        self.send_keys(self.checkout.get_bill_number(),Phonenumber)
        self.send_keys(self.checkout.get_bill_fax(),Faxnumber)
        self.js_click(self.checkout.get_bill_continue())

    def shippingText(self):
        return self.get_text(self.checkout.get_shipping_text())
    
    def guest_checkout(self):
        self.js_click(self.checkout.get_guest_checkout())
    
    def checkout_Text(self):
        return self.get_text(self.checkout.get_checkoutText())

    def registrion_click(self):
        self.js_click(self.checkout.get_registration())

    def email_require_Text(self):
        return self.get_text(self.checkout.get_emailRequire())
    
    def click_skipping_checkbox(self):
        self.click(self.checkout.get_skipping_clickbox())

    def click_skipping(self):
        self.js_click(self.checkout.get_skipping_contnue())

    def CocText(self):
        return self.get_text(self.checkout.get_cocText())

    




