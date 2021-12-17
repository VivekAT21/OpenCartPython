from selenium.webdriver.common.by import By


class Locators:
    """LOGIN PAGE LOCATORS"""

    ADMIN_EMAIL_INPUT = (By.ID, "input-username")
    ADMIN_PWD_INPUT = (By.ID, "input-password")
    ADMIN_LOGIN_BTN = (By.XPATH, "//button[@class='btn btn-primary']")

    '''PAGE HEADING LOCATOR'''
    PAGE_HEADING_LABEL = (By.TAG_NAME, "h1")
    PANEL_HEADING_LABEL = (By.XPATH, "//h3[@class='panel-title']")

    '''DASHBOARD PAGE LOCATORS'''
    DASHBOARD_HEADING_LABEL = (By.TAG_NAME, "h1")
    ORDERS_LISTING_PAGE_LINK = (By.XPATH, "//div[@class='row']//div[1]//div[1]//div[3]//a[1]")
    CATALOG_MENU_LINK = (By.ID, 'menu-catalog')

    '''CATALOG MENU LINKS'''
    PRODUCTS_LISTING_PAGE_LINK = (By.XPATH, "//a[normalize-space()='Products']")
    PRODUCTS_LISTING_ROWS = (By.XPATH, "//div[@class='panel-body']//tbody//tr")
    PRODUCTS_LISTING_COLUMNS = (By.XPATH, "//div[@class='panel-body']//tbody//tr[1]//td")

    def PRODUCTS_LISTING_COLUMN_VALUE(self, i, j):
        return By.XPATH, "//div[@class='panel-body']//tbody//tr[" + i + "]//td[" + j + "]"

    PRDUCTS_LISTING_GRID_HEADING = (By.XPATH, "//h3[normalize-space()='Product List']")

    '''PRODUCTS LISTING PAGE LOCATORS'''
    ADD_PRODUCT_BTN = (By.XPATH, "//i[@class='fa fa-plus']")

    ''''ADD PRODUCT PAGE LOCATORS'''
    SAVE_PRODUCT_ICON = (By.XPATH,  "//button[@type='submit']")
    ADD_PRODUCT_TAB_GENERAL = (By.XPATH, "//a[normalize-space()='General']")
    PRODUCT_GEN_PRODUCT_NAME = (By.ID, "input-name1")
    PRODUCT_GEN_META_TAG_TITLE = (By.ID, "input-meta-title1")
    ADD_PRODUCT_TAB_DATA = (By.XPATH, "//a[normalize-space()='Data']")
    ADD_PRODUCT_TAB_LINKS = (By.XPATH, "//a[normalize-space()='Link']")
    ADD_PRODUCT_TAB_ATTRIBUTE = (By.XPATH, "//a[normalize-space()='Attribute']")
    ADD_PRODUCT_TAB_OPTION = (By.XPATH, "//a[normalize-space()='Option']")
    ADD_PRODUCT_TAB_RECURRING = (By.XPATH, "//a[normalize-space()='Recurring']")

    VALIDATION_ADD_PRODUCT_BANNER = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    VALIDATION_COMMON_LOCATOR = "/following-sibling::div[@class='text-danger']"
    VALIDATION_PRODUCT_NAME = (By.XPATH, "//input[@id='input-name1']" + VALIDATION_COMMON_LOCATOR)
    VALIDATION_META_TAG = (By.XPATH, "//input[@id='input-meta-title1']" + VALIDATION_COMMON_LOCATOR)

