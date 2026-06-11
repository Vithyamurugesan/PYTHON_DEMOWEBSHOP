from Pages.RegisterPage import RegisterPage
import time

class RegisterAction:

    def __init__(self, driver):

        self.driver = driver
        self.registerPage = RegisterPage()

    def click_register_link(self):

        self.driver.find_element(
            *self.registerPage.get_register_link()
        ).click()

    def enter_first_name(self, first_name):

        self.driver.find_element(
            *self.registerPage.get_first_name()
        ).send_keys(first_name)

    def enter_last_name(self, last_name):

        self.driver.find_element(
            *self.registerPage.get_last_name()
        ).send_keys(last_name)

    def enter_email(self, email):

        unique_email = (
            email +
            str(int(time.time())) +
            "@gmail.com"
        )

        self.driver.find_element(
            *self.registerPage.get_email()
        ).send_keys(unique_email)

    def enter_password(self, password):

        self.driver.find_element(
            *self.registerPage.get_password()
        ).send_keys(password)

    def enter_confirm_password(self, confirm_password):

        self.driver.find_element(
            *self.registerPage.get_confirm_password()
        ).send_keys(confirm_password)

    def click_register_button(self):

        self.driver.find_element(
            *self.registerPage.get_register_button()
        ).click()

    def get_success_message(self):

        return self.driver.find_element(
            *self.registerPage.get_success_message()
        ).text