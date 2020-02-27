from lib.auth.fixtures.f_browser import FixturesRegister
from lib.global_.fixtures.f_browser_settings import FixturesSettings
from lib.main.pages.page_main import PageMain


class TestAuth(FixturesSettings, FixturesRegister):

    def test_register(self, register, main=PageMain()):
        assert main.is_current_user(first_name=register['first_name'], last_name=register['last_name'])
