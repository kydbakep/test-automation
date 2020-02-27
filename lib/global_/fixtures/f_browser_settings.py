import pytest

from selene.support.shared import browser
from selenium.common.exceptions import WebDriverException

from settings.s_browser import Settings


class FixturesSettings:

    @pytest.fixture(scope='session', name='browser_settings', autouse=True)
    def set_browser_for_tests(self):
        Settings()
        yield
        try:
            browser.quit()
        except WebDriverException:
            pass
