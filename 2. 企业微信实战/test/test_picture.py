from page.main import Main
from page.manage import Manage


class TestPicture:
    def setup(self):
        self.main = Main(reuse=True)
        self.manage = Manage(reuse=True)

    def test_picture(self):
        self.main.add_picture().add_picture()
        assert self.manage.get_picture("Snipaste_2020-02-10_12-14-351")
