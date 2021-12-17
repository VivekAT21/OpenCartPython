from HybridPythonFW.configfiles.Locators import Locators
from HybridPythonFW.pages.AddProductPage import AddProductPage
from HybridPythonFW.pages.BasePage import BasePage


class ProductsListingPage(BasePage):
    locators = Locators()

    def __int__(self, driver):
        super().__init__(driver)

    def get_products_listing_page_title(self):
        title = self.get_title()
        return title

    def get_products_listing_page_heading(self):
        return self.get_element_text(self.locators.PRDUCTS_LISTING_GRID_HEADING);

    def get_count_of_rows(self):
        return self.get_no_of_rows_or_col_in_table(self.locators.PRODUCTS_LISTING_ROWS)

    def get_count_of_col(self):
        return self.get_no_of_rows_or_col_in_table(self.locators.PRODUCTS_LISTING_COLUMNS)

    def get_value_of_n_row_from_table(self):
        data_list = []
        row_count = self.get_count_of_rows()
        col_count = self.get_count_of_col()
        for i in range(1, row_count):
            row_value = []
            for j in range(3, col_count-1):
                row_value.append(self.get_element_text(self.locators.PRODUCTS_LISTING_COLUMN_VALUE(str(i), str(j))))
            data_list.append(row_value)
        return data_list

    def print_values(self):
        list_len = len(self.get_value_of_n_row_from_table())
        print(self.get_value_of_n_row_from_table()[0])

    def navigate_to_add_product_page(self):
        self.do_click(self.locators.ADD_PRODUCT_BTN)
        return AddProductPage(self.driver)