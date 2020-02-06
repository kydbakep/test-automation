from selene.api import s, by, be, query
from selene.support.shared import browser


from src.helper.global_.selectors.sel_global_project import PRELOADER_SPINNER
from src.helper.warehouse.selectors.s_wh_residue import TABLE_BODY
from src.lib.lib_url import WH_RESIDUE_URL


class PageWarehouseResidue:
    def __init__(self, goods_name=None):
        self.__page_url = WH_RESIDUE_URL
        self.__preloader = s(PRELOADER_SPINNER)
        self.__residue_table = s(TABLE_BODY['table'])
        self.__residue_row = s(TABLE_BODY['row'])
        self.__goods_row = TABLE_BODY['row']
        if goods_name:
            self.__target_goods_row = by.xpath(TABLE_BODY['row_by_title'].format(name=goods_name))

    def __get_order_id(self):
        try:
            order_id = s(self.__target_goods_row).get(query.attribute(name='data-order-id'))
        except Exception as e:
            print('\nNo target goods initialized in class!')
            print(type(e))
            order_id = None
        return order_id

    @staticmethod
    def __get_checkbox_element_for_target_row(order_id):
        return f'label[for="residue_table-checkbox-{order_id}"]'

    def __assure_page_loaded(self, wait_time=4):
        self.__residue_table.should(be.visible, wait_time)
        self.__preloader.should(be.not_.visible)

    def open_page(self):
        browser.open(self.__page_url)
        self.__assure_page_loaded()

    def is_page_loaded(self):
        return self.__residue_table.matching(be.visible)

    def activate_checkbox(self):
        element = s(self.__get_checkbox_element_for_target_row(self.__get_order_id()))
        element.click()
