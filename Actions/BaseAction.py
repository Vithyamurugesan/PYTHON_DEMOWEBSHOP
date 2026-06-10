from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BaseActions:

    def __init__(self, driver):
        self.driver=driver
        self.wait=WebDriverWait(driver, 15)
        self.actions=ActionChains(driver)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            self.js_click(locator)

    def js_click(self, locator):
        self.driver.execute_script("arguments[0].click();", self.find(locator))

    def action_click(self, locator):
        self.actions.click(self.find(locator)).perform()

    def send_keys(self, locator, text):
        element=self.find(locator)
        element.send_keys(text)

    def clear(self, locator):
        self.find(locator).clear()

    def get_text(self, locator):
        return self.find(locator).text

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def open_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def take_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)