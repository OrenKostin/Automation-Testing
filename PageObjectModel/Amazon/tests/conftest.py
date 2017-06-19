from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import Login
import pytest
import time

@pytest.fixture(scope="class")
def one_time_setup(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()
    lp = Login(driver)
    lp.login("oren_test3@gmail.com", "123456")
    time.sleep(2)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
