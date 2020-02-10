from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Manage(BasePage):
    def add_picture(self):
        add_picture_locator = (By.CSS_SELECTOR, '[href="#material/image"]')
        picture_load_locator = (By.CSS_SELECTOR, '#materialMain .js_upload_file_selector')
        picture_locator = (By.CSS_SELECTOR, '#js_upload_input')
        self.find(add_picture_locator).click()
        self.find(picture_load_locator).click()
        self.find(picture_locator).send_keys("C:/Users/yuruo/Desktop/Snipaste_2020-02-10_12-14-35.png")

    def get_picture(self, name):
        locator = (By.CSS_SELECTOR, 'div[style*="%s"' % name)
        return len(self.findElements(locator)) >= 1
