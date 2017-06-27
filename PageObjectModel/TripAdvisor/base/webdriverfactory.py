from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        if self.browser == "edge":
            driver = webdriver.Edge()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "iexplorer":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Firefox()

        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get("https://www.tripadvisor.ca/")

        return driver
