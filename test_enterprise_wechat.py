from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHome():
    def setup(self):
        chromeOptions = Options()
        chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.implicitly_wait(1)

    def teardown(self):
        self.driver.quit()

    def test_home(self):
        self.driver.find_element(By.ID, '.menu_contacts').click()
        WebDriverWait(self.driver, 10).until(self.wait_element)
        #self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        self.driver.find_element(By.ID, 'username').send_keys("abc")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("abce")
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys("11111111112")
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()


    def wait_element(self, x):
        size = len(self.driver.find_elements(By.ID, 'username'))
        if size < 1:
            self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        return size >= 1
