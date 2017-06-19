from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
from utilities.custom_logger import custom_logger
import time

class Login(SeleniumDriver):

    log = custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _sign_in_link = "nav-link-yourAccount" #by.id
    _email = "ap_email" #by.id
    _password = "ap_password" #by.id
    _sign_in_btn = "signInSubmit" #by.id
    _user_icon = "//a[@id='nav-link-yourAccount']/span[text()='Hello, oren']" #by.xpath
    _error_message = "//div[@id='auth-error-message-box']//div[@class='a-box-inner a-alert-container']"
    _log_out_btn = "//a[@id='nav-item-signout']//span[text()='Not oren? Sign Out']"
    _sign_in_text = "//div[@id='a-page']//h1[contains(text(),'Sign in')]"


    def click_sign_in_link(self):
        self.click_on_element(self._sign_in_link)

    def enter_email(self, email):
        self.send_keys_to_element(email, self._email)

    def enter_password(self, password):
        self.send_keys_to_element(password, self._password)

    def click_sign_in_btn(self):
        self.click_on_element(self._sign_in_btn)

    def hover_over_sign_in_link(self):
        self.hover_over(self._sign_in_link, locator_type="id")

    def click_log_out_btn(self):
        self.click_on_element(self._log_out_btn, "xpath")

    def hover_over_sign_in_link_and_click(self):
        self.hover_over_and_click(self._log_out_btn, "xpath")

    def login(self, email, password):
        self.click_sign_in_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in_btn()

    def log_out(self):
        self.hover_over_sign_in_link()
        self.click_log_out_btn()

    def verify_login_successful(self):
        result = self.is_element_present(self._user_icon, "xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_present(self._error_message, "xpath")
        return result

    def verify_login_failed_global(self):
        title = self.get_title()
        if "Amazon Sign In" in title:
            return True
        else:
            return False

    # def verify_log_out_successful(self):
    #     result = self.is_element_present(self._sign_in_text, "xpath")
    #     return result

    def verify_log_out_successful(self):
        title = self.get_title()
        if "Amazon Sign In" in title:
            return True
        else:
            return False
