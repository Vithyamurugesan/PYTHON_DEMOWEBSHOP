from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Actions.BaseAction import BaseAction
from Pages.SearchPage import SearchPage
from selenium.webdriver.common.by import By

class SearchAction(BaseAction):

    def __init__(self,driver):
        super().__init__(driver)
        self.search_page=SearchPage()

    def searchProduct(self,keyword):
        self.send_keys(self.search_page .get_search_box(),keyword)
    
    def clickSearch(self):
        self.click(self.search_page .get_search_button())
    
    def verifySearchRedirect(self):
        print(self.get_url())
        return "search" in self.get_url()
    
    def is_warning_displayed(self):
        return self.wait_for_visible(self.search_page.get_warning_message()).is_displayed()

    def verify_no_product_message(self):
        return self.wait_for_visible(self.search_page.get_no_result_message()).is_displayed()

    def verifyResultsContainKeyword(self, keyword):

        titles=self.driver.find_elements(By.CSS_SELECTOR,".product-title")

        for element in titles:
            if keyword.lower() in element.text.lower():
                return True

        return False


    def isWarningDisplayed(self):
        return self.wait_for_visible(self.searchPage.get_warning_message()).is_displayed()
    
    def is_alert_present(self):
        try:
            self.wait.until(EC.alert_is_present())
            return True
        except:
            return False

    def accept_alert(self):
        self.driver.switch_to.alert.accept()