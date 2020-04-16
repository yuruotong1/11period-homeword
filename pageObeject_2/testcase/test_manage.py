from page.manage import Manage


class TestManage:
    def setup(self):
        self.manage = Manage(reuse=True)

    def test_manage(self):
        self.manage.load_picture()
        assert "Snipaste_2020-02-14_19-22-34.png" in self.manage.get_picture()
