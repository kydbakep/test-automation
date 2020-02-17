from selene.api import s, by, be, query
from selene.support.shared import browser

from lib.global_.helper.h_methods import set_select_option
from lib.main.selectors.sel_global_project import PRELOADER_SPINNER
from lib.url.lib_url import WH_RESIDUE_URL
from lib.warehouse.selectors.s_wh_residue import *


class PageWarehouseResidue:
    def __init__(self, goods_name=None):
        self.__page_url = WH_RESIDUE_URL
        self.__residue_table = s(TABLE_BODY['table'])
        self.__residue_row = s(TABLE_BODY['row'])
        self.__goods_row = TABLE_BODY['row']
        self.__target_row_f = TABLE_BODY['row_by_title']
        self.__target_goods_dialog_f = TARGET_GOODS_DIALOG_XPH_F
        self.__stock_select = s(WAREHOUSE_FILTER_SELECT)
        if goods_name:
            self.__target_goods_row = by.xpath(TABLE_BODY['row_by_title'].format(name=goods_name))

    def open_page(self):
        browser.open(self.__page_url)
        self.__assure_page_loaded()

    def __assure_page_loaded(self, wait_time=4):
        self.__residue_table.with_(timeout=wait_time).should(be.visible)
        s(PRELOADER_SPINNER).should(be.not_.visible)

    def is_page_loaded(self):
        is_loaded = self.__residue_table.matching(be.visible)
        return is_loaded

    def set_stock(self, stock_name):
        set_select_option(self.__stock_select(), stock_name)
        s(PRELOADER_SPINNER).should(be.not_.visible)

    def set_warehouse(self, wh_name):
        self.set_stock(wh_name)

    def product_row_set_checkbox(self):
        element = s(self.__get_checkbox_element_for_target_row(self.__get_order_id()))
        element.click()

    def product_row_join(self, product_name):
        element = s(by.xpath(self.__target_row_f.format(product_name)))
        element.double_click()
        s(by.xpath(self.__target_goods_dialog_f.format(product_name))).should(be.visible)

    def __get_order_id(self):
        order_id = None
        try:
            order_id = s(self.__target_goods_row).get(query.attribute(name='data-order-id'))
        except Exception as e:
            print('\nNo target goods initialized in class!')
            print(type(e))
        return order_id

    @staticmethod
    def __get_checkbox_element_for_target_row(order_id):
        element_selector = f'label[for="residue_table-checkbox-{order_id}"]'
        return element_selector

    def get_current_residue(self, product_name: str, stock_name: str = None):
        if stock_name:
            self.set_stock(stock_name)
        row_sel = self.__target_row_f.format(product_name)
        residue_sel = row_sel + '/div[@data-body-cell="residue"]'
        residue = s(by.xpath(residue_sel)).should(be.visible).get(query.text)
        return int(residue)
