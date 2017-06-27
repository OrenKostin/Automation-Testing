from selenium import webdriver
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger
import logging

class AssertStatus(SeleniumDriver):

    log = custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result == True:
                    self.result_list.append("PASS")
                    self.log.info("VERIFICATION SUCCESSFUL")
                else:
                    self.result_list.append("FAIL")
                    self.log.error("VERIFICATION FAILED - " + result_message)
                    self.take_screenshot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error("VERIFICATION FAILED - " + result_message)
                self.take_screenshot(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("EXCEPTION OCCURED - " + result_message)
            self.take_screenshot(result_message)

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        self.set_result(result, result_message)

        if "FAIL" in self.result_list:
            self.log.error(test_name + " :: TEST FAILED :: " + result_message)
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(test_name + " :: TEST PASSED")
            self.result_list.clear()
            assert True == True
