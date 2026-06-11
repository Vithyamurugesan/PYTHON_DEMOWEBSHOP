from selenium.webdriver.common.by import By

class LoginPage:

    # LOGIN LOCATORS
    _login_link = (By.XPATH, "//a[contains(@class,'login')]")
    _email = (By.ID, "Email")
    _password = (By.XPATH, "//input[@id='Password']/parent::div/input")
    _login_btn = (By.CSS_SELECTOR, "input[value='Log in']")
    _user_account_name = (By.CSS_SELECTOR, ".header-links .account")
    _logout_link = (By.CSS_SELECTOR, ".ico-logout")

    _forgot_password_link = (By.XPATH, "//div[@class='inputs reversed']/child::span/a")
    _recovery_email = (By.ID, "Email")
    _recover_btn = (By.XPATH, "//div[@class='buttons']/child::input[@value='Recover']")
    _recovery_success_message = (By.XPATH, "//div[@class='result']/ancestor::div[@class='page-body']/div")
    _validation_message = (By.XPATH, "//input[@id='Email']/following-sibling::span[2]/span")
    _login_error_message = (By.CSS_SELECTOR, ".validation-summary-errors")

    def get_login_link(self): return self._login_link
    def get_email(self): return self._email
    def get_password(self): return self._password
    def get_login_btn(self): return self._login_btn
    def get_user_account_name(self): return self._user_account_name
    def get_logout_link(self): return self._logout_link

    def get_forgot_password_link(self): return self._forgot_password_link
    def get_recovery_email(self): return self._recovery_email
    def get_recover_btn(self): return self._recover_btn
    def get_recovery_success_message(self): return self._recovery_success_message
    def get_validation_message(self): return self._validation_message
    def get_login_error_message(self): return self._login_error_message