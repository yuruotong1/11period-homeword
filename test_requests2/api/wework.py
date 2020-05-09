from test_requests2.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self, secrete):
        wework_data = self.yaml_load('../api/wework.yaml')
        self.params['corpsecret'] = secrete
        return self.send_api(wework_data['get_token'])['access_token']
