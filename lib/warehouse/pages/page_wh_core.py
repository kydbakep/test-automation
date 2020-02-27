from selene.api import s, be
from selene.support.shared import browser

from lib.main.selectors.sel_global_project import PRELOADER_SPINNER
from lib.warehouse.selectors.s_wh_core import *
from lib.url.lib_url import WAREHOUSE_URL


class PageWarehouse:

    def __init__(self):
        self.__preloader = s(PRELOADER_SPINNER)
        self.__residue_tab = RESIDUE_TAB
        self.__posting_tab = POSTING_TAB
        self.__writeoff_tab = WRITEOFF_TAB
        self.__movements_tab = MOVE_TAB
        self.__stocktaking_tab = STOCKTAKING_TAB
        self.__supplier_refunds_tab = REFUNDS_TAB
        self.__settings_tab = SETTINGS_TAB
        self.__active_tab_prefix = ACTIVE_TAB_PREFIX
        self.tabs = (
            self.__residue_tab, self.__posting_tab, self.__writeoff_tab, self.__movements_tab,
            self.__stocktaking_tab, self.__supplier_refunds_tab, self.__settings_tab)

    def open_tab(self, tab_selector: str):
        browser.open(WAREHOUSE_URL)
        s(tab_selector).should(be.clickable).click()
        self.__preloader.should(be.not_.visible)
        s(self.__active_tab_prefix + tab_selector).should(be.visible)
        return True

    def open_residue_tab(self):
        self.open_tab(self.__residue_tab)

    def open_posting_tab(self):
        self.open_tab(self.__posting_tab)

    def open_writeoff_tab(self):
        self.open_tab(self.__writeoff_tab)

    def open_movements_tab(self):
        self.open_tab(self.__movements_tab)

    def open_refunds_tab(self):
        self.open_tab(self.__supplier_refunds_tab)

    def open_settings_tab(self):
        self.open_tab(self.__settings_tab)
