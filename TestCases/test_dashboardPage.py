import pytest
from OpenCartPython.TestData import TestData
from OpenCartPython.pageObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("initiate_browser")
class Test_DashboardPage:
    admin_username = TestData.ADMIN_USERNAME
    admin_password = TestData.ADMIN_PASSWORD
    admin_dashboard_heading = TestData.ADMIN_DASHBOARD_HEADING

    def test_verify_dashboard_page_title(self):
        self.loginPage = LoginPage(self.driver)
        dashboardpage = self.loginPage.do_login(self.admin_username, self.admin_password)
        assert dashboardpage.get_page_heading() == self.admin_dashboard_heading