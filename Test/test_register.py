import pytest

from Actions.RegisterAction import RegistrationActions
from Utilities.configReader import ReadConfig
from Actions.RegisterActions import RegisterActions


class TestRegistration:

    baseURL = ReadConfig.get_base_url()

    def test_register_new_user(self, setup):

        self.driver = setup

        self.driver.get(self.baseURL)

        register = RegistrationActions(
            self.driver
        )

        register.click_register_link()

        register.register_from_excel(
            "TestData.xlsx",
            "Sheet2",
            0
        )

        register.click_register_button()

        actual = register.get_success_message()

        assert actual == "Your registration completed"

    def test_existing_user(self, setup):

        self.driver = setup

        self.driver.get(self.baseURL)

        register = RegistrationActions(
            self.driver
        )

        register.click_register_link()

        register.enter_first_name("Haritha")
        register.enter_last_name("K")

        register.enter_email(
            ReadConfig.get_email()
        )

        register.enter_password(
            ReadConfig.get_password()
        )

        register.enter_confirm_password(
            ReadConfig.get_password()
        )

        register.click_register_button()

        assert (
            register.get_existing_email_error()
            ==
            "The specified email already exists"
        )