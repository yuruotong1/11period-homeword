from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.contact import Contact
from page.manage import Manage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def add_member(self):
        locator = (By.LINK_TEXT, '添加成员')
        self._driver.execute_script("arguments[0].click();", self.find(locator))
        return Contact(reuse=True)



    def add_picture(self):
        menu_manage_locator = (By.CSS_SELECTOR, '#menu_manageTools')
        material_locator = (By.CSS_SELECTOR, '[href = "#material/text"]')
        self.find(menu_manage_locator).click()
        self.find(material_locator).click()
        return Manage(reuse=True)
