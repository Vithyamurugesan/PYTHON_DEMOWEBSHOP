from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import BaseAction
from Pages.SearchPage import SearchPage

class SearchAction(BaseAction):

    def __init__(self,driver):
        super().__init__(driver)
        self.searchPage=SearchPage()

    def searchProduct(self,keyword):
        self.send_keys(self.searchPage.get_search_box(),keyword)
    
    def clickSearch(self):
        self.click(self.searchPage.get_search_button())
    
    def verifySearchRedirect(self):
        return "search" in self.get_url()
    
    def is_warning_displayed(self):
        return self.wait_for_visible(self.search_page.get_warning_message()).is_displayed()

    def verify_no_product_message(self):
        return self.wait_for_visible(self.search_page.get_no_result_message()).is_displayed()

    