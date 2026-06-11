from Actions.RegisterAction import RegisterAction
from Utilities.excelReader import get_data

class TestRegistration:

    def test_register_user(
            self,
            setup_and_teardown
    ):

        register = RegisterAction(self.driver)

        data = get_data(
            "TestData/TestData.xlsx",
            "Register"
        )

        row = data[0]

        register.click_register_link()

        register.enter_first_name(row[0])

        register.enter_last_name(row[1])

        register.enter_email(row[2])

        register.enter_password(str(row[3]))

        register.enter_confirm_password(str(row[4]))

        register.click_register_button()

        assert register.get_success_message() == "Your registration completed"