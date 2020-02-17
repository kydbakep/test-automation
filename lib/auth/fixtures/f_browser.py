import pytest
from selene.support.shared import browser

from src.helper.global_.randomizer import get_random_email, get_random_low_string
from src.pages.page_auth import PageAuth


class RegisterFixture:

    @staticmethod
    @pytest.fixture(scope='class', autouse=True)
    def register(auth=PageAuth()):
        email = get_random_email()
        password = get_random_low_string()
        try:
            customer = auth.register(email, password)
            yield {'first_name': customer['first_name'], 'last_name': customer['last_name']}
        except Exception as e:
            print(e)
        finally:
            browser.quit()
