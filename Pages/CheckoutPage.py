from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self):

        self.__existAddress=(By.ID,"billing-address-select")
        self.__newAddress=(By.XPATH,"//select[@id='billing-address-select']/child::option[text()='New Address']")

        self.__billFirstName=(By.XPATH,"//label[@for='BillingNewAddress_FirstName']/following-sibling::input")
        self.__billLastName=(By.XPATH,"//label[@for='BillingNewAddress_LastName']/following-sibling::input")
        self.__billEmail=(By.XPATH,"//label[@for='BillingNewAddress_Email']/following-sibling::input")
        self.__billCompany=(By.XPATH,"//label[@for='BillingNewAddress_Company']/following-sibling::input")
        self.__billCountry=(By.XPATH,"//label[@for='BillingNewAddress_CountryId']/following-sibling::select")
        self.__billState=(By.XPATH,"//label[@for='BillingNewAddress_StateProvinceId']/following-sibling::select")
        self.__billCity=(By.XPATH,"//label[@for='BillingNewAddress_City']/following-sibling::input")
        self.__billAddress1=(By.XPATH,"//label[@for='BillingNewAddress_Address1']/following-sibling::input")
        self.__billAddress2=(By.XPATH,"//label[@for='BillingNewAddress_Address2']/following-sibling::input")
        self.__billZip=(By.XPATH,"//label[@for='BillingNewAddress_ZipPostalCode']/following-sibling::input")
        self.__billNumber=(By.XPATH,"//label[@for='BillingNewAddress_PhoneNumber']/following-sibling::input")
        self.__billFax=(By.XPATH,"//label[@for='BillingNewAddress_FaxNumber']/following-sibling::input")
        self.__billContinue=(By.XPATH,"//div[@id='billing-buttons-container']//descendant::input")
        self.__shippingText=(By.XPATH,"//label[text()='Select a shipping address from your address book or enter a new address.']")
        self.__wrongEmail=(By.XPATH,"//span[@class='field-validation-error']/parent::div")
        self.__guestCheckout=(By.XPATH,"//input[@value='Checkout as Guest']")
        self.__checkoutText=(By.XPATH,"//div[@class='page-title']/h1")
        self.__Regsiration=(By.XPATH,"//input[@class='button-1 register-button']")
        self.__EmailRequiedText = (By.XPATH,"//span[@class='field-validation-error']")


    def get_exist_address(self):
        return self.__existAddress

    def get_new_address(self):
        return self.__newAddress

    def get_bill_first_name(self):
        return self.__billFirstName

    def get_bill_last_name(self):
        return self.__billLastName

    def get_bill_email(self):
        return self.__billEmail

    def get_bill_company(self):
        return self.__billCompany

    def get_bill_country(self):
        return self.__billCountry

    def get_bill_state(self):
        return self.__billState

    def get_bill_city(self):
        return self.__billCity

    def get_bill_address1(self):
        return self.__billAddress1

    def get_bill_address2(self):
        return self.__billAddress2

    def get_bill_zip(self):
        return self.__billZip

    def get_bill_number(self):
        return self.__billNumber

    def get_bill_fax(self):
        return self.__billFax

    def get_bill_continue(self):
        return self.__billContinue

    def get_shipping_text(self):
        return self.__shippingText

    def get_wrong_email(self):
        return self.__wrongEmail
    
    def get_guest_checkout(self):
        return self.__guestCheckout

    def get_checkoutText(self):
        return self.__checkoutText
    
    def get_registration(self):
        return self.__Regsiration
    
    def get_emailRequire(self):
        return self.__EmailRequiedText