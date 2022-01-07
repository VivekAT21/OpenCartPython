from OpenCartPython.pageObjects.BasePage import BasePage
from OpenCartPython.configfiles.Locators import Locators
from OpenCartPython.pageObjects.DashboardPage import DashboardPage


class LoginPage(BasePage):

    # BY LOCATORS
    locators = Locators()
    admin_email = locators.ADMIN_EMAIL_INPUT
    admin_pwd = locators.ADMIN_PWD_INPUT
    admin_login = locators.ADMIN_LOGIN_BTN

    # Constructor of the page class
    def __int__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self):
        title = self.get_title()
        return title

    def do_login(self, username, password):
        self.do_send_keys(self.admin_email, username)
        self.do_send_keys(self.admin_pwd, password)
        self.do_click(self.admin_login)
        return DashboardPage(self.driver)