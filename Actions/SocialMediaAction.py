from Actions.BaseAction import BaseAction
from Pages.SocialMediaLink import SocialMediaPage
from selenium.webdriver.support import expected_conditions as EC


class SocialMediaAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.social_media_page = SocialMediaPage()

    def click_social_media_link(self, media):

        parent_window = self.driver.current_window_handle

        self.click(self.social_media_page.get_link(media))

        self.wait.until(EC.number_of_windows_to_be(2))

        for window in self.driver.window_handles:
            if window != parent_window:
                self.driver.switch_to.window(window)
                break

        self.wait.until(EC.url_contains("http"))

        url = self.driver.current_url.lower()

        self.driver.close()

        self.driver.switch_to.window(parent_window)

        if media.lower() == "facebook":
            return "facebook.com" in url

        elif media.lower() == "twitter":
            return "twitter.com" in url or "x.com" in url

        elif media.lower() == "youtube":
            return "youtube.com" in url

        return False