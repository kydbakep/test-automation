from selene.api import s, be
from selene.core.entity import SeleneElement
from selene.support.shared import browser

from src.helper.global_.selectors.sel_global_project import PRELOADER_SPINNER
from src.helper.warehouse.selectors.s_wh_core import *
from src.lib.lib_url import WAREHOUSE_URL


class PageWarehouse:

    def __init__(self):
        self.__preloader = s(PRELOADER_SPINNER)
        self.__residue_tab = s(RESIDUE_TAB)
        self.__posting_tab = s(POSTING_TAB)
        self.__writeoff_tab = s(WRITEOFF_TAB)
        self.__movements_tab = s(MOVE_TAB)
        self.__supplier_refunds_tab = s(REFUNDS_TAB)
        self.__settings_tab = s(SETTINGS_TAB)

    def __open_tab(self, tab_element: SeleneElement):
        browser.open(WAREHOUSE_URL)
        tab_element.should(be.clickable).click()
        self.__preloader.should(be.not_.visible)

    def open_residue_tab(self):
        self.__open_tab(self.__residue_tab)

    def open_posting_tab(self):
        self.__open_tab(self.__posting_tab)

    def open_writeoff_tab(self):
        self.__open_tab(self.__writeoff_tab)

    def open_movements_tab(self):
        self.__open_tab(self.__movements_tab)

    def open_refunds_tab(self):
        self.__open_tab(self.__supplier_refunds_tab)

    def open_settings_tab(self):
        self.__open_tab(self.__settings_tab)
