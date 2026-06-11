from selenium.webdriver.common.by import By

class RegisterPage:

    def __init__(self):

        self.__registerLink = (
            By.XPATH,
            "//a[contains(@class,'ico-register')]"
        )

        self.__firstNameField = (
            By.XPATH,
            "//label[text()='First name:']/following::input[@id='FirstName']"
        )

        self.__lastNameField = (
            By.XPATH,
            "//label[text()='Last name:']/following::input[@id='LastName']"
        )

        self.__emailField = (
            By.XPATH,
            "//label[text()='Email:']/following::input[@id='Email']"
        )

        self.__passwordField = (
            By.XPATH,
            "//label[text()='Password:']/following::input[@id='Password']"
        )

        self.__confirmPasswordField = (
            By.XPATH,
            "//label[text()='Confirm password:']/following::input[@id='ConfirmPassword']"
        )

        self.__registerButton = (
            By.XPATH,
            "//div[@class='buttons']/descendant::input[@id='register-button']"
        )

        self.__continueButton = (
            By.XPATH,
            "//div[@class='buttons']/descendant::input[@value='Continue']"
        )

        self.__registrationSuccessMessage = (
            By.XPATH,
            "//div[@class='result']"
        )

        self.__existingEmailError = (
            By.XPATH,
            "//div[@class='validation-summary-errors']/descendant::li"
        )

        self.__firstNameError = (
            By.XPATH,
            "//span[@for='FirstName']"
        )

        self.__lastNameError = (
            By.XPATH,
            "//span[@for='LastName']"
        )

        self.__emailError = (
            By.XPATH,
            "//span[@for='Email']"
        )

        self.__passwordError = (
            By.XPATH,
            "//span[@for='Password']"
        )

        self.__confirmPasswordError = (
            By.XPATH,
            "//span[@for='ConfirmPassword']"
        )

    def get_register_link(self):
        return self.__registerLink

    def get_first_name(self):
        return self.__firstNameField

    def get_last_name(self):
        return self.__lastNameField

    def get_email(self):
        return self.__emailField

    def get_password(self):
        return self.__passwordField

    def get_confirm_password(self):
        return self.__confirmPasswordField

    def get_register_button(self):
        return self.__registerButton

    def get_continue_button(self):
        return self.__continueButton

    def get_success_message(self):
        return self.__registrationSuccessMessage

    def get_existing_email_error(self):
        return self.__existingEmailError

    def get_first_name_error(self):
        return self.__firstNameError

    def get_last_name_error(self):
        return self.__lastNameError

    def get_email_error(self):
        return self.__emailError

    def get_password_error(self):
        return self.__passwordError

    def get_confirm_password_error(self):
        return self.__confirmPasswordError