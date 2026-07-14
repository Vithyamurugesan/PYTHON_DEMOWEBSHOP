import pytest
from Actions.NewsletterAction import NewsletterAction
from Utilities.CsvReader import CsvReader

NEWSLETTER_CSV = "TestData/NewsletterData.csv"


@pytest.mark.usefixtures("setup_and_teardown")
class TestNewsletter:

    # @NewsletterSubscription
    @pytest.mark.parametrize(
        "row",
        CsvReader.get_newsletter_data(NEWSLETTER_CSV)
    )
    def test_newsletter_subscription(self, row):

        newsletter = NewsletterAction(self.driver)

        newsletter.enter_newsletter_email(row["email"])
        newsletter.click_subscribe_button()

        expected = (
            "Thank you for signing up! "
            "A verification email has been sent. "
            "We appreciate your interest."
        )

        actual = newsletter.get_subscription_message()

        assert actual == expected, \
            "Newsletter subscription success message is incorrect"