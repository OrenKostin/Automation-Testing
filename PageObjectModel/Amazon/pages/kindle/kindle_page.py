from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class KindleDevices(SeleniumDriver):

    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)

    # locators
    _search_bar = "twotabsearchtextbox" #by.id
    _kindle_auto_complete = "issDiv0" #by.id
    _all_kindle_products = "//ul[@id='s-results-list-atf']//h2"
    _kindle_product = "//ul[@id='s-results-list-atf']//h2[contains(text(),'{}')]" #by.xpath
    _add_product_to_cart = "add-to-cart-button" #by.id
    _close_pop_up_window = "//div[@id='a-popover-4']//button" #by.xpath
    _confirm_pop_up_window = "intl_pop_addToOrder" #by.id
    _proceed_to_checkout_btn = "//div[@id='hlb-next-steps']//a[@class='hucSprite s_checkout hlb-checkout-button']"
    _pick_up_address = "address" #by.id
    _pick_up_address_search_btn = "Search" #by.name
    _ship_to_this_address_btn = "(//div[@id='wrapper']//input[@name='shipToThisAddress'])[1]" #by.xpath
    _choose_shipping_option = "(//form[@id='shippingOptionFormId']//input[@class='a-button-text' and contains (@type,'submit')])[1]"
    _cc_name = "ccName" #by.id
    _cc_number = "addCreditCardNumber" #by.id

    _click_exp_month= "(//form[@id='form-add-credit-card']//button)[1]"
    # _click_exp_month = "//form[@id='form-add-credit-card']//span[@class='a-button a-button-dropdown']//button[@class='a-button-text a-declarative']"
    # _choose_exp_month = "//form[@id='form-add-credit-card']//select[@id='ccMonth']//option[@value='3']"
    _choose_exp_month = "//ul[@id='1_dropdown_combobox']//a[text()='{}']"
    _click_exp_year = "(//form[@id='form-add-credit-card']//button)[2]"
    _choose_exp_year = "//ul[@id='2_dropdown_combobox']//a[text()='{}']"
    # _exp_month = "//form[@id='form-add-credit-card']//select[@id='ccMonth']" #by.xpath
    # _exp_year = "//form[@id='form-add-credit-card']//select[@id='ccYear']" #by.xpath
    _add_cc = "ccAddCard" #by.id
    # _error_message = 'newCCErrors' #by.id
    _error_message = "//div[@id='newCCErrors']//h4[text()='Sorry, there was a problem']" #by.xpath

    def search_bar_auto_complete(self, data):
        self.send_keys_to_element(data, self._search_bar)

    def click_auto_complete(self):
        self.click_on_element(self._kindle_auto_complete)

    def click_kindle_product(self, product_name):
        self.click_on_element(self._kindle_product.format(product_name), "xpath")

    def click_add_to_cart_btn(self):
        self.click_on_element(self._add_product_to_cart)

    def close_pop_up(self):
        self.click_on_element(self._close_pop_up_window, "xpath")
        self.log.info("closed pop up")

    def confirm_pop_up(self):
        self.click_on_element(self._confirm_pop_up_window)

    def click_checkout_btn(self):
        self.click_on_element(self._proceed_to_checkout_btn, "xpath")

    def enter_pick_up_address(self, data):
        self.send_keys_to_element(data, self._pick_up_address)

    def click_pick_up_address_search_btn(self):
        self.click_on_element(self._pick_up_address_search_btn, "name")

    def click_ship_to_this_address(self):
        self.click_on_element(self._ship_to_this_address_btn, "xpath")

    def click_shipping_option(self):
        self.click_on_element(self._choose_shipping_option, "xpath")

    def enter_credit_card_name(self, cc_name):
        self.send_keys_to_element(cc_name, self._cc_name)

    def enter_credit_card_number(self, cc_number):
        self.send_keys_to_element(cc_number, self._cc_number)

    def click_cc_exp_month(self):
        self.click_on_element(self._click_exp_month, "xpath")

    def choose_cc_exp_month(self, exp_month):
        self.click_on_element(self._choose_exp_month.format(exp_month), "xpath")

    def click_cc_exp_year(self):
        self.click_on_element(self._click_exp_year, "xpath")

    def choose_cc_exp_year(self, exp_year):
        self.click_on_element(self._choose_exp_year.format(exp_year), "xpath")

    def enter_credit_card_info(self, cc_name, cc_number, exp_month, exp_year):
        self.enter_credit_card_name(cc_name)
        self.enter_credit_card_number(cc_number)
        self.click_cc_exp_month()
        self.choose_cc_exp_month(exp_month)
        self.click_cc_exp_year()
        self.choose_cc_exp_year(exp_year)

    def add_card(self):
        self.click_on_element(self._add_cc)

    def verify_error_message(self):
        result = self.is_element_displayed(self._error_message, "xpath")
        return result

    def home_page(self):
        self.driver.get("https://www.amazon.ca/")
