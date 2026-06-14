import pytest

from Actions.LoginActions import LoginActions
from Actions.ContactAction import ContactAction
from Utilities.CsvReader import CsvReader
from Utilities.configReader import ReadConfig

contact_data = CsvReader.get_contact_data("TestData/contactData.csv")[:1]


@pytest.mark.usefixtures("setup_and_teardown")
class TestContact:

    @pytest.mark.parametrize("data", contact_data)
    def test_contact_with_login(self, data):

        login = LoginActions(self.driver)
        contact = ContactAction(self.driver)

        login.click_login_link()
        login.enter_email(ReadConfig.get_email())
        login.enter_password(ReadConfig.get_password())
        login.click_login_button()

        contact.click_contact_link()

        actual_name = contact.get_name_value()
        actual_email = contact.get_email_value()

        assert actual_name == data["name"]
        assert actual_email == data["email"]

    def test_contact_without_login(self):

        self.driver.delete_all_cookies()
        self.driver.get(ReadConfig.get_base_url())

        contact = ContactAction(self.driver)

        contact.click_contact_link()

        actual_name = contact.get_name_value()
        actual_email = contact.get_email_value()

        assert actual_name == ""
        assert actual_email == ""
        