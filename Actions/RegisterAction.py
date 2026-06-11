import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.RegisterPage import RegisterPage
from Utilities.excelReader import get_data


class RegisterAction:

    def __init__(self, driver):

        self.driver = driver
        self.page = RegisterPage()

    def click_register_link(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.page.get_register_link()
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def enter_first_name(self, firstname):

        self.driver.find_element(
            *self.page.get_first_name()
        ).send_keys(firstname)

    def enter_last_name(self, lastname):

        self.driver.find_element(
            *self.page.get_last_name()
        ).send_keys(lastname)

    def enter_email(self, email):

        self.driver.find_element(
            *self.page.get_email()
        ).send_keys(email)

    def enter_password(self, password):

        self.driver.find_element(
            *self.page.get_password()
        ).send_keys(password)

    def enter_confirm_password(self, password):

        self.driver.find_element(
            *self.page.get_confirm_password()
        ).send_keys(password)

    def click_register_button(self):

        button = self.driver.find_element(
            *self.page.get_register_button()
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def click_continue_button(self):

        self.driver.find_element(
            *self.page.get_continue_button()
        ).click()

    def get_success_message(self):

        return self.driver.find_element(
            *self.page.get_success_message()
        ).text

    def get_existing_email_error(self):

        return self.driver.find_element(
            *self.page.get_existing_email_error()
        ).text

    def register_from_excel(
            self,
            file_name,
            sheet_name,
            row
    ):

        data = get_data(file_name, sheet_name)

        first_name = data[row][0]
        last_name = data[row][1]
        email = data[row][2]
        password = data[row][3]
        confirm_password = data[row][4]

        unique_email = (
            email.split("@")[0]
            + str(int(time.time()))
            + "@gmail.com"
        )

        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(unique_email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)

        return unique_email