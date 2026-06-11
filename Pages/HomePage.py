from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self):
        self.__registerLink = (By.XPATH, "//a[contains(@class,'ico-register')]")
    def get_register_link(self):
        return self.__registerLink