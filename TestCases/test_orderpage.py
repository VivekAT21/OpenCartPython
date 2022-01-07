import pytest

from OpenCartPython.pageObjects.DashboardPage import DashboardPage
from OpenCartPython.pageObjects.LoginPage import LoginPage
from OpenCartPython.pageObjects.OrderPage import OrderPage
from OpenCartPython.TestData import TestData


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
