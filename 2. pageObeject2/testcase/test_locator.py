class TestLocator:
    def test_locator(self):
        a = "abcde%sjalfj"
        b = "FFF"
        c = a % b
        assert "avc" in c