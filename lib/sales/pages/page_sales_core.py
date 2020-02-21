from selene.api import be
from selene.support.shared import browser

from lib.global_.helper.h_methods import get_fresh_document_label
from lib.main.selectors.sel_global_project import PRELOADER_SPINNER
from lib.sales.helper.h_sales import SalesHelper
from lib.sales.selectors.s_sales import *
from lib.url.lib_url import SALES_URL


class PageSales(SalesHelper):

    def __init__(self):
        super().__init__()
        self.__page_url = SALES_URL
        self.__preloader = s(PRELOADER_SPINNER)

    def open_page(self):
        browser.open(self.__page_url)
        self.__assure_page_loaded()

    def __assure_page_loaded(self, wait_time=4):
        self._sales_table.with_(timeout=wait_time).should(be.visible)
        self.__preloader.should(be.not_.visible)

    def __open_new_sale_dialog(self):
        self._sales_create_button.should(be.clickable).click()
        self._sales_create_dialog.should(be.visible)

    @staticmethod
    def __get_target_goods_dict_from_list(goods_list: list, target_title: str):
        for product in goods_list:
            if product.get('title') == target_title:
                return product

    def create_sale(self, goods: dict, quantity: int = 0, from_cell: str = ''):
        goods_title = goods['title']
        qty = quantity or goods['quantity']
        self.__open_new_sale_dialog()
        self._set_client()
        self._set_stock()
        self._set_product(goods_title)
        self._set_count(count=qty, cell_name=from_cell, serials=goods.get('serials'))
        self._save_sale()
        label = get_fresh_document_label()
        return label
