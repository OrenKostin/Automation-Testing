from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger
import logging

class LegoStarWars(SeleniumDriver):

    log = custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _search_bar = "twotabsearchtextbox" #by.id
    _auto_complete = 'issDiv3' #by.id
    _lego_type = "//div[@id='leftNavContainer']//span[text()='Star Wars']" #by.xpath
    _lego_product = "//ul[@id='s-results-list-atf']//h2[contains(text(),'{}')]" #by.xpath
    _buying_options = 'buybox-see-all-buying-choices-announce' #by.id
    _add_to_cart = "add-to-cart-button" #by.id
    _proceed_to_checkout = 'hlb-ptc-btn-native' #by.id

    _pick_up_address = "address" #by.id
    _pick_up_address_search_btn = "Search" #by.name
    _ship_to_this_address_btn = "(//div[@id='wrapper']//input[@name='shipToThisAddress'])[1]" #by.xpath
    _choose_shipping_option = "(//form[@id='shippingOptionFormId']//input[@class='a-button-text' and contains (@type,'submit')])[1]"

    _cc_name = "ccName" #by.id
    _cc_number = "addCreditCardNumber" #by.id
    _click_exp_month= "(//form[@id='form-add-credit-card']//button)[1]"
    _choose_exp_month = "//ul[@id='1_dropdown_combobox']//a[text()='{}']"
    _click_exp_year = "(//form[@id='form-add-credit-card']//button)[2]"
    _choose_exp_year = "//ul[@id='2_dropdown_combobox']//a[text()='{}']"
    _add_cc = "ccAddCard" #by.id

    _error_message = "//div[@id='newCCErrors']//h4[text()='Sorry, there was a problem']" #by.xpath



    def search_product(self, data):
        self.send_keys_to_element(data, self._search_bar)

    def auto_complete_product(self):
        self.click_on_element(self._auto_complete)

    def scroll_to_element(self):
        self.scroll_into_view(self._lego_type, "xpath")

    def click_lego_creator(self):
        self.click_on_element(self._lego_type, "xpath")

    def click_lego_product(self, product_name):
        self.click_on_element(self._lego_product.format(product_name), "xpath")

    # def click_see_all_buying_options(self):
    #     self.click_on_element(self._buying_options)

    def click_add_to_cart_btn(self):
        self.click_on_element(self._add_to_cart)

    def click_proceed_to_checkout_btn(self):
        self.click_on_element(self._proceed_to_checkout)

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
