from selenium import webdriver
from pages.home.login_page import Login
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

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("orenkostin@gmail.com", "Abrakadabra2016")
        result = self.lp.verify_login_successful()
        self.ts.mark_final("test_valid_login", result, "Login failed")

    @pytest.mark.run(order=1)
    # @data(("",""), ("oren_test1@gmail",""), ("","123456"), ("oren_test1@gmail","123456"))
    @data(*get_csv_data("C:\\Users\okostin\Documents\Python\Selenium\Frameworks\Amazon\\invalid_login.csv"))
    @unpack
    def test_invalid_login(self, username, password):
        self.lp.log_out()
        self.lp.login(username, password)
        result = self.lp.verify_login_failed_global()
        self.ts.mark_final("test_invalid_login", result, "Login successful")

    # @pytest.mark.run(order=1)
    # def test_logout(self):
    #     self.lp.log_out()
    #     result = self.lp.verify_log_out_successful()
    #     self.ts.mark_final("test_logout", result, "Login page displayed")
