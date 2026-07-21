from Actions.BaseAction import BaseAction
from Pages.NewsletterPage import NewsletterPage


class NewsletterAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.page = NewsletterPage()

    def enter_newsletter_email(self, email):
        self.clear(self.page.get_newsletter_email())
        self.send_keys(self.page.get_newsletter_email(), email)

    def click_subscribe_button(self):
        self.click(self.page.get_subscribe_button())

    def get_subscription_message(self):
        return self.get_text(self.page.get_subscription_result())