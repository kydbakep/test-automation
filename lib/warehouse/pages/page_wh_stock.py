from selene.api import s, be
from selene.support.shared import browser

from lib.main.selectors.sel_global_project import DIALOG_MASK_H, PRELOADER_SPINNER
from lib.randomizer import get_random_stock_name
from lib.url.lib_url import WAREHOUSE_URL
from lib.warehouse.helper.h_wh_stock import WarehouseStockHelper
from lib.warehouse.selectors.s_wh_stock import *


class PageWarehouseStock(WarehouseStockHelper):

    def __init__(self):
        self.default_stock = 'Склад'
        self.__page_url = WAREHOUSE_URL
        self.__dialog_mask = s(DIALOG_MASK_H)
        self.__stock_create_button = s(STOCK_CREATE_BUTTON)
        self.__stock_edit_button = s(STOCK_EDIT_BUTTON)
        self.__stock_delete_button = s(STOCK_DELETE_BUTTON)
        self.__stock_creation_dialog = s(STOCK_CREATE_DIALOG)
        self.__stock_title_input = s(STOCK_CREATE_TITLE_INPUT)
        self.__stock_radio_local = s(STOCK_CREATE_RADIO_BUTTON_LOCAL)
        self.__stock_radio_global = s(STOCK_CREATE_RADIO_BUTTON_GLOBAL)
        self.__stock_save_button = s(STOCK_SAVE_BUTTON)

        self.__category_create_button = s(STOCK_CREATE_CATEGORY_BUTTON)
        self.__category_edit_button = s(STOCK_EDIT_CATEGORY_BUTTON)
        self.__category_delete_button = s(STOCK_DELETE_CATEGORY_BUTTON)
        self.__category_creation_dialog = s(STOCK_CREATE_CATEGORY_DIALOG)

    def open_page(self):
        browser.open(self.__page_url)
        self.__assure_page_loaded()

    def __assure_page_loaded(self, wait_time=4):
        self.__stock_create_button.with_(timeout=wait_time).should(be.visible)
        s(PRELOADER_SPINNER).should(be.not_.visible)

    def __create_stock(self, name=None, local=True, finish=True):
        stock_name = name or get_random_stock_name()
        self.__dialog_mask.should(be.not_.visible)
        self.__stock_create_button.should(be.clickable).click()
        self.__stock_creation_dialog.should(be.visible)
        self.__stock_title_input.type(stock_name)
        if local:
            self.__stock_radio_local.click()
        else:
            self.__stock_radio_global.click()
        self.__save_stock_dialog(finish)
        return stock_name

    def __save_stock_dialog(self, finish=True):
        self.__stock_save_button.click()
        if finish:
            self.__stock_creation_dialog.with_(timeout=10).should(be.not_.visible)

    def create_local_stock(self, name=None, finish=True):
        return self.__create_stock(name=name, local=True, finish=finish)

    def create_global_stock(self, name=None, finish=True):
        return self.__create_stock(name=name, local=False, finish=finish)
