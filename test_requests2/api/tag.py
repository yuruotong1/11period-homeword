from test_requests2.api.wework import WeWork


class Tag(WeWork):
    def __init__(self):
        secrete = "heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0"
        self.params['access_token']=self.get_token(secrete)
        self.tag_data = self.yaml_load('../api/tag.yaml')

    def get(self, **kwargs):
        self.send_api(self.tag_data['get'])

    def add(self, **kwargs):
        self.send_api(self.tag_data['add'])

    def delete(self, tag_id=[], group_id=[], **kwargs):
        self.params['tag_id'] = tag_id
        self.params['group_id'] = group_id
        self.send_api(self.tag_data['delete'])

    def update(self):
        pass
