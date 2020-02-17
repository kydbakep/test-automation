from selene import Config
from selene.api import s, be, browser

from lib.auth.selectors.sel_auth_page import *
from lib.auth.test_data.td_registration import REGISTRATION_DATA
from lib.global_.helper.h_methods import set_select_option
from lib.url.lib_url import LOGIN_URL, REGISTRATION_URL
from settings.s_browser import Settings


class PageAuth(Settings):

    def __init__(self, login: str = None, password: str or int = None):
        super().__init__()
        self.login = login
        self.password = password
        self.__login_input = s(AUTH_LOGIN_INPUT)
        self.__email_input = s(AUTH_EMAIL_INPUT)
        self.__password_input = s(AUTH_PASSWORD_INPUT)
        self.__first_name_input = s(REGISTER_FIRST_NAME_INPUT)
        self.__last_name_input = s(REGISTER_LAST_NAME_INPUT)
        self.__company_name_input = s(REGISTER_COMPANY_NAME_INPUT)
        self.__country_select = REGISTER_COUNTRY_SELECT
        self.__city_input = s(REGISTER_CITY_INPUT)
        self.__phone_input = s(REGISTER_PHONE_INPUT)
        self.__template_select = REGISTER_TEMPLATE_SELECT
        self.__register_submit_button = s(REGISTRATION_SUBMIT_BUTTON)
        self.__submit_button = s(SUBMIT_BUTTON)

    def log_in(self, login: str = None, password: str or int = None):
        browser.open(LOGIN_URL)
        self.__login_input.should(be.visible).type(login or self.login)
        self.__password_input.should(be.visible).type(password or self.password)
        self.__submit_button.click()

    def register(self, login: str = None, password: str or int = None):
        browser.open(REGISTRATION_URL)
        self.__email_input.type(login or self.login)
        self.__password_input.should(be.visible).type(password or self.password)
        self.__submit_button.click()
        customer = self.__set_registration_data()
        self.__register_submit_button.click()
        self.__register_submit_button.with_(Config(timeout=10)).should(be.not_.visible)
        return customer

    def __set_registration_data(self):
        data = REGISTRATION_DATA
        first_name = data['first_name']
        last_name = data['last_name']
        self.__first_name_input.with_(Config(timeout=10)).should(be.visible).type(first_name)
        self.__last_name_input.type(last_name)
        self.__company_name_input.type(data['company_name'])
        set_select_option(browser.element(self.__country_select)(), data['country'])
        self.__city_input.set_value(data['city'])
        self.__phone_input.click().type(data['phone'])
        set_select_option(browser.element(self.__template_select)(), data['template'])
        return {'first_name': first_name, 'last_name': last_name}
