from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self):
        self.__login_link = (By.XPATH, "//a[contains(@class,'login')]")
        self.__email = (By.ID, "Email")
        self.__password = (By.XPATH, "//input[@id='Password']/parent::div/input")
        self.__login_btn = (By.CSS_SELECTOR, "input[value='Log in']")
        self.__user_account_name = (By.CSS_SELECTOR, ".header-links .account")
        self.__logout_link = (By.CSS_SELECTOR, ".ico-logout")
        self.__forgot_password_link = (By.XPATH, "//div[@class='inputs reversed']/child::span/a")
        self.__recovery_email = (By.ID, "Email")
        self.__recover_btn = (By.XPATH, "//div[@class='buttons']/child::input[@value='Recover']")
        self.__recovery_success_message = (By.XPATH,"//div[@class='result']/ancestor::div[@class='page-body']/div")
        self.__validation_message = (By.XPATH,"//input[@id='Email']/following-sibling::span[2]/span")
        self.__login_error_message = (By.CSS_SELECTOR, ".validation-summary-errors")

    def get_login_link(self):
        return self.__login_link

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_login_btn(self):
        return self.__login_btn

    def get_user_account_name(self):
        return self.__user_account_name

    def get_logout_link(self):
        return self.__logout_link

    def get_forgot_password_link(self):
        return self.__forgot_password_link

    def get_recovery_email(self):
        return self.__recovery_email

    def get_recover_btn(self):
        return self.__recover_btn

    def get_recovery_success_message(self):
        return self.__recovery_success_message

    def get_validation_message(self):
        return self.__validation_message

    def get_login_error_message(self):
        return self.__login_error_message
    