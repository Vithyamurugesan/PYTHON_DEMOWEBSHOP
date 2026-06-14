from Actions.BaseAction import BaseAction
from Pages.ContactPage import ContactPage

class ContactAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.page = ContactPage()

    def click_contact_link(self):
        self.click(self.page.get_contact_link())

    def get_name_value(self):
        return self.find(self.page.get_name_field()).get_attribute("value")

    def get_email_value(self):
        return self.find(self.page.get_email_field()).get_attribute("value")