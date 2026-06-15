from selenium.webdriver.common.by import By


class GiftCardPage:

    def __init__(self):
        self.__gift_cards_menu = (
            By.XPATH,
            "//ul[@class='top-menu']//a[contains(text(),'Gift Cards')]"
        )
        self.__virtual_gift_card = (
            By.XPATH,
            "//a[text()='$5 Virtual Gift Card']"
        )
        self.__recipient_name = (
            By.ID,
            "giftcard_1_RecipientName"
        )
        self.__recipient_email = (
            By.ID,
            "giftcard_1_RecipientEmail"
        )
        self.__sender_name = (
            By.ID,
            "giftcard_1_SenderName"
        )
        self.__add_to_cart = (
            By.XPATH,
            "//input[contains(@id,'add-to-cart-button')]"
        )
        self.__success_message = (
            By.XPATH,
            "//p[contains(text(),'The product has been added')]"
        )
        self.__shopping_cart = (
            By.XPATH,
            "//span[text()='Shopping cart']/ancestor::a"
        )
        self.__quantity = (
            By.XPATH,
            "//input[contains(@class,'qty-input')]"
        )
        self.__update_cart = (
            By.XPATH,
            "//input[@name='updatecart']"
        )
        self.__recipient_email_error = (
            By.XPATH,
            "//span[contains(@id,'RecipientEmail-error')]"
        )
        self.__sender_email = (By.ID, "giftcard_1_SenderEmail")

    def get_gift_cards_menu(self):
        return self.__gift_cards_menu

    def get_virtual_gift_card(self):
        return self.__virtual_gift_card

    def get_recipient_name(self):
        return self.__recipient_name

    def get_recipient_email(self):
        return self.__recipient_email
    
    def get_sender_email(self):
        return self.__sender_email

    def get_sender_name(self):
        return self.__sender_name

    def get_add_to_cart(self):
        return self.__add_to_cart

    def get_success_message(self):
        return self.__success_message

    def get_shopping_cart(self):
        return self.__shopping_cart

    def get_quantity(self):
        return self.__quantity

    def get_update_cart(self):
        return self.__update_cart

    def get_recipient_email_error(self):
        return self.__recipient_email_error