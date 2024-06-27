import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get('http://127.0.0.1:8000/')
    driver.maximize_window()
    yield driver

    driver.quit()
