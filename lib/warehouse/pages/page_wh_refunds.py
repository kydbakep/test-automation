from selene.api import s, ss, by, be, query

from lib.global_.helper.h_methods import set_select_option, PRELOADER_SPINNER, is_element_displayed
from lib.warehouse.pages.page_wh_posting import PageWarehousePosting
from lib.warehouse.selectors.s_wh_refunds import *


class PageWarehousePostingRefunds(PageWarehousePosting):
    def __init__(self):
        super().__init__()

        self.__close_refund_dialog_button = s(REFUND_DIALOG_CLOSE_BUTTON)
        self.__document_row = s(REFUND_DOCUMENT_ROW_X)
        self.__supplier_row = s(REFUND_SUPPLIER_ROW_X)
        self.__supplier_passport_dialog = s(REFUND_DIALOG_SUPPLIER_PASSPORT)
        self.__supplier_passport_close_button = s(REFUND_DIALOG_SUPPLIER_PASSPORT_CLOSE_BUTTON)
        self.__stock_select = s(REFUND_STOCK_SELECTOR)
        self.__refund_goods = ss(REFUND_GOODS)
        self.__refund_product_curr_quantity = REFUND_GOODS_CURR_QUANTITY_X_F
        self.__refund_product_aval_quantity = REFUND_GOODS_AVAL_QUANTITY_X_F
        self.__refund_product_price = REFUND_GOODS_PRICE_X_F
        self.__refund_product_sum = REFUND_GOODS_SUM_X_F
        self.__refund_comment = s(REFUND_COMMENT)
        self.__make_refund_button = s(REFUND_SUBMIT_BUTTON)

    def get_available_goods_for_refund(self, stock_name: str = None):
        if stock_name:
            self.__set_stock(stock_name)
        titles = self.__get_refund_goods_list()
        return titles

    def _get_refund_goods_details(self, goods_name):
        curr_qty_sel = self.__refund_product_curr_quantity.format(goods_name)
        curr_quantity: int = s(by.xpath(curr_qty_sel)).get(query.value)
        aval_quantity: int = int(s(by.xpath(self.__refund_product_aval_quantity.format(goods_name))).get(query.text)
                                 .replace('/', '').strip())
        price: int = int(s(by.xpath(self.__refund_product_price.format(goods_name))).get(query.text))
        total_price: int = int(s(by.xpath(self.__refund_product_sum.format(goods_name))).get(query.text))
        comment: str = self.__refund_comment.get(query.value)

        data = dict(current_quantity=curr_quantity,
                    avaliable_quantity=aval_quantity,
                    price=price,
                    total_price=total_price,
                    comment=comment)
        return data

    def open_supplier_card(self):
        self.__supplier_row.s('a').click()
        self.__supplier_passport_dialog.should(be.visible)
        return True

    def close_supplier_card(self):
        if is_element_displayed(self.__supplier_passport_dialog):
            self.__supplier_passport_close_button.should(be.clickable).click()
        self.__supplier_passport_dialog.should(be.not_.visible)
        return True

    def close_dialog_by_button(self):
        self._create_refund_dialog.should(be.visible)
        self.__close_refund_dialog_button.should(be.clickable).click()
        self._create_refund_dialog.should(be.not_.visible)
        return True

    def __set_stock(self, stock_name):
        set_select_option(self.__stock_select(), stock_name)
        s(PRELOADER_SPINNER).should(be.not_.visible)

    def __get_refund_goods_list(self):
        titles = []
        self.__refund_goods[0].should(be.visible)
        for product in self.__refund_goods:
            titles.append(product.should(be.visible).text)
        return titles
