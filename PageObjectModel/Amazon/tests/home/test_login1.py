from selenium import webdriver
from pages.home.login_page1 import Login
from utilities.assert_status import AssertStatus
import unittest, pytest
import time
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("one_time_setup")
@ddt
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_setup):
        self.lp = Login(self.driver)
        self.ts = AssertStatus(self.driver)

    # @pytest.mark.run(order=2)
    # def test_valid_login(self):
    #     self.lp.login("oren.test3@gmail.com", "dragon123456")
    #     result = self.lp.verify_login_successful()
    #     self.ts.mark_final("test_valid_login", result, "Login failed")

    @pytest.mark.run(order=1)
    @unpack
    def test_invalid_login(self):
        self.lp.login("oren_test1@gmail","123456")
        result = self.lp.verify_login_failed_global()
        self.ts.mark_final("test_invalid_login", result, "Login successful")
