from selene.api import s, by, be

from lib.global_.helper.h_methods import set_select_option
from lib.sales.selectors.s_sales import SelectorsSales, Configured
from lib.sales.test_data.td_sales_core import DEFAULT_CLIENT_NAME


class SalesHelper(Configured):

    def __init__(self, client_name=DEFAULT_CLIENT_NAME, stock_name='Склад', cell_name='Ячейка 1'):
        __selectors = SelectorsSales

        super().__init__(cell_name)
        self.__client_name = client_name
        self.__stock_name = stock_name
        self._sales_table = s(__selectors.SALES_TABLE)
        self._sales_create_button = s(__selectors.SALES_CREATE_BUTTON)
        self._sales_create_dialog = s(__selectors.SALES_CREATE_DIALOG)
        self.__sales_dialog_client_input = s(__selectors.SALES_DIALOG_CLIENT_INPUT)
        self.__sales_dialog_product_input = s(__selectors.SALES_DIALOG_PRODUCT_INPUT)

        self.__sales_dialog_client_target = __selectors.SALES_DIALOG_DROPDOWN_CLIENT_ELEMENT_F
        self.__sales_dialog_product_target = __selectors.SALES_DIALOG_PRODUCT_DROPDOWN_ELEMENT_F

        self.__sales_dialog_description_input = s(__selectors.SALES_DIALOG_DESCRIPTION_INPUT)
        self.__sales_dialog_warehouse_select = s(__selectors.SALES_DIALOG_STOCK_SELECT)
        self.__sales_dialog_save_button = s(__selectors.SALES_DIALOG_SAVE_BUTTON)

        self.__sales_modal_frame = s(__selectors.SALES_MODAL_FRAME)
        self.__sales_modal_quantity_total_input = s(__selectors.SALES_MODAL_QUANTITY_TOTAL_INPUT)
        self.__sales_modal_quantity_single_input = s(__selectors.SALES_MODAL_QUANTITY_SINGLE_INPUT)
        self.__sales_modal_quantity_total_add_all_button = s(__selectors.SALES_MODAL_QUANTITY_TOTAL_ADD_ALL_BUTTON)
        self.__sales_modal_quantity_serial_add_all_button = s(__selectors.SALES_MODAL_QUANTITY_SERIAL_ADD_ALL_BUTTON)
        self.__sales_modal_serial_input = s(__selectors.SALES_MODAL_SERIAL_NUMBER_INPUT)
        self.__sales_modal_serial_label = __selectors.SALES_MODAL_SERIAL_NUMBER_LABEL_X_F

        self.__sales_modal_price_input = s(__selectors.SALES_MODAL_PRICE_INPUT)
        self.__sales_modal_discount_input = s(__selectors.SALES_MODAL_DISCOUNT_INPUT)
        self.__sales_modal_warranty_input = s(__selectors.SALES_MODAL_WARRANTY_INPUT)
        self.__sales_modal_save_button = s(__selectors.SALES_MODAL_SAVE_BUTTON)

        self.__sales_payment_dialog = s(__selectors.SALES_PAYMENT_DIALOG)
        self.__sales_payment_employee_select = s(__selectors.SALES_PAYMENT_EMPLOYEE_SELECT)
        self.__sales_payment_cashbox_select = s(__selectors.SALES_PAYMENT_CASHBOX_SELECT)
        self.__sales_payment_comment_input = s(__selectors.SALES_PAYMENT_COMMENT_INPUT)
        self.__sales_payment_submit_button = s(__selectors.SALES_PAYMENT_SUBMIT_BUTTON)

    def _set_client(self, client_name=None):
        client_input = self.__sales_dialog_client_input.should(be.visible)
        client_input.should(be.clickable).click()
        client_input.set_value(client_name or self.__client_name)
        target = by.xpath(self.__sales_dialog_client_target.format(client_name or self.__client_name))
        s(target).should(be.clickable).click()
        s(target).should(be.not_.visible)

    def _set_stock(self, stock_name=None):
        set_select_option(self.__sales_dialog_warehouse_select(), stock_name or self.__stock_name)

    def _set_count(self, count: int = 1, cell_name: str = None, serials: list = None):
        if cell_name and not serials:
            self._cell_quantity_input.set_value(count)
        else:
            if serials:
                self.__set_count_serial(count, serials)
            else:
                self.__set_count_not_serial(count)
        self.__sales_modal_save_button.should(be.clickable).click()
        self.__sales_modal_frame.should(be.not_.visible)

    def __set_count_not_serial(self, count):
        cnt_input = self.__sales_modal_quantity_single_input
        cnt_input.set_value(count)

    def __set_count_serial(self, count, serials: list):
        if count == len(serials):
            self.__sales_modal_quantity_serial_add_all_button.click()
            for num in serials:
                s(self.__sales_modal_serial_label.format(num)).should(be.visible)
        else:
            added_serials = []
            for _ in range(count):
                num = serials.pop(0)
                added_serials.append(num)
                self.__sales_modal_serial_input.set_value(num)
                s(self.__sales_modal_serial_label.format(num)).should(be.visible)

    def _set_goods(self, goods_name):
        self._set_product(product_name=goods_name)

    def _set_product(self, product_name):
        self.__sales_dialog_product_input.set_value(product_name)
        target = by.xpath(self.__sales_dialog_product_target.format(product_name))
        s(target).should(be.clickable).click()
        s(target).should(be.not_.visible)

    def _save_sale(self, employee: str = None, cashbox: str = None, comment: str = None):
        self.__sales_dialog_save_button.should(be.clickable).click()
        self._pay_for_sale(employee=employee, cashbox=cashbox, comment=comment)
        self._sales_create_dialog.should(be.not_.visible)

    def _pay_for_sale(self, employee: str = None, cashbox: str = None, comment: str = None):
        self.__sales_payment_dialog.should(be.visible)
        if employee:
            set_select_option(self.__sales_payment_employee_select(), employee)
        if cashbox:
            set_select_option(self.__sales_payment_cashbox_select(), cashbox)
        if comment:
            self.__sales_payment_comment_input.set_value(comment)
        self.__sales_payment_submit_button.should(be.clickable).click()
        self.__sales_payment_dialog.should(be.not_.visible)
