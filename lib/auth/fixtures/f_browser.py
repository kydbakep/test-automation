import pytest

from lib.auth.pages.page_auth import PageAuth
from lib.randomizer import get_random_email, get_random_low_string


class FixturesRegister:

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
