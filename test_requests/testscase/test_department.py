import pytest

from test_requests.api.department import Department
from test_requests.api.wework import WeWork


class TestDepartment:
    def setup(self):
        self.department = Department()

    def test_token(self):
        r = WeWork.get_token("C7uGOrNyxWWzwBsUyWEbLUlJOWjU7Qw5ORPxemPKw6w")
        assert r["errmsg"] == "ok"

    def test_create(self):
        r = self.department.create("hello",1)
        assert  r["errmsg"] == "created"


    def test_update(self):
        r = self.department.update(1067, name="abcde")
        assert r["errmsg"] == "updated"

    def test_delete(self):
        r = self.department.delete(1067)
        assert r["errmsg"] == "deleted"

    def test_get(self):
        r = self.department.get(1067)
        assert r["errmsg"] == "ok"


    @pytest.mark.parametrize("a", [{"abc":1,"dd":2, "ff":2},{"kkk":1}])
    def test_dict(self, a):
        print(a)