from OpenCartPython.configfiles.Locators import Locators
from OpenCartPython.pageObjects.BasePage import BasePage


class AddProductPage(BasePage):
    locators = Locators()

    def __init__(self, driver):
        super().__init__(driver)

    def get_add_product_page_heading(self):
        return self.get_element_text(self.locators.PANEL_HEADING_LABEL)

    def enter_text_in_general_tab_fields(self, product_name, meta_tag_name):
        self.do_send_keys(self.locators.PRODUCT_GEN_PRODUCT_NAME, product_name)
        self.scroll_till_element_is_visible(self.locators.PRODUCT_GEN_META_TAG_TITLE)
        self.do_send_keys(self.locators.PRODUCT_GEN_META_TAG_TITLE, meta_tag_name)
        self.do_click(self.locators.SAVE_PRODUCT_ICON)

    def get_add_product_validation_text(self):
        return self.get_element_text(self.locators.VALIDATION_ADD_PRODUCT_BANNER)

    def get_blank_product_name_validation(self):
        return self.get_element_text(self.locators.VALIDATION_PRODUCT_NAME)

    def get_blank_meta_tag_title_validation(self):
        return self.get_element_text(self.locators.VALIDATION_META_TAG)