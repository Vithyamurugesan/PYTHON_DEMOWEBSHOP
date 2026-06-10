import pytest
from Actions.LoginActions import LoginActions
from Utilities.excelReader import get_data

login_data = get_data("TestData/loginData.xlsx", "login")
recovery_data = get_data("TestData/loginData.xlsx", "recovery")

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    @pytest.mark.parametrize("email,password,type", login_data)
    def test_login(self, email, password, type):

        actions = LoginActions(self.driver)

        actions.click_login_link()
        actions.enter_email(email)
        actions.enter_password(password)
        actions.click_login_button()
        if type == "valid":
            assert actions.get_user_account_name() is not None

        elif type == "invalid":
            assert "Login was unsuccessful" in actions.get_login_error_message()

    @pytest.mark.parametrize("email,message", recovery_data)
    def test_recovery(self, email, message):
        actions = LoginActions(self.driver)

        actions.click_login_link()
        actions.click_forgot_password()

        if email is None:
            email = ""

        actions.enter_recovery_email(email)
        actions.click_recover_button()
        if message == "Email with instructions has been sent to you.":
            actual = actions.get_recovery_success_message()
            assert message in actual
        else:
            actual = actions.get_validation_message()
            assert message in actual