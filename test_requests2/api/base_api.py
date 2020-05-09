import json

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:
    # key:value
    params = {}
    data = {}

    @staticmethod
    def yaml_load(path):
        with open(path) as f:
            return yaml.safe_load(f)

    def json_path(self, path, r=None, **kwargs):
        if r is None:
            r = self.r
        return jsonpath(r, path)

    @classmethod
    def format(cls, r):
        cls.r = r.json()
        result = json.dumps(json.loads(r.text), indent=2, ensure_ascii=False)
        print(result)
        return result

    def send_api(self, data: dict):
        raw = yaml.dump(data)
        for key, value in self.params.items():
            raw = raw.replace(f'${{{key}}}', repr(value))
        data = yaml.load(raw)
        proxies = {
            "https":"http://127.0.0.1:8888",
            "http":"http://127.0.0.1:8888"

        }
        result = requests.request(
            method=data['method'],
            url=data['url'],
            params=data.get('params'),
            header=data.get('header'),
            json=data.get('json'),
            proxies=proxies,
            verify=False

        )

        self.format(result)
        return result.json()

    def run_steps(self, steps:list):
        for step in steps:
            raw = yaml.dump(step)
            for key, value in self.params.items():
                raw = raw.replace(f'${{{key}}}', repr(value))
            step = yaml.load(raw)
            if 'method' in step.keys():
                method = step['method'].split('.')[-1]
                getattr(self, method)(**step)
            if 'extract' in step.keys():
                self.data[step['extract']] = self.json_path(**step)
            if 'assert' in step.keys():
                assert eval(step['assert'])