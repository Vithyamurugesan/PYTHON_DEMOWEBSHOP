from Actions.GiftCardAction import GiftCardAction
from Utilities.excelReader import get_data
import pytest


class TestGiftCard:

    def test_valid_gift_card_purchase(
            self,
            setup_and_teardown):

        gift = GiftCardAction(self.driver)

        data = get_data(
            "TestData/TestData.xlsx",
            "GiftCard"
        )

        row = data[0]

        gift.click_gift_cards_menu()

        gift.select_virtual_gift_card()

        gift.enter_recipient_name(row[0])

        gift.enter_recipient_email(row[1])

        gift.enter_sender_name(row[2])

        gift.click_add_to_cart()

        assert (
            "The product has been added"
            in
            gift.get_success_message()
        )

    @pytest.mark.parametrize(
        "data",
        get_data(
            "TestData/TestData.xlsx",
            "InvalidRecipientEmail"
        )
    )
    def test_invalid_recipient_email(
            self,
            setup_and_teardown,
            data):

        gift = GiftCardAction(self.driver)

        gift.click_gift_cards_menu()

        gift.select_virtual_gift_card()

        gift.enter_recipient_name(data[0])

        gift.enter_recipient_email(data[1])

        gift.enter_sender_name(data[2])

        gift.click_add_to_cart()

        assert (
            gift.get_recipient_email_error()
            ==
            data[3]
        )

    @pytest.mark.parametrize(
        "data",
        get_data(
            "TestData/TestData.xlsx",
            "QuantityUpdate"
        )
    )
    def test_quantity_update(
            self,
            setup_and_teardown,
            data):

        gift = GiftCardAction(self.driver)

        gift.click_gift_cards_menu()

        gift.select_virtual_gift_card()

        gift.enter_recipient_name(data[0])

        gift.enter_recipient_email(data[1])

        gift.enter_sender_name(data[2])

        gift.click_add_to_cart()

        gift.click_shopping_cart()

        gift.update_quantity(
            str(data[3])
        )

        gift.click_update_cart()

        assert (
            gift.get_quantity_value()
            ==
            str(data[3])
        )