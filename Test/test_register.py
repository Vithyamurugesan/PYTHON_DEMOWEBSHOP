from atexit import register

import pytest
from Utilities.CsvReader import CsvReader
from Actions.RegisterAction import RegisterAction
from Utilities.excelReader import get_data
from Utilities.configReader import ReadConfig

class TestRegistration:

<<<<<<< HEAD
    def test_register_user(self,setup_and_teardown):
#
=======
    def test_register_user(self,setup_and_teardown: None):

>>>>>>> 69e003c538df7874743b0273829bd3abebfe0814
        register = RegisterAction(self.driver)
        data = get_data("TestData/TestData.xlsx","Register")

        row = data[0]

        register.click_register_link()

        register.enter_first_name(row[0])

        register.enter_last_name(row[1])

        register.enter_email(row[2])

        register.enter_password(str(row[3]))

        register.enter_confirm_password(str(row[4]))

        register.click_register_button()

        assert register.get_success_message() == "Your registration completed"

    @pytest.mark.parametrize( "data",get_data("TestData/TestData.xlsx", "InvalidEmail"))
    def test_invalid_email(self, setup_and_teardown: None, data: Any):
        register = RegisterAction(self.driver)

        register.click_register_link()

        register.enter_first_name(data[0])

        register.enter_last_name(data[1])

        register.enter_normal_email(data[2])

        register.enter_password(str(data[3]))

        register.enter_confirm_password(str(data[4]))

        register.click_register_button()

        assert (register.get_email_error()==data[5])

    def test_empty_fields(self,setup_and_teardown):
        register = RegisterAction(self.driver)

        register.click_register_link()

        register.enter_first_name(ReadConfig.get_first_name())
        
        register.enter_last_name(ReadConfig.get_last_name())
        
        register.enter_normal_email(ReadConfig.get_email())
        
        register.enter_password("")
        
        register.enter_confirm_password("")
        
        register.click_register_button()
        
        assert (register.get_password_error()==ReadConfig.get_password_required_error())