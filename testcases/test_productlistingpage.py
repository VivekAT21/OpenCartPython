import pytest
from HybridPythonFW.pages.LoginPage import LoginPage
from HybridPythonFW.testdata import TestData


@pytest.mark.usefixtures("initiate_browser")
class Test_ProductListingPage:
    admin_username = TestData.ADMIN_USERNAME
    admin_password = TestData.ADMIN_PASSWORD
    admin_dashboard_heading = TestData.ADMIN_DASHBOARD_HEADING

    def test_verify_that_page_heading_is_correct(self):
        self.loginPage = LoginPage(self.driver)
        dashboardpage = self.loginPage.do_login(self.admin_username, self.admin_password)
        productlistingpage = dashboardpage.navigate_to_product_listing_page()
        productlistingpage.print_values()
        assert productlistingpage.get_count_of_col() == 8


