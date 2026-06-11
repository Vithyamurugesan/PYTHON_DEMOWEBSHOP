import pytest
from selenium import webdriver
from Configuration.configReader import ReadConfig
import os
from datetime import datetime
import allure


@pytest.fixture()
def setup_and_teardown(request):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())

    request.cls.driver = driver

    yield

    driver.quit()


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