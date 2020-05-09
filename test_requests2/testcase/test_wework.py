import pytest

from test_requests2.api.base_api import BaseApi
from test_requests2.api.tag import Tag
from test_requests2.api.wework import WeWork


class TestWeWork:
    test_data = BaseApi.yaml_load('test_work.yaml')
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
        cls.reset()

    @pytest.mark.parametrize("name", test_data['data'])
    def test_wework(self, name):
        self.tag.params['name'] = name
        self.tag.run_steps(self.test_data['steps'])
        # tag = Tag()
        # tag.get()
        # tag.params['name'] = "ffff"
        # result = tag.json_path('$..tag[?(@.name=="ffff")]')
        # tag.delete(result[0]['id'])
    @classmethod
    def reset(cls):
        cls.tag.get()
        for name in ['demo1', 'demo2', 'demo3']:
            res = cls.tag.json_path(f'$..tag[?(@.name=="{name}")]')
            if isinstance(res, list) and len(res) > 0:
                cls.tag.delete(tag_id=[res[0]['id']])

        cls.tag.get()