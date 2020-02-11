from page.mgnage import Manage


class TestManage:
    def setup(self):
        self.manage = Manage(reuse=True)

    def test_add_picture(self):
        self.manage.add_picture()
        assert self.manage.get_picture("Snipaste_2020-02-11_09-51-471.png")

