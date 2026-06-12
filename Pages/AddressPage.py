from selenium.webdriver.common.by import By

class AddressPage:

    def __init__(self):

        self.__first_name=(By.ID, "Address_FirstName")
        self.__last_name=(By.ID, "Address_LastName")
        self.__email=(By.ID, "Address_Email")
        self.__company=(By.ID, "Address_Company")
        self.__country=(By.ID, "Address_CountryId")
        self.__state=(By.ID, "Address_StateProvinceId")
        self.__city=(By.ID, "Address_City")
        self.__address1=(By.ID, "Address_Address1")
        self.__address2=(By.ID, "Address_Address2")
        self.__postal_code=(By.ID, "Address_ZipPostalCode")
        self.__phone=(By.ID, "Address_PhoneNumber")
        self.__fax_number=(By.ID, "Address_FaxNumber")
        self.__save=(By.CSS_SELECTOR,"input.button-1.save-address-button")
        self.__add_new_button=(By.CSS_SELECTOR,"input.button-1.add-address-button")
        self.__validation_messages=(By.CSS_SELECTOR,"span.field-validation-error")
        self.__address_cards=(By.CSS_SELECTOR,"div.section.address-item")


    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_company(self):
        return self.__company

    def get_country(self):
        return self.__country

    def get_state(self):
        return self.__state

    def get_city(self):
        return self.__city

    def get_address1(self):
        return self.__address1

    def get_address2(self):
        return self.__address2

    def get_postal_code(self):
        return self.__postal_code

    def get_phone(self):
        return self.__phone

    def get_fax_number(self):
        return self.__fax_number

    def get_save(self):
        return self.__save

    def get_add_new_button(self):
        return self.__add_new_button

    def get_validation_messages(self):
        return self.__validation_messages

    def get_address_cards(self):
        return self.__address_cards