from selenium.webdriver.common.by import By

class ContactPage:

    def __init__(self):
        self.__contact_link = (By.XPATH,"//div[@class='column information']//a[text()='Contact us']")
        self.__name_field = (By.ID, "FullName")
        self.__email_field = (By.ID, "Email")

    def get_contact_link(self):
        return self.__contact_link

    def get_name_field(self):
        return self.__name_field

    def get_email_field(self):
        return self.__email_field