from Actions.BaseAction import BaseAction
from Pages.LoginPage import LoginPage

class LoginActions(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.page = LoginPage()
    def click_login_link(self):
        self.click(self.page.get_login_link())

    def enter_email(self, email):
        email = email or "" 
        self.clear(self.page.get_email())
        self.send_keys(self.page.get_email(), email)

    def enter_password(self, password):
        password = password or ""  
        self.clear(self.page.get_password())
        self.send_keys(self.page.get_password(), password)

    def click_login_button(self):
        self.click(self.page.get_login_btn())

    def get_user_account_name(self):
        return self.get_text(self.page.get_user_account_name())

    def get_login_error_message(self):
        return self.get_text(self.page.get_login_error_message())


    def click_forgot_password(self):
        self.click(self.page.get_forgot_password_link())

    def enter_recovery_email(self, email):
        email = email or "" 
        self.clear(self.page.get_recovery_email())
        self.send_keys(self.page.get_recovery_email(), email)

    def click_recover_button(self):
        self.click(self.page.get_recover_btn())

    def get_recovery_success_message(self):
        return self.get_text(self.page.get_recovery_success_message())

    def get_validation_message(self):
        return self.get_text(self.page.get_validation_message())