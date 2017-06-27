from pages.home.login_page import LoginPage
from utilities.assert_status import AssertStatus
import unittest, pytest
import time

@pytest.mark.usefixtures("one_time_setup")
class TestLoginPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        self.ts = AssertStatus(self.driver)

    @pytest.mark.run(order=3)
    def test_valid_login(self, email="oren.test3@gmail.com", password="dragon"):
        # self.lp.click_profile_icon()
        # self.lp.switch_to_login_frame()
        self.lp.enter_email(email)
        self.lp.enter_password(password)
        self.lp.click_log_in_btn()
        self.driver.switch_to.default_content()
        result = self.lp.verify_login_successful()
        self.ts.mark_final("test_valid_login", result, "user name is not displayed")

    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        self.lp.invalid_login("oren.test3@gmail.com", "123")
        result = self.lp.verify_login_failed()
        self.ts.mark_final("test_invalid_login", result, "error message is not displayed")
        time.sleep(1)

    @pytest.mark.run(order=1)
    def test_log_out(self):
        self.lp.click_user_name()
        self.lp.click_sign_out_btn()
        result = self.lp.verify_logout_successful()
        self.ts.mark_final("test_log_out", result, "JOIN link is not displayed")
