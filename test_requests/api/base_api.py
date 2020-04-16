import json


class BaseApi:
    def format(self, r):
        print(json.dump(r.json(), indent=2))