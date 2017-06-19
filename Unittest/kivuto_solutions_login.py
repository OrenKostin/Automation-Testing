import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class Kivuto(unittest.TestCase):

    # invoke firefox browser and maximize window
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    # get kivuto url
    def setUp(self):
        driver = self.driver
        driver.get("http://kivuto.com//")
        driver.implicitly_wait(2)

    # navigate to Texidium Brand and try to log in
    def test_texidium_brand(self):
        driver = self.driver

        # find the main page handle
        parent_handle = driver.current_window_handle

        # find Brands element in upper menu bar
        brand_element = driver.find_element_by_xpath(
        "//ul[@id='menu-header-navigation-1']//span[text()='Brands']")

        # navigate to Brands element
        actions = ActionChains(driver)
        actions.move_to_element(brand_element).perform()
        time.sleep(2)

        # find Texidium brand and click on it
        texidium_brand = driver.find_element(
        By.XPATH, "//ul[@id='menu-header-navigation-1']//li[contains(@class,'2611')]")
        texidium_brand.click()
        time.sleep(3)

        # find all opened pages
        all_handles = driver.window_handles

        # find the Texidium page and switch to it
        for handle in all_handles:
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                break

        # find Texidium page handle
        texidium_handle = driver.current_window_handle

        # find sign in button and click on it
        sign_in_btn = driver.find_element(By.XPATH, "//div[@id='newHeaderInner']//a[text()='Sign in']")
        sign_in_btn.click()
        time.sleep(2)

        # find all opened pages
        all_handles = driver.window_handles

        # find Texidium sign in page and switch to it
        for handle in all_handles:
            if handle not in parent_handle and handle not in texidium_handle:
                driver.switch_to.window(handle)
                break
        time.sleep(5)

        # find email field and fill it
        wait = WebDriverWait(driver, 30, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        email_field = wait.until(EC.presence_of_element_located((By.ID,
                                                         "username")))
        
        email_field.send_keys("KivutoIsAwesome@gmail.com")
        time.sleep(2)

        # find password field and fill it
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("1234")
        time.sleep(2)

        # find confirmation button and click on it
        confirmation_btn = driver.find_element(By.XPATH, "//button[text()='Sign In']")
        confirmation_btn.click()
        time.sleep(5)

        # find error message element
        error_message = driver.find_element(
        By.XPATH, "//div[contains(@class,'alert-danger ng-binding')]")

        # assert that an error message is displayed
        self.assertTrue(error_message.is_displayed())

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
