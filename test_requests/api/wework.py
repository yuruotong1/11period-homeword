import requests

from test_requests.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = "wwd6da61649bd66fea"

    @classmethod
    def get_token(cls, secrete):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(base_url,
                         params={"corpid": cls.corpid,
                                 "corpsecret": secrete}
                         )
        return r.json()['access_token']

