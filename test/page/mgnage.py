from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Manage(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#manageTools'

    def add_picture(self):
        goto_material_locator = (By.CSS_SELECTOR, '[href="#material/text"]')
        goto_picture_locator = (By.CSS_SELECTOR, '[href="#material/image"]')
        goto_add_picture_locator = (By.CSS_SELECTOR, '.js_upload_file_selector')
        upload_picture_locator = (By.ID, 'js_upload_input')
        self.find_element(goto_material_locator).click()
        self.find_element(goto_picture_locator).click()
        self.find_element(goto_add_picture_locator).click()
        self.find_element(upload_picture_locator).send_keys("C:/Users/yuruo/Desktop/Snipaste_2020-02-11_09-51-47.png")

    def get_picture(self, name):
        new_picture_locator = (By.CSS_SELECTOR, '.material_picCard_cnt_pic[style*="%s"]' % name)
        return len(self.find_elements(new_picture_locator)) >= 1
