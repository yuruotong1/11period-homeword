from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Contact(BasePage):

    def add_member(self, name):
        name_locator = (By.NAME, 'username')
        acctid_locator = (By.NAME, 'acctid')
        gender_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        mobile_locator = (By.NAME, 'mobile')
        sure_locator = (By.CSS_SELECTOR, '.js_btn_save')
        self.find(name_locator).send_keys(name)
        self.find(acctid_locator).send_keys("seveniruby")
        self.find(gender_locator).click()
        self.find((By.CSS_SELECTOR, ".ww_telInput_zipCode_input")).click()
        self.find((By.CSS_SELECTOR, 'li[data-value="853"]')).click()
        self.find(mobile_locator).send_keys("66666666")
        self.find(sure_locator).click()

    def get_first_member(self, member_name):
        locator = (By.CSS_SELECTOR, '#member_list td:nth-child(2)[title="%s"]' % member_name)
        return len(self.findElements(locator)) >= 1
