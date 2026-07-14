from selenium.webdriver.common.by import By

class NewsletterPage:

    def __init__(self):
        self.__email = (By.ID, "newsletter-email")
        self.__subscribe = (By.ID, "newsletter-subscribe-button")
        self.__result = (By.ID, "newsletter-result-block")

    def get_newsletter_email(self):
        return self.__email

    def get_subscribe_button(self):
        return self.__subscribe

    def get_subscription_result(self):
        return self.__result