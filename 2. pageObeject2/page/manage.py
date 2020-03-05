from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Manage(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#manageTools'

    def load_picture(self):
        material_locator = (By.CSS_SELECTOR, '[href="#material/text"]')
        goto_picture_locator = (By.CSS_SELECTOR, '[href="#material/image"]')
        goto_upload_locator = (By.CSS_SELECTOR, '.js_upload_file_selector')
        upload_locator = (By.CSS_SELECTOR, '#js_upload_input')
        self.find_element(material_locator).click()
        self.find_element(goto_picture_locator).click()
        self.find_element(goto_upload_locator).click()
        self.find_element(upload_locator).send_keys("C:/Users/yuruo/Desktop/Snipaste_2020-02-14_19-22-34.png")

    def get_picture(self):
        first_picture_locator = (By.CSS_SELECTOR, '.material_picCard_cnt_pic')
        return self.find_element(first_picture_locator).get_attribute("style")