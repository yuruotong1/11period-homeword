import requests
from jsonpath import jsonpath

from test_requests2.api.base_api import BaseApi


class Topic(BaseApi):
    proxies = {
        "https": "http://127.0.0.1:8888",
        "http": "http://127.0.0.1:8888"

    }

    def create_topic(self, title, raw, category):
        # format = {
        #     "title": "hello",
        #     "raw": "rawrawrawrawrawrawrawrawrawr",
        #     "category": "18"
        # }
        json_data = {
            "title": title,
            "raw": raw,
            "category": category
        }
        result = requests.request(
            method="post",
            url="https://home.testing-studio.com/posts.json",
            headers={"Api-Key": "ac0a96ece9875adbecf66ee1189f22befcad2b3e73f3aa1afb3a67cb17f840b5",
                     "Api-Username": "ruotongyu"
                     },
            json=json_data,
            proxies=self.proxies,
            verify=False

        )
        print(result.json())
        topic_id = jsonpath(result.json(), "$..topic_id")
        return "https://home.testing-studio.com/t/topic/" + topic_id
