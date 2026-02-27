import pytest
from locators import MyLocators
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def ml():
    ml = MyLocators()
    return ml
