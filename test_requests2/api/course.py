import logging
import re
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO)


class Course:
    _black_list = ["【资料】"]

    def __init__(self):
        chromeOptions = Options()
        chromeOptions.debugger_address = "127.0.0.1:9222"
        self._driver = webdriver.Chrome(options=chromeOptions)
        # self._driver = webdriver.Chrome()
        # self._driver.get('https://ke.qq.com/course/513051?tuin=62382059')

        with open('./article.md', "r+") as f:
            f.truncate()  # 清空文件

    def get_course(self):
        # 计算出有多少小节
        knobs = len(self._driver.find_elements(By.CSS_SELECTOR, '.task-part-list>div'))
        logging.info("有 " + str(knobs) + " 小节")
        for knob in range(1, knobs + 1):
            knob_locator = '.task-part-list>div:nth-child(%s)' % (knob)
            global link
            link = ".task-part-item:nth-child(%s)" % (knob)
            # 获取小节标题
            knob_title_locator = knob_locator + ' h3'
            knob_title = self._driver.find_element(By.CSS_SELECTOR, knob_title_locator).text
            logging.info("标题为：" + knob_title)
            # 将小节标题写入文件
            self.file_write("# " + knob_title)
            # 在标题后追加换行符号
            self.file_write("")
            # 在markdown创建表格
            self.file_write("课程章节名称|上课时间|回放视频地址|课程贴地址|课件下载|安装软件教程|课程问卷|")
            self.file_write("|---|---|---|---|---|---|---|")
            # 一个小节可能有多个任务

            knob_tasks_locator = knob_locator + ' a'
            knob_tasks = len(self._driver.find_elements(By.CSS_SELECTOR, knob_tasks_locator))
            # 遍历每一个任务，提取出任务内容和时间
            self.task(knob_title, knob_tasks, knob_tasks_locator)

    def file_write(self, content):
        file = open("./article.md", "a", encoding='utf-8')
        file.write(content + "\n")
        file.close()

    def task(self, knob_title, knob_tasks, knob_tasks_locator):
        for task in range(1, knob_tasks + 1):
            # 用来跳过黑名单
            break_tag = False
            task_content_locator = knob_tasks_locator + ':nth-child(%s) p>span:nth-child(1)' % (task)
            task_time_locator = knob_tasks_locator + ':nth-child(%s) p>span:nth-child(2)' % (task)
            task_content = self._driver.find_element(By.CSS_SELECTOR, task_content_locator).text
            task_href = link + " .task-task-item:nth-child(%s)" % (task)
            task_href_link = self._driver.find_element(By.CSS_SELECTOR, task_href).get_attribute('href')
            # 检测黑名单，设置标记
            for black in self._black_list:
                if black in task_content:
                    break_tag = True
            # 跳过黑名单
            if not break_tag:
                # 将回放改成直播
                task_content = re.sub("【回放】", "【直播】", task_content)
                task_time = self._driver.find_element(By.CSS_SELECTOR, task_time_locator).text
                # 将内容和时间写入表格
                self.file_write \
                        (
                        task_content + "|" + task_time + "|" + "[" + task_content + "]" + "(" + task_href_link + ")" + "|" +
                        "||||")
                # 在每个表格后追加换行符号
        self.file_write("")
