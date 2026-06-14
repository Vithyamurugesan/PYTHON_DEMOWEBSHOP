from selenium.webdriver.common.by import By

class DownloadPage:

    def __init__(self):
        self.__my_account_link = (By.XPATH,"//div[@class='column my-account']/descendant::a[@class='account']")

        self.__download_product_link = (By.XPATH,"(//div[@class='listbox']/descendant::a[@class='inactive'])[3]")

        self.__product_count = (By.XPATH,"//table[@class='data-table']//tbody//tr")

        self.__product_name = (By.XPATH,"//table[@class='data-table']//tbody//tr/td[3]")

        self.__internal_error_message = (By.XPATH,"//p[contains(text(),\"We're sorry, an internal error occurred.\")]")

    def get_internal_error_message(self):
        return self.__internal_error_message
    def get_my_account_link(self):
        return self.__my_account_link

    def get_download_product_link(self):
        return self.__download_product_link

    def get_product_count(self):
        return self.__product_count

    def get_product_name(self):
        return self.__product_name