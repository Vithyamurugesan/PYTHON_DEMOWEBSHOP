import pytest

from Actions.AddressActions import AddressAction
from Utilities.CsvReader import CsvReader
from Utilities.logCreator import get_logger


logger = get_logger()


@pytest.mark.Vetri
@pytest.mark.usefixtures("setup_and_teardown")
class TestAddress:


    @pytest.mark.parametrize(
        "data",
        CsvReader.get_address_data("TestData/AddressTestData.csv", "addAddress")
    )
    def test_add_new_address(self, data):

        logger.info(f"Starting add new address test for user: {data[0]} {data[1]}")

        address = AddressAction(self.driver)

        address.navigate_to_address_page()
        logger.info("Navigated to address page")

        address.click_add_new_button()
        logger.info("Clicked add new address button")

        address.enter_first_name(data[0])
        address.enter_last_name(data[1])
        address.enter_email(data[2])
        address.enter_company(data[3])
        logger.info("Entered personal and company details")

        address.select_country(data[4])
        address.select_state(data[5])
        logger.info(f"Selected country: {data[4]} and state: {data[5]}")

        address.enter_city(data[6])
        address.enter_address1(data[7])
        address.enter_address2(data[8])
        address.enter_postal_code(data[9])
        address.enter_phone(data[10])
        address.enter_fax(data[11])
        logger.info("Entered complete address details")

        address.click_save()
        logger.info("Clicked save address button")

        assert address.verify_address_displayed(data[0], data[1])
        logger.info("New address verified successfully")



    @pytest.mark.parametrize(
        "data",
        CsvReader.get_address_data("TestData/AddressTestData.csv", "missingRequired")
    )
    def test_add_address_without_required_fields(self, data):

        logger.info("Starting add address without required fields test")

        address = AddressAction(self.driver)

        address.navigate_to_address_page()
        logger.info("Navigated to address page")

        address.click_add_new_button()
        logger.info("Clicked add new address button")

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
        logger.info("Entered address data with missing required field")

        address.click_save()
        logger.info("Clicked save button")

        assert address.is_validation_displayed()
        logger.info("Validation message verified successfully")



    @pytest.mark.parametrize(
        "data",
        CsvReader.get_address_data("TestData/AddressTestData.csv", "verifyAddress")
    )
    def test_verify_address_displayed(self, data):

        logger.info(f"Starting verify address test for user: {data[0]} {data[1]}")

        address = AddressAction(self.driver)

        address.navigate_to_address_page()
        logger.info("Navigated to address page")

        address.click_add_new_button()
        logger.info("Clicked add new address button")

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
        logger.info("Entered address details")

        address.click_save()
        logger.info("Saved address details")

        assert address.verify_address_displayed(data[0], data[1])
        logger.info("Address displayed verification completed successfully")