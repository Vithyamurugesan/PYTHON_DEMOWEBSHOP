from selenium.webdriver.common.by import By


class SocialMediaPage:

    def __init__(self):
        self.__facebook_link=(By.XPATH, "//a[contains(@href,'facebook')]")
        self.__twitter_link=(By.XPATH, "//a[contains(@href,'twitter') or contains(@href,'x.com')]")
        self.__youtube_link=(By.XPATH, "//a[contains(@href,'youtube')]")

    def get_link(self, media):

        media=media.lower()
        
        if media=="facebook":
            return self.__facebook_link
        
        elif media=="twitter":
            return self.__twitter_link
        
        elif media=="youtube":
            return self.__youtube_link
        
        else:
            raise ValueError(f"Unknown social media link : {media}")