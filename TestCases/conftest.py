import pytest
from selenium import webdriver
from selenium.webdriver.common.devtools.v85 import headless_experimental
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from OpenCartPython.configfiles.config import config_constants


@pytest.fixture(scope="function", params=["chrome"])
# request is a special fixture provided by the pytest
# it provides the info of the requested functions
def initiate_browser(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # request.class.driver
    # means driver is available to the requesting class
    request.cls.driver = web_driver
    web_driver.maximize_window()
    web_driver.get(config_constants.BASE_URL)
    yield
    web_driver.close()