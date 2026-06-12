from selenium.webdriver.common.by import By

class RegisterPage:

    def __init__(self):

        self.__registerLink = ( By.XPATH,"//div[@class='header-links']/descendant::a[contains(@class,'ico-register')]")

        self.__firstNameField = (By.XPATH,"//label[text()='First name:']/following-sibling::input")

        self.__lastNameField = ( By.XPATH,"//label[text()='Last name:']/following-sibling::input")

        self.__emailField = (By.XPATH,"//label[text()='Email:']/following-sibling::input")

        self.__passwordField = (By.XPATH,"//label[text()='Password:']/following-sibling::input")

        self.__confirmPasswordField = (By.XPATH,"//label[text()='Confirm password:']/following-sibling::input")

        self.__registerButton = (By.XPATH, "//div[@class='buttons']/child::input[@id='register-button']")

        self.__continueButton = (By.XPATH, "//div[@class='buttons']/child::input[@value='Continue']")

        self.__registrationSuccessMessage = (By.XPATH,"//div[@class='result']")

        self.__existingEmailError = (By.XPATH,"//div[@class='validation-summary-errors']/descendant::li")

        self.__emailError = (By.XPATH,"//input[@id='Email']/following::span[@for='Email'][1]")

        self.__passwordError = ( By.XPATH,"//input[@id='Password']/following::span[@for='Password'][1]")

        

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

    def get_email_error(self):
        return self.__emailError

    def get_password_error(self):
        return self.__passwordError
    

