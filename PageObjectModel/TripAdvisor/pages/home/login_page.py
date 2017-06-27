from base.selenium_driver_1 import SeleniumDriver
from utilities.custom_logger import custom_logger
import logging
import time

class LoginPage(SeleniumDriver):

    log = custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _user_icon = "//div[@id='taplc_global_nav_action_profile_0']//span[@class='ui_icon friend']" #by.xpath
    _iframe_login = "overlayRegFrame" #by.id
    _email_field = "regSignIn.email" #by.id
    _password_field = "regSignIn.password" #by.id
    _log_in_btn = "//div[@id='regSignIn']//div[text()='Log In']" #by.xpath
    _user_name = "//div[@id='taplc_global_nav_action_profile_0']//span[text()='oren.test3@']" #by.xpath
    # _user_name = "//div[@id='taplc_global_nav_action_profile_0']//span[2]"
    _sign_out_btn = "//div[@id='taplc_global_nav_menus_0']//a[text()='Sign out']"
    _JOIN_btn = "//div[@id='taplc_global_nav_action_profile_0']//a[text()='JOIN']"
    _captcha ="//span[@id='recaptcha-anchor']/div[@class='recaptcha-checkbox-checkmark']"
    # _captcha = 'recaptcha-anchor' #by.id
    _error_message = 'regErrors'


    def click_profile_icon(self):
        self.click_on_element(self._user_icon, "xpath")

    def switch_to_login_frame(self):
        self.switch_to_frame(frame_id=self._iframe_login)

    def clear_captcha(self):
        self.click_on_element(self._captcha)

    def enter_email(self, email):
        self.send_keys_to_element(email, self._email_field)

    def enter_password(self, password):
        self.send_keys_to_element(password, self._password_field)

    def click_log_in_btn(self):
        self.click_on_element(self._log_in_btn, "xpath")

    def click_user_name(self):
        self.click_on_element(self._user_name, "xpath")

    def click_sign_out_btn(self):
        self.click_on_element(self._sign_out_btn, "xpath")

    def login(self, email="", password=""):
        self.click_profile_icon()        
        self.switch_to_login_frame()
        self.enter_email(email)
        self.enter_password(password)
        self.click_log_in_btn()
        self.driver.switch_to.default_content()

    def invalid_login(self, email="", password=""):
        self.click_profile_icon()
        self.switch_to_login_frame()
        self.enter_email(email)
        self.enter_password(password)
        self.click_log_in_btn()


    def verify_logout_successful(self):
        result = self.is_element_present(self._JOIN_btn, "xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_present(self._error_message)
        return result

    def verify_login_successful(self):
        self.wait_for_element(self._user_name, "xpath")
        result = self.is_element_present(self._user_name, "xpath")
        return result
