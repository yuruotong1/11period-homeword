from page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        self._pamrams["value"]=value
        self.steps("../page/search.yaml")
