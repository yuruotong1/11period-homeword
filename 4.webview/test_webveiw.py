from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebview:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True
        caps['noReset'] = True
        caps['chromedriverExecutable'] = 'D:/develop/chromedriver/2.20.exe'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def test_webview(self):
        self.driver.find_element(By.XPATH, '//*[@text="交易" and contains(@resource-id, "tab_name")]').click()
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_xueying_SJY").click()
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="请输入手机号"]')))
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入手机号"]').send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入验证码"]').send_keys("555555")
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(By.ID, "action_bar_back").click()