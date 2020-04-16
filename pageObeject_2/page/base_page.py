from selenium import webdriver


class BasePage:
    _base_url = ""

    def __init__(self, reuse=False):
        if reuse:
            chrome_option = webdriver.ChromeOptions()
            chrome_option.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=chrome_option)
        else:
            self._driver = webdriver.Chrome()
        if self._base_url != "":
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(3)

    def find_element(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        return self._driver.find_element(by, locator)

    def find_elements(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)
        return self._driver.find_elements(by, locator)
