import pytest
from selene.support.shared import browser

from settings.s_browser import get_default_url


class FixturesHelper:

    @pytest.fixture(scope='module')
    def remonline_start_page(self):
        browser.open(get_default_url())

    @pytest.fixture(scope='module')
    def google_page(self):
        browser.open('http://google.com')
