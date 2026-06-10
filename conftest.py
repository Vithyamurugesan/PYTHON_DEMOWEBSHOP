import pytest
from selenium import webdriver
from Configuration.configReader import ReadConfig

@pytest.fixture()
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    request.cls.driver = driver
    yield
    driver.quit()