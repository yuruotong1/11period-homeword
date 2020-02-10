from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None, reuse=False):
        self._driver = None
        self._base_url = ""
        if driver is None:
            if reuse:
                chrome_option = webdriver.ChromeOptions()
                chrome_option.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=chrome_option)
            else:
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def findElements(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by, locator)
