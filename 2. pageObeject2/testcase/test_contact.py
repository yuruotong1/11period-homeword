from page.main import Main


class TestContact:
    def setup(self):
        self.main = Main(reuse=True)

    def test_contact(self):
        self.contact = self.main.goto_add_member().add_member()
        assert self.contact.get_member() == "MrDong"



