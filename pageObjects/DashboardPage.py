from HybridPythonFW.configfiles.Locators import Locators
from HybridPythonFW.pages.BasePage import BasePage
from HybridPythonFW.pages.OrderPage import OrderPage
from HybridPythonFW.pages.ProductsListingPage import ProductsListingPage


class DashboardPage(BasePage):
    locators = Locators()
    dashboard_heading = locators.PAGE_HEADING_LABEL
    product_listing_page = locators.PRODUCTS_LISTING_PAGE_LINK
    catalog_menu_link = locators.CATALOG_MENU_LINK

    def __int__(self, driver):
        super().__init__(driver)

    def get_dashboard_page_title(self):
        title = self.get_title()
        return title

    def get_page_heading(self):
        return self.get_element_text(self.dashboard_heading);

    def open_catalog_menu(self):
        self.do_click(self.catalog_menu_link)

    def navigate_to_order_page(self):
        self.do_click(self.order_page)
        return OrderPage(self.driver)

    def navigate_to_product_listing_page(self):
        self.open_catalog_menu()
        self.do_click(self.product_listing_page)
        return ProductsListingPage(self.driver)