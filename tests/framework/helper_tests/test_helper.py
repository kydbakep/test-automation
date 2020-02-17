import pytest
from selene.api import by, s, ss, browser
from selenium.common.exceptions import NoSuchElementException

from lib.global_.helper.h_methods import is_element_displayed
from settings.s_browser import get_default_url


@pytest.mark.tests_for_helper
class TestHelperMethods:

    @pytest.fixture(scope='session')
    def remonline_start_page(self):
        browser.open(get_default_url())

    @pytest.fixture(scope='session')
    def google_page(self):
        browser.open('http://google.com')

    FIELD_ID = 'l-auth-login'
    ELEMENTS = {'css': f'#{FIELD_ID}',
                'xpath': f"//input[@id='{FIELD_ID}']",
                'selenium_element': 'web_element',
                'selene_element': s(f'#{FIELD_ID}'),
                'selene_collection': ss(f'#{FIELD_ID}'),
                'by': by.xpath(f"//input[@id='{FIELD_ID}']")}

    @pytest.mark.parametrize('field_type', ELEMENTS)
    def test_is_element_displayed(self, remonline_start_page, field_type):
        field = self.ELEMENTS[field_type]
        if field == 'web_element':
            field = s(f'#{self.FIELD_ID}')
        assert is_element_displayed(field, timeout=4)

    @pytest.mark.parametrize('field_type', ELEMENTS)
    def test_is_element_not_displayed(self, google_page, field_type):
        field = self.ELEMENTS[field_type]
        if field == 'web_element':
            try:
                field = s(f'#{self.FIELD_ID}')
            except NoSuchElementException:
                field = None
        assert not is_element_displayed(field, 0.5)
