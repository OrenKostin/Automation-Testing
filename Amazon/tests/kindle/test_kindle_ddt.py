from pages.kindle.kindle_page import KindleDevices
from utilities.assert_status import AssertStatus
import unittest, pytest
import time
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("one_time_setup")
@ddt
class TestKindle(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_setup):
        self.kd = KindleDevices(self.driver)
        self.ts = AssertStatus(self.driver)

    @data(("ki", 'Kindle Paperwhite, 6" High-Resolution Display (300 ppi) with Built-in Light, Wi-Fi',
            "halifax", "oren", "1234", "08", "2018"))
    @unpack
    def test_kindle(self, auto_complete, product_name, address, cc_name, cc_number, cc_exp_month, cc_exp_year):
        self.kd.search_bar_auto_complete(auto_complete)
        self.kd.click_auto_complete()
        self.kd.click_kindle_product(product_name)
        self.kd.click_add_to_cart_btn()
        # self.kd.close_pop_up()
        self.kd.confirm_pop_up()
        self.kd.click_checkout_btn()
        self.kd.enter_pick_up_address(address)
        self.kd.click_pick_up_address_search_btn()
        self.kd.click_ship_to_this_address()
        self.kd.click_shipping_option()
        self.kd.enter_credit_card_info(cc_name, cc_number, cc_exp_month, cc_exp_year)
        self.kd.add_card()

        result = self.kd.verify_error_message()
        self.ts.mark_final("test_kindle", result, "Error message not displayed")

    def tearDown(self):
        self.kd.home_page()
