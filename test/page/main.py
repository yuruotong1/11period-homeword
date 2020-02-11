from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.contact import Contact


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_add_member(self):
        add_member_locator = (By.CSS_SELECTOR, '[node-type="addmember"]')
        self.find_element(add_member_locator).click()
        return Contact(reuse=True)

