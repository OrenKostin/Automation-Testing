from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        if self.browser == "edge":
            driver = webdriver.Edge()
        elif self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        # driver.delete_all_cookies()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("https://www.amazon.ca/")
        return driver
