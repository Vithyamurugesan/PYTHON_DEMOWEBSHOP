from Actions.BaseAction import BaseAction
from Pages.AddressPage import AddressPage
from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AddressAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.address_page = AddressPage()

    def click_add_new_button(self):
        self.click(self.address_page.get_add_new_button())

    def enter_first_name(self, value):
        self.send_keys(self.address_page.get_first_name(), value)

    def enter_last_name(self, value):
        self.send_keys(self.address_page.get_last_name(), value)

    def enter_email(self, value):
        self.send_keys(self.address_page.get_email(), value)

    def enter_company(self, value):
        self.send_keys(self.address_page.get_company(), value)

    def select_country(self, value):
        if value and value.strip():
            self.select_dropdown(self.address_page.get_country(), value)

    def select_state(self, value):
        if value and value.strip():
            self.wait.until(EC.presence_of_element_located((By.XPATH,f"//select[@id='Address_StateProvinceId']/option[text()='{value}']")))
            self.select_dropdown(self.address_page.get_state(), value)

    def enter_city(self, value):
        self.send_keys(self.address_page.get_city(), value)

    def enter_address1(self, value=""):
        self.send_keys(self.address_page.get_address1(), value)

    def enter_address2(self, value):
        self.send_keys(self.address_page.get_address2(), value)

    def enter_postal_code(self, value):
        self.send_keys(self.address_page.get_postal_code(), value)

    def enter_phone(self, value):
        self.send_keys(self.address_page.get_phone(), value)

    def enter_fax(self, value):
        self.send_keys(self.address_page.get_fax_number(), value)

    def click_save(self):
        self.click(self.address_page.get_save())

    def get_validation_messages(self):
        return self.driver.find_elements(*self.address_page.get_validation_messages())

    def get_address_cards(self):
        return self.driver.find_elements(*self.address_page.get_address_cards())

    def verify_address_displayed(self, first_name, last_name):
        cards=self.get_address_cards()
        for card in cards:
            if first_name in card.text and last_name in card.text:
                return True
        return False

    def is_validation_displayed(self):
        return len(self.get_validation_messages())>0
    
    def navigate_to_address_page(self):
        parsed=urlparse(self.driver.current_url)
        base_url=f"{parsed.scheme}://{parsed.netloc}"
        self.driver.get(f"{base_url}/customer/addresses")