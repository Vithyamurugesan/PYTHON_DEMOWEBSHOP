

from Actions.BaseAction import BaseActions
from Pages.CheckoutPage import CheckoutPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class checkoutAction(BaseActions):
    checkout=CheckoutPage()

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def form_fill(self):
        # Dummy function Stub needed Login Module and cart Module 
        # Login()
        # Cart()
        self.send_keys(self.checkout.get_bill_first_name(),"Jeeva")
        self.send_keys(self.checkout.get_bill_last_name(),"Pranesh")
        self.send_keys(self.checkout.get_bill_email(),"Jeeva")
        self.send_keys(self.checkout.get_bill_company(),"Jeeva")
        self.select_dropdown(self.checkout.get_bill_country,"India")
        self.send_keys(self.checkout.get_bill_city(),"salem")
        self.send_keys(self.checkout.get_bill_address1(),"sivaji nagar")
        self.send_keys(self.checkout.get_bill_address2(),"sivaji nagar1")
        self.send_keys(self.checkout.get_bill_zip(),"87654")
        self.send_keys(self.checkout.get_bill_number(),"987654323456")
        self.send_keys(self.checkout.get_bill_fax(),"34567876")





