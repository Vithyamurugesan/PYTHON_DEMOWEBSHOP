from Pages.RegisterPage import RegisterPage
from Actions.BaseAction import BaseAction
import time

class RegisterAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.registerPage = RegisterPage()

    def click_register_link(self):
        self.click(self.registerPage.get_register_link())

    def enter_first_name(self, first_name):
        self.send_keys(self.registerPage.get_first_name(), first_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.registerPage.get_last_name(), last_name)

    def enter_email(self, email):
        unique_email = email + str(int(time.time())) + "@gmail.com"
        self.send_keys(self.registerPage.get_email(), unique_email)

    def enter_password(self, password):
        self.send_keys(self.registerPage.get_password(), password)

    def enter_confirm_password(self, confirm_password):
        self.send_keys(self.registerPage.get_confirm_password(), confirm_password)

    def click_register_button(self):
        self.click(self.registerPage.get_register_button())

    def get_success_message(self):
        return self.get_text(self.registerPage.get_success_message())
    
    def enter_normal_email(self, email):
        self.send_keys(self.registerPage.get_email(),email)

    def get_email_error(self):
        return self.get_text(self.registerPage.get_email_error())
    
    def get_password_error(self):
        return self.get_text(self.registerPage.get_password_error())