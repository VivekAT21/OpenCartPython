import pytest

from HybridPythonFW.pages.LoginPage import LoginPage
from HybridPythonFW.testdata import TestData


@pytest.mark.usefixtures("initiate_browser")
class Test_AddProductPage:

    def navigate_to_add_product_page(self):
        self.loginPage = LoginPage(self.driver)
        dashboardpage = self.loginPage.do_login(TestData.ADMIN_USERNAME, TestData.ADMIN_PASSWORD)
        productlistingpage = dashboardpage.navigate_to_product_listing_page()
        return productlistingpage.navigate_to_add_product_page()

    def test_verify_that_page_heading_is_correct(self):
        add_product_page = self.navigate_to_add_product_page()
        assert add_product_page.get_add_product_page_heading() == "Add Product"

    def test_verify_that_validation_is_prompted_if_user_doesnot_have_permission(self):
        add_product_page = self.navigate_to_add_product_page()
        add_product_page.enter_text_in_general_tab_fields(TestData.PRODUCT_NAME, TestData.PRODUCT_META_TAG)
        validation = add_product_page.get_add_product_validation_text()
        assert validation == "Warning: You do not have permission to modify products!\n×"

    def test_verify_that_validation_is_displayed_for_blank_product_name(self):
        add_product_page = self.navigate_to_add_product_page()
        add_product_page.enter_text_in_general_tab_fields("", TestData.PRODUCT_META_TAG)
        validation = add_product_page.get_blank_product_name_validation()
        assert validation == "Product Name must be greater than 1 and less than 255 characters!"

    def test_verify_that_validation_is_displayed_for_blank_meta_tage_title(self):
        add_product_page = self.navigate_to_add_product_page()
        add_product_page.enter_text_in_general_tab_fields(TestData.PRODUCT_NAME, "")
        validation = add_product_page.get_blank_meta_tag_title_validation()
        assert validation == "Meta Title must be greater than 1 and less than 255 characters!"