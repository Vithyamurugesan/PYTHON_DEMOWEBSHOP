import pytest
from Actions.AddressActions import AddressAction
from Utilities.CsvReader import CsvReader

@pytest.mark.Vetri
@pytest.mark.usefixtures("setup_and_teardown")
class TestAddress:

    @pytest.mark.parametrize(
        "data",
        CsvReader.get_address_data("TestData/AddressTestData.csv", "addAddress")
    )
    def test_add_new_address(self, data):

        address = AddressAction(self.driver)

        address.navigate_to_address_page()
        address.click_add_new_button()

        address.enter_first_name(data[0])
        address.enter_last_name(data[1])
        address.enter_email(data[2])
        address.enter_company(data[3])
        address.select_country(data[4])
        address.select_state(data[5])
        address.enter_city(data[6])
        address.enter_address1(data[7])
        address.enter_address2(data[8])
        address.enter_postal_code(data[9])
        address.enter_phone(data[10])
        address.enter_fax(data[11])

        address.click_save()

        assert address.verify_address_displayed(data[0], data[1])

    @pytest.mark.parametrize(
        "data",
        CsvReader.get_address_data("TestData/AddressTestData.csv", "missingRequired")
    )
    def test_add_address_without_required_fields(self, data):

        address = AddressAction(self.driver)

        address.navigate_to_address_page()
        address.click_add_new_button()

        address.enter_first_name(data[0])
        address.enter_last_name(data[1])
        address.enter_email(data[2])
        address.enter_company(data[3])
        address.select_country(data[4])
        address.select_state(data[5])
        address.enter_city(data[6])
        address.enter_address1(data[7])
        address.enter_address2(data[8])
        address.enter_postal_code(data[9])
        address.enter_phone(data[10])
        address.enter_fax(data[11])

        address.click_save()

        assert address.is_validation_displayed()

    @pytest.mark.parametrize(
        "data",
        CsvReader.get_address_data("TestData/AddressTestData.csv", "verifyAddress")
    )
    def test_verify_address_displayed(self, data):

        address = AddressAction(self.driver)

        address.navigate_to_address_page()
        address.click_add_new_button()

        address.enter_first_name(data[0])
        address.enter_last_name(data[1])
        address.enter_email(data[2])
        address.enter_company(data[3])
        address.select_country(data[4])
        address.select_state(data[5])
        address.enter_city(data[6])
        address.enter_address1(data[7])
        address.enter_address2(data[8])
        address.enter_postal_code(data[9])
        address.enter_phone(data[10])
        address.enter_fax(data[11])

        address.click_save()

        assert address.verify_address_displayed(data[0], data[1])