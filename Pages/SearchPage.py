from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class SearchPage:

    def __init__(self):
        self.__searchBox=(By.ID,"small-searchterms")
        self.__searchButton=(By.XPATH,"//input[@value='Search']")
        self.__searchResult=(By.CLASS_NAME,"product-grid")
        self.__noResultMessage=(By.XPATH,"//*[contains(text(),'No products were found')]")
        self.__warningMessage=(By.CSS_SELECTOR,".warning")

    def get_search_box(self):
        return self._search_box

    def get_search_button(self):
        return self._search_button

    def get_search_result(self):
        return self._search_result

    def get_no_result_message(self):
        return self._no_result_message

    def get_warning_message(self):
        return self._warning_message