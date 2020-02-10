from page.contact import Contact
from page.main import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)
        self.contact = Contact(reuse=True)

    def test_add_member(self):
        self.main.add_member().add_member("seveniruby")
        assert self.contact.get_first_member("seveniruby")
