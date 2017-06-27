from selenium.webdriver.common.by import By
from traceback import print_stack
import logging
from utilities.custom_logger import custom_logger
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
import os

class SeleniumDriver():

    log = custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def take_screenshot(self, result_message):
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "..\screenshots\\"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "partial link":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "tag":
            return By.TAG_NAME
        else:
            self.log.info("Locator type {0}, is not supported/recognized".format(locator_type))

    def get_element(self, locator, locator_type="id"):
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Success - Element found with locator-type: {0}, and locator: {1}".format(locator_type, locator))
            return element
        except:
            self.log.info("Failure - Element not found with locator-type: {0}, and locator: {1}".format(locator_type, locator))

    def get_element_list(self, locator, locator_type="id"):
        try:
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)

            self.log.info ("Found a list of {0} elements".format(str(elements_list)))
            return elements
        except:
            self.log.info ("Found a list of {0} elements".format(locator_type, locator))

    def send_keys_to_element(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            element.send_keys(data)
            self.log.info ("Success - Sent data to element with locator-type: {0}, and locator: {1}".format(locator_type, locator))
        except:
            self.log.info ("Failure - Cannot send data to element with locator-type: {0}, and locator: {1}".format(locator_type, locator))
            # print_stack()

    def click_on_element(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info ("Success - Clicked on element with locator-type: {0}, and locator: {1}".format(locator_type, locator))
        except:
            self.log.info ("Failure - Cannot click on element with locator-type: {0}, and locator: {1}".format(locator_type, locator))
            # print_stack()

    def is_element_present(self, locator, locator_type="id"):
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                self.log.info ("Element with locator-type: {0}, and locator: {1} is not none".format(locator_type, locator))
                return True
            else:
                self.log.info ("Element with locator-type: {0}, and locator: {1} is none".format(locator_type, locator))
                return False
        except:
            self.log.info ("Element with locator-type: {0}, and locator: {1} is none".format(locator_type, locator))
            return False

    def element_presence_check(self, locator, locator_type="id"):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            if len(element) > 0:
                self.log.info ("Element present with locator: " + locator +
                              " locatorType: " + str(by_type))
                return True
            else:
                self.log.info ("Element not present with locator: " + locator +
                              " locatorType: " + str(by_type))
                return False
        except:
            self.log.info ("Element not found")
            return False

    def is_element_displayed(self, locator, locator_type="id"):
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            if element.is_displayed() == True:
                self.log.info ("Success - Element displayed with locator: " + locator +
                              " locatorType: " + str(by_type))
                return True
            else:
                self.log.info ("Failure - Element not displayed with locator: " + locator +
                              " locatorType: " + str(by_type))
                print_stack()
                return False
        except:
            self.log.info ("Exception occured - Element not displayed with locator: " + locator +
                          " locatorType: " + str(by_type))
            print_stack()
            return False

    def hover_over(self , locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            self.log.info("Success - Hovered over Element with locator-type: {0}, and locator: {1}".format(locator_type, locator))
        except:
            self.log.error("Failure - Cannot Hover over Element with locator-type: {0}, and locator: {1}".format(locator_type, locator))

    def wait_for_element(self, locator, locator_type="id", timeout=30, poll_frequency=0.5):
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency,
            ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
            return element
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()

    def scroll_web_page(self, pixels, direction="down"):
        scroll_up = "window.scrollBy(0, -{0});".format(pixels)
        scroll_down = "window.scrollBy(0, {0});".format(pixels)

        if direction == "up":
            # Scroll Up -
            self.driver.execute_script(scroll_up)

        if direction == "down":
            # Scroll Down +
            self.driver.execute_script(scroll_down)

    def scroll_into_view(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.location_once_scrolled_into_view
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.scroll_web_page(200, direction="up")
            self.log.info("Success - scrolled to element with locator-type: {0}, and locator: {1}".format(locator_type, locator))
        except:
            self.log.info("Failure - could not scroll to element with locator-type: {0}, and locator: {1}".format(locator_type, locator))

    def drop_down_btn(self, locator, locator_type="id", visible_text=None, index=None, value=None):
        try:
            element = self.get_element(locator, locator_type)
            sel = Select(element)
            if visible_text is not None:
                sel.select_by_visible_text(visible_text)
                self.log.info("Success - selected element by visible text")
            elif index is not None:
                sel.select_by_index(index)
                self.log.info("Success - selected element by index")
            else:
                sel.select_by_value(value)
                self.log.info("Success - selected element by value")
        except:
            self.log.info("Failure - Could not select element with locator-type: {0}, and locator: {1}".format(locator_type, locator))

    def switch_to_frame(self, frame_id=None, frame_name=None, frame_number=0):
        try:
            if frame_id is not None:
                self.driver.switch_to.frame(frame_id)
                self.log.info ("Success - switched frame by ID")
            elif frame_name is not None:
                self.driver.switch_to.frame(frame_name)
                self.log.info ("Success - switched frame by name")
            else:
                self.driver.switch_to.frame(frame_number)
                self.log.info ("Success - switched frame by number")
        except:
            self.log.info ("Failure - Could not switch a frame")
            print_stack()
