from selene.api import s, by
from selene.browser import open_url
from selene.support.conditions.be import visible, in_dom

from settings.s_browser import Settings
from src.helper.global_.global_helper import set_select_option
from src.helper.global_.test_data.data_registration import REGISTRATION_DATA
from src.lib.lib_url import LOGIN_URL, REGISTRATION_URL
from src.helper.global_.selectors.sel_auth_page import *


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
        self.__country_select = s(REGISTER_COUNTRY_SELECT)
        self.__city_input = s(REGISTER_CITY_INPUT)
        self.__phone_input = s(REGISTER_PHONE_INPUT)
        self.__template_select = s(REGISTER_TEMPLATE_SELECT)
        self.__register_submit_button = s(REGISTRATION_SUBMIT_BUTTON)
        self.__submit_button = s(SUBMIT_BUTTON)

    def log_in(self, login: str = None, password: str or int = None):
        open_url(LOGIN_URL)
        self.__login_input.should_be(visible).set(login or self.login)
        self.__password_input.should_be(visible).set(password or self.password)
        self.__submit_button.click()

    def register(self, login: str = None, password: str or int = None):
        open_url(REGISTRATION_URL)
        self.__email_input.set(login or self.login)
        self.__password_input.should_be(visible).set(password or self.password)
        self.__submit_button.click()
        customer = self.__set_registration_data()
        self.__register_submit_button.click()
        return customer

    def __set_registration_data(self):
        data = REGISTRATION_DATA
        first_name = data['first_name']
        last_name = data['last_name']
        self.__first_name_input.should_be(visible, 10).set(first_name)
        self.__last_name_input.set(last_name)
        self.__company_name_input.set(data['company_name'])
        set_select_option(self.__country_select.get_actual_webelement(), data['country'])
        self.__city_input.set(data['city'])
        self.__phone_input.click().send_keys(data['phone'])
        set_select_option(self.__template_select.get_actual_webelement(), data['template'])
        return {'first_name': first_name, 'last_name': last_name}
