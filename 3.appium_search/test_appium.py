from appium import webdriver
from appium.webdriver.common import mobileby
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True
        caps['noReset'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def test_search(self):
        self.driver.find_element(By.ID, 'tv_search').click()
        self.driver.find_element(By.ID, 'search_input_text').send_keys("alibaba")
        self.driver.find_element(By.XPATH, '//*[@text="BABA"]').click()
        self.driver.find_element(By.XPATH, '//*[contains(@resource-id, "title_container")]//*[@text="股票"]').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@text="09988"]/../../..//*[contains(@resource-id, "follow_btn")]').click()
        self.driver.find_element(By.ID, 'action_delete_text').click()
        self.driver.find_element(By.ID, 'search_input_text').send_keys("alibaba")
        self.driver.find_element(By.XPATH, '//*[@text="BABA"]').click()
        self.driver.find_element(By.XPATH, '//*[contains(@resource-id, "title_container")]//*[@text="股票"]').click()
        res = self.driver.find_element(By.XPATH,
                                       '//*[@text="09988"]/../../..//*[contains(@resource-id, "followed_btn")]').get_attribute(
            "text")
        self.driver.hide_keyboard()

        mobileby
        assert "已添加" == res