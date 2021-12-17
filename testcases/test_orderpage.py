import pytest

from HybridPythonFW.pages.DashboardPage import DashboardPage
from HybridPythonFW.pages.LoginPage import LoginPage
from HybridPythonFW.pages.OrderPage import OrderPage
from HybridPythonFW.testdata import TestData


@pytest.mark.usefixtures("initiate_browser")
class Test_OrderPage:
    admin_username = TestData.ADMIN_USERNAME
    admin_password = TestData.ADMIN_PASSWORD
    admin_orders_title = TestData.ADMIN_ORDER_TITLE

    def navigate_order_page(self):
        self.loginPage = LoginPage(self.driver)
        dashboard_page = self.loginPage.do_login(self.admin_username, self.admin_password)
        dashboard_page.navigate_to_order_page()
        return OrderPage(self.driver)

    def test_verify_order_page_title(self):
        order_page = self.navigate_order_page()
        assert order_page.get_the_order_page_title() == self.admin_orders_title

    # def test_verify_order_page_title(self):
    #     self.loginPage = LoginPage(self.driver)
    #     dashboard_page = self.loginPage.do_login(self.admin_username, self.admin_password)
    #     order_page = dashboard_page.navigate_to_order_page()
    #     assert order_page.get_the_order_page_title() == self.admin_orders_title
