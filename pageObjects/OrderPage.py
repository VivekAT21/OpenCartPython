from OpenCartPython.pageObjects.BasePage import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_the_order_page_title(self):
        return self.get_title()