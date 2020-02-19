from selene.api import s, be
from selene.support.shared import browser

from lib.main.selectors.sel_global_project import PRELOADER_SPINNER
from lib.settings.selectors.s_settings_general import ADDRESS_STORAGE_CHECKBOX_SPAN, ADDRESS_STORAGE_CHECKBOX_INPUT
from lib.url.lib_url import *


class PageSettings:
    def __init__(self):
        self.__page_url = SETTINGS_COMMON_URL
        self.__general_url = SETTINGS_GENERAL_URL
        self.__general_address_storage_checkbox_span = s(ADDRESS_STORAGE_CHECKBOX_SPAN)
        self.__general_address_storage_checkbox_input = s(ADDRESS_STORAGE_CHECKBOX_INPUT)
        self.__settings_branch_url = SETTINGS_BRANCH_URL
        self.__settings_locations_url = SETTINGS_BRANCH_URL
        self.__settings_employee_url = SETTINGS_EMPLOYEE_URL
        self.__settings_status_url = SETTINGS_STATUS_URL
        self.__settings_tags_url = SETTINGS_TAGS_URL
        self.__settings_notifications_url = SETTINGS_NOTIFICATIONS_URL
        self.__settings_services_url = SETTINGS_SERVICES_URL
        self.__settings_book_url = SETTINGS_BOOK_URL
        self.__settings_form_editor_url = SETTINGS_FORM_EDITOR_URL
        self.__settings_templates_url = SETTINGS_TEMPLATES_URL
        self.__settings_price_and_discount_url = SETTINGS_PRICE_AND_DISCOUNT_URL
        self.__settings_marketing_url = SETTINGS_MARKETING_URL
        self.__settings_integrations_url = SETTINGS_INTEGRATIONS_URL
        self.__settings_api_url = SETTINGS_API_URL
        self.__settings_license_url = SETTINGS_LICENSE_URL
        self.__settings_referrals_url = SETTINGS_REFERRALS_URL
        self.__settings_partners_url = SETTINGS_REFERRALS_URL

    def open_page(self):
        browser.open(self.__page_url)
        self.__assure_page_loaded()

    def __assure_page_loaded(self, wait_time=4):
        self.__get_element_from_url(self.__general_url).with_(timeout=wait_time).should(be.visible)
        s(PRELOADER_SPINNER).should(be.not_.visible)

    @staticmethod
    def __get_element_from_url(url_: str):
        element = s(f'a[href={url_}]')
        return element

    def _open_tab_using_element(self, url_: str):
        self.__get_element_from_url(url_).should(be.clickable).click()

    @staticmethod
    def _open_tab_using_url(url_: str):
        browser.get(url_)

    def enable_address_storage_use(self):
        self._open_tab_using_element(self.__general_url)

