from selenium import webdriver
import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
import time

@pytest.fixture(scope='class')
def one_time_setup(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()
    lp = LoginPage(driver)
    lp.login("oren.test3@gmail.com", "dragon")


    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
