from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Contact(BasePage):
    def add_member(self):
        user_name_locator = (By.ID, 'username')
        acctid_locator = (By.ID, 'memberAdd_acctid')
        gender_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        zipcode_locator = (By.CSS_SELECTOR, '.ww_telInput_zipCode')
        macao_locator = (By.CSS_SELECTOR, '[data-value="853"]')
        mobile_number_locator = (By.ID, 'memberAdd_phone')
        save_locator = (By.CSS_SELECTOR, '.js_btn_save')
        self.find_element(user_name_locator).send_keys("MrDong")
        self.find_element(acctid_locator).send_keys("MrDong")
        self.find_element(gender_locator).click()
        self.find_element(zipcode_locator).click()
        self.find_element(macao_locator).click()
        self.find_element(mobile_number_locator).send_keys("66666666")
        self.find_element(save_locator).click()
        return self

    def get_member(self, name):
        first_member_locator = (By.CSS_SELECTOR, '#member_list td:nth-child(2)[title="%s"]' % name)
        return len(self.find_elements(first_member_locator)) >= 1
