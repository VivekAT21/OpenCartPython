import pytest
from OpenCartPython.TestData import TestData
from OpenCartPython.pageObjects.DashboardPage import DashboardPage
from OpenCartPython.pageObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("initiate_browser")
class Test_Login():

    def test_verify_page_title(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.get_login_page_title() == TestData.ADMIN_LOGIN_PAGE_TITLE

    def test_verify_if_user_is_able_to_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("admin", "admin")
        self.dashboardPage = DashboardPage(self.driver)
        assert self.dashboardPage.get_page_title() == "Dashboard"