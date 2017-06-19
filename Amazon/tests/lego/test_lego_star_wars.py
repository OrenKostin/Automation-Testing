from pages.lego.lego_star_wars_page import LegoStarWars
from utilities.assert_status import AssertStatus
import unittest, pytest
import time
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data

@pytest.mark.usefixtures("one_time_setup")
@ddt
class TestLegoStarWars(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, one_time_setup):
        self.lc = LegoStarWars(self.driver)
        self.ts = AssertStatus(self.driver)

    @data(*get_csv_data("C:\\Users\okostin\Documents\Python\Selenium\Frameworks\Amazon\\lego_star_wars.csv"))
    @unpack
    def test_lego_star_wars(self, auto_complete, product_name, address, cc_name, cc_number, cc_month, cc_year):
        self.lc.search_product(auto_complete)
        self.lc.auto_complete_product()
        self.lc.scroll_to_element()
        self.lc.click_lego_creator()
        self.lc.click_lego_product(product_name)
        # self.lc.click_see_all_buying_options()
        self.lc.click_add_to_cart_btn()
        self.lc.click_proceed_to_checkout_btn()

        self.lc.enter_pick_up_address(address)
        self.lc.click_pick_up_address_search_btn()
        self.lc.click_ship_to_this_address()
        self.lc.click_shipping_option()
        self.lc.enter_credit_card_info(cc_name, cc_number, cc_month, cc_year)
        self.lc.add_card()

        result = self.lc.verify_error_message()
        self.ts.mark_final("test_lego_star_wars", result, "Error message displayed")

    def tearDown(self):
        self.lc.home_page()
