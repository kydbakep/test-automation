from selene.api import s, ss, by, be, query

from lib.global_.helper.h_methods import set_select_option, PRELOADER_SPINNER, is_element_displayed
from lib.randomizer import get_random_int, get_random_low_string
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
        self.__refund_goods_row = REFUND_TARGET_GOODS_ROW_F

        self.__refund_goods_edit_button = REFUND_GOODS_EDIT_BUTTON_X_F
        self.__refund_goods_edit_modal = s(REFUND_GOODS_EDIT_MODAL_X)
        self.__refund_goods_edit_modal_quantity_input = s(REFUND_GOODS_EDIT_MODAL_QUANTITY_SINGLE_INPUT)

        self.__refund_goods_edit_modal_serial_input = s(REFUND_GOODS_EDIT_MODAL_SERIAL_NUMBER_INPUT)
        self.__refund_goods_edit_modal_serial_dropdown = s(REFUND_GOODS_EDIT_MODAL_SERIAL_NUMBER_DROPDOWN)
        self.__refund_goods_edit_modal_serial_dropdown_item = REFUND_GOODS_EDIT_MODAL_SERIAL_NUMBER_ITEM_X_F
        self.__refund_goods_edit_modal_serial_label = REFUND_GOODS_EDIT_MODAL_SERIAL_NUMBER_LABEL_X_F
        self.__refund_goods_edit_modal_serial_total_count = s(REFUND_GOODS_EDIT_MODAL_SERIAL_ITEMS_TOTAL_COUNT)

        self.__refund_goods_edit_modal_price_input = s(REFUND_GOODS_EDIT_MODAL_PRICE_INPUT)
        self.__refund_goods_edit_modal_comment_input = s(REFUND_GOODS_EDIT_MODAL_COMMENT_INPUT)
        self.__refund_goods_edit_modal_add_all_button = s(REFUND_GOODS_EDIT_MODAL_ADD_ALL)
        self.__refund_goods_edit_modal_close_button = s(REFUND_GOODS_EDIT_MODAL_CLOSE_BUTTON)
        self.__refund_goods_edit_modal_save_button = s(REFUND_GOODS_EDIT_MODAL_SAVE_BUTTON)

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

    def _get_refund_goods_details(self, goods_name: str):
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

    def close_refund_dialog_by_button(self):
        self._create_refund_dialog.should(be.visible)
        self.__close_refund_dialog_button.should(be.clickable).click()
        self._create_refund_dialog.should(be.not_.visible)
        return True

    def open_product_edit_dialog(self, product_name: str):
        s(by.xpath(self.__refund_goods_row.format(product_name))).hover()
        s(by.xpath(self.__refund_goods_edit_button.format(product_name))).should(be.clickable).click()
        self.__refund_goods_edit_modal.should(be.visible)
        return True

    def save_product_edit_dialog(self):
        self.__refund_goods_edit_modal_save_button.should(be.visible).click()
        self.__refund_goods_edit_modal.should(be.not_.visible)
        return True

    def close_product_edit_dialog(self):
        self.__refund_goods_edit_modal_close_button.should(be.clickable).click()
        self.__refund_goods_edit_modal.should(be.not_.visible)
        return True

    def set_product_quantity(self, quantity: int, serials: list = None):
        if serials:
            added_serials = []
            for _ in range(quantity):
                num = serials.pop(0)
                added_serials.append(num)
                self.__refund_goods_edit_modal_serial_input.set_value(num)
                self.__refund_goods_edit_modal_serial_dropdown.should(be.visible)
                element = by.xpath(self.__refund_goods_edit_modal_serial_dropdown_item.format(num))
                s(element).should(be.clickable).click()
                s(self.__refund_goods_edit_modal_serial_label.format(num)).should(be.visible)
            is_set_correctly = int(self.__refund_goods_edit_modal_serial_total_count.get(query.value)) == quantity
        else:
            self.__refund_goods_edit_modal_quantity_input.set_value(quantity)
            val = int(self.__refund_goods_edit_modal_quantity_input.get(query.value))
            is_set_correctly = val == quantity
        return is_set_correctly

    def set_product_price(self, quantity: int):
        self.__refund_goods_edit_modal_price_input.set_value(quantity)
        val = int(self.__refund_goods_edit_modal_price_input.get(query.value))
        is_set_correctly = val == quantity
        return is_set_correctly

    def set_product_comment(self, comment: str):
        self.__refund_goods_edit_modal_comment_input.set_value(comment)
        val = self.__refund_goods_edit_modal_comment_input.get(query.value)
        is_set_correctly = val == comment
        return is_set_correctly

    def is_products_can_be_edited(self, products: list):
        can_be_edited = False
        for product in products:
            title = product['title']
            quantity = product['quantity']

            self.open_product_edit_dialog(product_name=title)
            if product.get('serials'):
                serials = product['serials']
                is_quantity_set = self.set_product_quantity(quantity - 1, serials=serials)
            else:
                is_quantity_set = self.set_product_quantity(quantity - 1)
            is_price_set = self.set_product_price(get_random_int(15, 999))
            is_comment_set = self.set_product_comment(get_random_low_string(20))
            if all([is_quantity_set, is_price_set, is_comment_set]) is True:
                can_be_edited = True
            else:
                can_be_edited = False
            self.close_product_edit_dialog()

        return can_be_edited

    def __set_stock(self, stock_name):
        set_select_option(self.__stock_select(), stock_name)
        s(PRELOADER_SPINNER).should(be.not_.visible)

    def __get_refund_goods_list(self):
        titles = []
        self.__refund_goods[0].should(be.visible)
        for product in self.__refund_goods:
            titles.append(product.should(be.visible).text)
        return titles
