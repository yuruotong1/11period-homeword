from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps['autoGrantPermissions'] = True
            # caps['noReset'] = True
            caps['chromedriverExecutable'] = 'D:/develop/chromedriver/2.20.exe'
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self)->Main():
        return Main(self._driver)
