from Pages.GiftCardPage import GiftCardPage
from Actions.BaseAction import BaseAction


class GiftCardAction(BaseAction):

    def __init__(self, driver):

        super().__init__(driver)

        self.page = GiftCardPage()

    def click_gift_cards_menu(self):

        menu = self.find(
            self.page.get_gift_cards_menu()
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            menu
        )

        self.driver.execute_script(
            "arguments[0].click();",
            menu
        )

    def select_virtual_gift_card(self):

        card = self.find(
            self.page.get_virtual_gift_card()
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            card
        )

        self.driver.execute_script(
            "arguments[0].click();",
            card
        )

    def enter_recipient_name(self, name):

        element = self.find(
            self.page.get_recipient_name()
        )

        element.clear()

        element.send_keys(name)

    def enter_recipient_email(self, email):

        element = self.find(
            self.page.get_recipient_email()
        )

        element.clear()

        element.send_keys(email)

    def enter_sender_name(self, sender):

        element = self.find(
            self.page.get_sender_name()
        )

        element.clear()

        element.send_keys(sender)

    def click_add_to_cart(self):

        button = self.find(
            self.page.get_add_to_cart()
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def click_shopping_cart(self):

        cart = self.find(
            self.page.get_shopping_cart()
        )

        self.driver.execute_script(
            "arguments[0].click();",
            cart
        )

    def update_quantity(self, quantity):

        qty = self.find(
            self.page.get_quantity()
        )

        qty.clear()

        qty.send_keys(str(quantity))

    def click_update_cart(self):

        button = self.find(
            self.page.get_update_cart()
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def get_quantity_value(self):

        return self.find(
            self.page.get_quantity()
        ).get_attribute("value")