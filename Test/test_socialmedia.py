import pytest
from Actions.SocialMediaAction import SocialMediaAction

@pytest.mark.Vetri
@pytest.mark.usefixtures("setup_and_teardown")
class TestSocialMedia:

    @pytest.mark.parametrize("media", ["Facebook", "Twitter", "YouTube"])
    def test_social_media_link_redirects(self, media):

        social = SocialMediaAction(self.driver)

        assert social.click_social_media_link(media), \
            f"{media} link did not redirect to the correct page"