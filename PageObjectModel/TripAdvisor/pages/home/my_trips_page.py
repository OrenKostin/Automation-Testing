from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger
import logging

class MyTrips(SeleniumDriver):

    log = custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _search_bar = "//div[@id='taplc_trip_search_home_default_0']//input[@placeholder='City or hotel name']" #by.xpath
    _start_date_btn = "(//div[@id='taplc_trip_search_home_default_0']//span[@class='picker-inner'])[1]" #by.xpath
    _next_month_btn = "//div[@class='dsdc-next ui_icon single-chevron-right-circle']" #by.xpath
    _start_month_all_days = "(//span[@class='dsdc-month'])[1]//span[@class='dsdc-cell dsdc-day']" #by.xpath
    _end_month_all_days = "(//span[@class='dsdc-month'])[2]//span[@class='dsdc-cell dsdc-day']" #by.xpath
    _submit_hotels = "SUBMIT_HOTELS" #by.id
    _hotel_class_rating = "//div[@id='HOTELS_LEFT_FILTERS']//div[contains(text(),'Hotel class')]" #by.xpath
    _5_stars_rating = "//div[@id='jfy_filter_bar_hotel_class']//label[@for='jfy_filter_s_10']" #by.xpath
    _all_heart_icons = "//div[@id='taplc_hsx_hd_hotels_list_0']//span[contains(@class,'heart')]" #by.xpath
    _heart_icon = "(//div[@id='taplc_hsx_hd_hotels_list_0']//span[contains(@class,'heart')])[{}]" #by.xpath
    # _heart_icon = "(//*[@id='ACCOM_OVERVIEW']//div[@class='listing_title'])[{}]"
    _all_heart_icons_fill = "//div[@id='taplc_hsx_hd_hotels_list_0']//span[contains(@class,'heart-fill')]" #by.xpath
    _new_trip_window = "//body[@id='BODY_BLOCK_JQUERY_REFLOW']//input[@placeholder='Name your trip']" #by.xpath
    _new_trip_create = "//body[@id='BODY_BLOCK_JQUERY_REFLOW']//span[text()='Create']"
    _continue_browsing = "//body[@id='BODY_BLOCK_JQUERY_REFLOW']//span[text()='Continue browsing']"
    _save_to_trip = ".//body[@id='BODY_BLOCK_JQUERY_REFLOW']//span[text()='Save']"
    _my_trips_icon = "//div[@id='taplc_global_nav_action_trips_0']"
    # _my_trips_icon = "//div[@id='taplc_global_nav_action_trips_0']//div[@class='masthead-saves']"
    # _my_trips_icon = "//div[@id='taplc_global_nav_action_trips_0']//a[@class='trips-icon']"
    # _my_trips_icon = "//div[@id='taplc_global_nav_action_trips_0']//span[@class='ui_icon my-trips']"
    _trip_location_icon = "//div[@id='trips-tiles']//a[contains(@class,'has-cover-photo')]"
    _verification_elements = "//div[@id='trip-items-region']//a[@class='title']"


    def search_bar(self, data):
        self.wait_for_element(self._search_bar, "xpath")
        self.send_keys_to_element(data, self._search_bar, "xpath")

    def click_start_date_btn(self):
        self.wait_for_element(self._start_date_btn, "xpath")
        self.click_on_element(self._start_date_btn, "xpath")

    def click_next_month_btn(self):
        self.wait_for_element(self._next_month_btn, "xpath")
        self.click_on_element(self._next_month_btn, "xpath")

    def click_valid_start_date(self):
        all_dates = self.get_elements(self._start_month_all_days, locator_type="xpath")
        for date in all_dates:
            date.click()
            break

    def click_valid_end_date(self):
        all_dates = self.get_elements(self._end_month_all_days, locator_type="xpath")
        for date in all_dates:
            if date.text == "7":
                date.click()
                break

    def click_find_hotels_btn(self):
        self.click_on_element(self._submit_hotels)

    def scroll_rating_category_into_view(self):
        self.wait_for_element(self._hotel_class_rating, "xpath")
        self.scroll_into_view(self._hotel_class_rating, "xpath")

    def click_5_star_rating(self):
        self.wait_for_element(self._5_stars_rating, "xpath")
        self.click_on_element(self._5_stars_rating, "xpath")

    def scroll_web_page_to_first_heart(self):
        self.wait_for_element(self._heart_icon.format(1), "xpath")
        self.scroll_into_view(self._heart_icon.format(1), "xpath")
        self.log.info("Success - Scrolled first heart into view")

    def click_first_heart_btn(self):
        all_hearts = self.get_elements(self._all_heart_icons, "xpath")
        for heart in all_hearts:
            heart.click()
            self.log.info("Success - clicked on a heart icon")
            break

    def name_new_trip(self, data):
        self.wait_for_element(self._new_trip_window, "xpath")
        self.send_keys_to_element(data, self._new_trip_window, "xpath")

    def create_new_trip(self):
        self.wait_for_element(self._new_trip_create, "xpath")
        self.click_on_element(self._new_trip_create, "xpath")

    def click_continue_browsing_btn(self):
        self.wait_for_element(self._continue_browsing, "xpath")
        self.click_on_element(self._continue_browsing, "xpath")

    def click_second_heart_btn(self):
        self.wait_for_element(self._heart_icon.format(2), "xpath")
        all_filled_hearts = self.get_elements(self._all_heart_icons_fill, "xpath")
        all_hearts = self.get_elements(self._all_heart_icons, "xpath")
        for heart in all_hearts:
            if heart not in all_filled_hearts:
                heart.click()
                self.log.info("Success - clicked on a heart icon")
                break

    def click_save_to_trip_btn(self):
        self.wait_for_element(self._save_to_trip, "xpath")
        self.click_on_element(self._save_to_trip, "xpath")

    def scroll_page_up(self):
        self.scroll_web_page()

    def click_my_trips_icon(self):
        result = self.is_element_displayed(self._my_trips_icon, "xpath")
        print (result)
        self.click_on_element(self._my_trips_icon, "xpath")

    def click_my_trips_link(self):
        self.click_on_element(self._trip_location_icon, "xpath")

    def verify_saved_trips(self):
        result = self.get_elements(self._verification_elements)
        if len(result) == 2:
            return True
        else:
            return False





# first
# <span class="saves secondary save-location-214680 ui_icon heart-fill" data-iconclass="heart" data-type="location" data-id="214680" onclick="require(['widget/saves'], function(Saves){ Saves.loadModule('214680'); })"/>
# second:
# <span class="saves secondary save-location-86966 ui_icon heart" data-iconclass="heart" data-type="location" data-id="86966" onclick="require(['widget/saves'], function(Saves){ Saves.loadModule('86966'); })"/
