import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from Utilities.configReader import ReadConfig
import os
from datetime import datetime
import allure

@pytest.fixture()
def setup_and_teardown(request):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())

    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.ID, "Email").send_keys(ReadConfig.get_email())
    driver.find_element(By.ID, "Password").send_keys(ReadConfig.get_password())
    driver.find_element(By.CSS_SELECTOR, "input.button-1.login-button").click()

    request.cls.driver = driver

    yield

    driver.quit()

# @pytest.fixture()
# def setup_and_teardown(request):

#     options=webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1920,1080")

#     driver=webdriver.Chrome(options=options)
#     driver.maximize_window()
#     driver.get(ReadConfig.get_base_url())

#     request.cls.driver = driver

#     yield

#     driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome=yield

    report=outcome.get_result()

    if report.when=="call" and report.failed:

        driver=getattr(item.cls, "driver", None)

        if driver:

            # Project root path
            project_root=os.path.dirname(os.path.abspath(__file__))

            screenshot_dir=os.path.join(project_root,"Screenshots")

            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            screenshot_path = os.path.join(screenshot_dir,f"{item.name}_{timestamp}.png")

            # Save screenshot
            driver.save_screenshot(screenshot_path)

            # Allure attachment
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{item.name}_Failure_Screenshot",
                attachment_type=allure.attachment_type.PNG
            )