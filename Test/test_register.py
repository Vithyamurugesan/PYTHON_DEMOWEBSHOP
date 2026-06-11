from Actions.RegisterAction import RegisterAction
from Configuration.configReader import ReadConfig


class TestRegistration:

    baseURL = ReadConfig.get_base_url()

    def test_register_new_user(self, setup_and_teardown):


        register = RegisterAction(self.driver)

        register.click_register_link()

        register.register_from_excel(
            "registerData.xlsx",
            "Sheet1",
            0
        )

        register.click_register_button()

        assert register.get_success_message() == \
               "Your registration completed"

    def test_existing_user(self, setup_and_teardown):


        register = RegisterAction(self.driver)

        register.click_register_link()

        register.enter_name_from_excel(
            "registerData.xlsx",
            "Sheet1",
            1
        )

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

        assert register.get_existing_email_error() == \
               "The specified email already exists"