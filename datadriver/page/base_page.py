import logging

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO)
class BasePage:
    _black_list = [
        (By.ID, 'image_cancel')]
    _error_count = 0
    _error_max=10
    #value:jd
    _pamrams={}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator=None):
        try:
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_count=0
            return element
        except Exception as e:
            self._error_count+=1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    logging.info(len(elements))
                    elements[0].click()
                    break
            return self.find(by, locator)


    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count+=1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    logging.info(len(elements))
                    elements[0].click()
                    break
            return self.send(value, by, locator)


    # - by: xpath
    # locator: '//*[@text="行情" and contains(@resource-id, "tab_name")]'
    # action: click

    # - by: id
    # locator: search_input_text
    # action: send
    # value: "{value}"
    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            steps:list[dict]=yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element=self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        content:str = step["value"]
                        for param in self._pamrams:
                            content = content.replace("{%s}"%param, self._pamrams[param])
                        self.send(content, step["by"], step["locator"])



