import pytest

import allure
from allure_commons.types import AttachmentType

from selene.support.shared import browser
from selenium.common.exceptions import WebDriverException

from settings.s_browser import Settings


class FixturesSettings:

    @pytest.fixture(scope='session', name='browser_settings', autouse=True)
    def set_browser_for_tests(self):
        Settings()
        yield
        try:
            import allure
            browser.quit()
        except WebDriverException:
            pass

    @pytest.fixture(scope='function', name='allure_screenshot')
    def make_screenshot_if_test_fails(self, request):
        state_before_test_runs = request.session.testsfailed
        yield
        failed = request.session.testsfailed - state_before_test_runs
        if failed:
            allure.attach(browser.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

