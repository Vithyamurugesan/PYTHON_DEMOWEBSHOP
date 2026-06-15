from Pages.GiftCardPage import GiftCardPage
from Actions.BaseAction import BaseAction


class GiftCardAction(BaseAction):

    def __init__(self, driver):

        super().__init__(driver)

        self.giftCardPage = GiftCardPage()

    def click_gift_cards_menu(self):

        self.click(
            self.giftCardPage.get_gift_cards_menu()
        )

    def select_virtual_gift_card(self):

        self.click(
            self.giftCardPage.get_virtual_gift_card()
        )

    def enter_recipient_name(self, name):

        self.send_keys(
            self.giftCardPage.get_recipient_name(),
            name
        )

    def enter_recipient_email(self, email):

        self.send_keys(
            self.giftCardPage.get_recipient_email(),
            email
        )

    def enter_sender_name(self, name):

        self.send_keys(
            self.giftCardPage.get_sender_name(),
            name
        )

    def click_add_to_cart(self):

        button = self.find(
            self.giftCardPage.get_add_to_cart()
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def get_success_message(self):

        return self.get_text(
            self.giftCardPage.get_success_message()
        )

    def click_shopping_cart(self):

        self.click(
            self.giftCardPage.get_shopping_cart()
        )

    def update_quantity(self, qty):

        element = self.find(
            self.giftCardPage.get_quantity()
        )

        element.clear()

        element.send_keys(qty)

    def click_update_cart(self):

        self.click(
            self.giftCardPage.get_update_cart()
        )

    def get_quantity_value(self):

        return self.get_attribute(
            self.giftCardPage.get_quantity(),
            "value"
        )

    def get_recipient_email_error(self):

        return self.get_text(
            self.giftCardPage.get_recipient_email_error()
        )