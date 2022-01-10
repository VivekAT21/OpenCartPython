from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from OpenCartPython.configfiles import config

class BasePage:
    const = config.config_constants()
    dur = const.WAIT_DURATION

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def do_click(self, by_locator):
        WebDriverWait(self.driver, self.dur).until(EC.visibility_of_element_located(by_locator)).click()

    def do_clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def do_send_keys(self, by_locator, text):
        self.do_clear(by_locator)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, self.dur).until(EC.visibility_of_element_located(by_locator)).text

    def get_title_visible(self, title):
        return WebDriverWait(self.driver, 10).until(EC.title_is(title))

    '''atb_nme is attribute_name'''
    def get_attribute_value(self, by_locator, atb_nme):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).get_attribute(atb_nme)

    def check_element_is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_enabled()

    '''for hidden elements'''
    def check_element_is_displayed(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def check_element_is_selected(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_selected()

    def select_dropdown_by_value(self, by_locator, value):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        select_wb = Select(web_element)
        return select_wb.select_by_value(value)

    def select_dropdown_list_by_value(self, by_locator, value):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        web_select = Select(web_element)
        option_list = web_select.options
        for ele in option_list:
            if ele.text == 'Option3':
                ele.click()
                break

    def scroll_till_element_is_visible(self, by_locator):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", web_element)

    def scroll_till_end_of_page(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def get_no_of_rows_or_col_in_table(self, by_locator):
        return len(WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator)))