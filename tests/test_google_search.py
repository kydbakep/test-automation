from src.pages.page_google import GoogleSearch as Google


class TestGoogleSearch:
    def test_google_search(self):
        google = Google()
        result = google.find('tobermory')
        assert 'Tobermory' in result
