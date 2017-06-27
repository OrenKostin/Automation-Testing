from pages.home.my_trips_page import MyTrips
from utilities.assert_status import AssertStatus
import unittest, pytest
import time

@pytest.mark.usefixtures("one_time_setup")
class TestMyTrips(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_setup):
        self.mt = MyTrips(self.driver)
        self.ts = AssertStatus(self.driver)


    def test_my_trips_feature(self):
        self.mt.search_bar("hawaii")
        self.mt.click_start_date_btn()
        self.mt.click_valid_start_date()
        self.mt.click_valid_end_date()
        self.mt.click_find_hotels_btn()


        self.mt.scroll_rating_category_into_view()
        time.sleep(1)
        self.mt.click_5_star_rating()
        time.sleep(1)
        self.mt.scroll_web_page_to_first_heart()
        self.mt.click_first_heart_btn()
        time.sleep(1)
        self.mt.name_new_trip("HAWAII")
        time.sleep(1)
        self.mt.create_new_trip()
        time.sleep(1)
        self.mt.click_continue_browsing_btn()
        time.sleep(1)
        self.mt.click_second_heart_btn()
        time.sleep(1)
        self.mt.click_save_to_trip_btn()
        time.sleep(1)
        self.mt.click_continue_browsing_btn()
        time.sleep(1)
        self.mt.scroll_page_up()
        time.sleep(1)
        self.mt.click_my_trips_icon()
        time.sleep(1)
        self.mt.click_my_trips_link()
        time.sleep(1)

        result = self.mt.verify_saved_trips()
        self.ts.mark_final("test_my_trips_feature", result, "Items saved != 2")
