from selene.api import s, ss, by, be

from lib.global_.helper.h_methods import set_select_option
from lib.sales.selectors.s_sales import SelectorsSales, Configured
from lib.sales.test_data.td_sales_core import DEFAULT_CLIENT_NAME


class SalesHelper(Configured):

    def __init__(self, client_name=DEFAULT_CLIENT_NAME, stock_name='Склад', cell_name='Ячейка 1'):
        __selectors = SelectorsSales

        super().__init__(cell_name)
        self.__client_name = client_name
        self.__stock_name = stock_name
        self._sales_table = s(__selectors.SALE_TABLE)
        self.__sales_create_button = s(__selectors.SALE_CREATE_BUTTON)
        self.__sales_create_dialog = s(__selectors.SALE_CREATE_DIALOG)
        self.__sales_dialog_client_input = s(__selectors.SALE_DIALOG_CLIENT_INPUT)
        self.__sales_dialog_product_input = s(__selectors.SALE_DIALOG_PRODUCT_INPUT)

        self.__sales_dialog_client_target = __selectors.SALE_DIALOG_DROPDOWN_CLIENT_ELEMENT_F
        self.__sales_dialog_product_target = __selectors.SALE_DIALOG_PRODUCT_DROPDOWN_ELEMENT_F

        self.__sales_dialog_description_input = s(__selectors.SALE_DIALOG_DESCRIPTION_INPUT)
        self.__sales_warehouse_select = s(__selectors.SALE_DIALOG_STOCK_SELECT)
        self.__sales_modal_frame = s(__selectors.SALE_MODAL_FRAME)
        self.__sales_modal_quantity_total_input = s(__selectors.SALE_MODAL_QUANTITY_TOTAL_INPUT)
        self.__sales_quantity_total_add_all_button = s(__selectors.SALE_MODAL_QUANTITY_TOTAL_ADD_ALL_BUTTON)
        self.__sales_modal_price_input = s(__selectors.SALE_MODAL_PRICE_INPUT)
        self.__sales_modal_discount_input = s(__selectors.SALE_MODAL_DISCOUNT_INPUT)
        self.__sales_modal_warranty_input = s(__selectors.SALE_MODAL_WARRANTY_INPUT)

    def _set_client(self, client_name=None):
        self.__sales_dialog_client_input.set_value(client_name or self.__client_name)
        target = by.xpath(self.__sales_dialog_client_target.format(client_name or self.__client_name))
        s(target).should(be.clickable).click()
        s(target).should(be.not_.visible)

    def _set_stock(self, stock_name=None):
        set_select_option(self.__sales_warehouse_select(), stock_name or self.__stock_name)

    def _set_count(self, count: int = 1, cell_name: str = None):
        if cell_name:
            self._cell_quantity_input.set_value(count)
        else:
            self.__sales_modal_quantity_total_input.set_value(count)

    def _set_goods(self, goods_name):
        self._set_product(product_name=goods_name)

    def _set_product(self, product_name):
        self.__sales_dialog_product_input.set_value(product_name)
        target = by.xpath(self.__sales_dialog_product_target.format(product_name))
        s(target).should(be.clickable).click()
        s(target).should(be.not_.visible)
        pass

