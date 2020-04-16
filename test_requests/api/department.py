import requests
from test_requests.api.wework import WeWork


class Department(WeWork):
    secrete = "C7uGOrNyxWWzwBsUyWEbLUlJOWjU7Qw5ORPxemPKw6w"
    def create(self, name, id, **kwargs):
        data={"name":name, "parentid":id}
        data.update(kwargs)
        base_ur = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        r = requests.post(base_ur,
                      params={"access_token":WeWork.get_token(self.secrete)},
                      json=data
                      )
        return r.json()

    def update(self, id, **kwargs):
        base_url="https://qyapi.weixin.qq.com/cgi-bin/department/update"
        data={"id":id}
        data.update(kwargs)
        r = requests.post(base_url,
            params={"access_token": WeWork.get_token(self.secrete)},
            json=data
        )
        return r.json()

    def delete(self, id):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(base_url,
                          params={"access_token": WeWork.get_token(self.secrete),
                                  "id":id
                                  }
                          )
        return r.json()




    def get(self, id=1):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(base_url,
                          params={"access_token": WeWork.get_token(self.secrete),
                                  "id":id
                                  }
                          )
        return r.json()