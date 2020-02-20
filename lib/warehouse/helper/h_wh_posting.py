from selene.api import s, ss, be, by

from lib.global_.helper.h_methods import is_element_displayed, set_select_option
from lib.warehouse.selectors.s_wh_posting import *


class WarehousePostingHelper:

    def __init__(self):
        self.__create_new_posting_dialog = s(POSTING_CREATE_DIALOG_FACE)
        self.__create_new_posting_button = s(POSTING_CREATE_NEW_BUTTON)
        # SUPPLIER
        self.__supplier_input = s(POSTING_SUPPLIER_INPUT)
        self.__supplier_dropdown_target = POSTING_SUPPLIER_DROPDOWN_TARGET_X_F
        # new client
        self.__add_new_client_plus_button = s(POSTING_ADD_NEW_CLIENT_PLUS_BUTTON)
        self.__add_new_client_dropdown_button = s(POSTING_ADD_NEW_CLIENT_DROPDOWN_BUTTON)
        self.__client_dialog = s(POSTING_CLIENT_DIALOG)
        self.__client_dialog_name_input = s(POSTING_CLIENT_DIALOG_NAME_INPUT)
        self.__client_dialog_submit_button = s(POSTING_CLIENT_DIALOG_SUBMIT_BUTTON)
        # WAREHOUSE
        self.__warehouse_select = POSTING_WAREHOUSE_SELECT
        # PRODUCT
        self.__name_input = s(POSTING_PRODUCT_NAME_INPUT)
        self.__new_product_area = s(POSTING_NEW_PRODUCT_AREA)
        self.__new_product_category_dropdown = s(POSTING_NEW_PRODUCT_CATEGORY_DROPDOWN)
        self.__new_product_category_parts = POSTING_NEW_PRODUCT_CATEGORY_TARGET_PARTS
        self.__new_product_category_store = POSTING_NEW_PRODUCT_CATEGORY_TARGET_STORE
        self.__new_product_category_custom = POSTING_NEW_PRODUCT_CATEGORY_TARGET_CUSTOM
        self.__new_product_quantity_input = s(POSTING_NEW_PRODUCT_QUANTITY_INPUT)
        self.__new_product_add_button = s(POSTING_NEW_PRODUCT_ADD_BUTTON)
        # price
        self.__new_product_price_purchase_input = s(POSTING_NEW_PRODUCT_PRICE_PURCHASE_INPUT)
        self.__new_product_price_zero_input = s(POSTING_NEW_PRODUCT_PRICE_ZERO_INPUT)
        self.__new_product_price_repair_input = s(POSTING_NEW_PRODUCT_PRICE_REPAIR_INPUT)
        self.__new_product_price_retail_input = s(POSTING_NEW_PRODUCT_PRICE_RETAIL_INPUT)
        # serial
        self.__new_product_is_serial_checkbox_input = s(POSTING_NEW_PRODUCT_IS_SERIAL_CHECKBOX_INPUT)
        self.__new_product_is_serial_checkbox_label = s(POSTING_NEW_PRODUCT_IS_SERIAL_CHECKBOX_LABEL)
        self.__serial_numbers_frame = s(POSTING_NEW_PRODUCT_SERIAL_NUMBERS_FRAME)
        self.__serial_number_input = s(POSTING_NEW_PRODUCT_SERIAL_NUMBERS_INPUT)
        self.__serial_number_added = POSTING_NEW_PRODUCT_SERIAL_NUMBERS_ADDED_NUMBER_F
        # VIEW
        self._posting_view_product_title = s(POSTING_VIEW_PRODUCT_TITLE)
        self._posting_view_product_titles = ss(POSTING_VIEW_PRODUCT_TITLE)

    def set_supplier(self, supplier, quick=True):
        # for now, supplier is supplier name. In future, it be dict with enhanced data
        self.__supplier_input.should(be.clickable).type(supplier)
        target = by.xpath(self.__supplier_dropdown_target.format(supplier))
        if is_element_displayed(target):
            s(target).should(be.match.element_has_text(supplier)).click()
        else:
            self.__create_new_supplier(supplier, quick)

    def _open_create_posting_dialog(self):
        if not is_element_displayed(self.__create_new_posting_dialog, 0.1):
            self.__create_new_posting_button.should(be.clickable).click()
            self.__create_new_posting_dialog.should(be.visible)

    def _fill_posting_data(self, supplier: str, stock: str):
        self.set_supplier(supplier)
        set_select_option(s(self.__warehouse_select)(), stock)

    def _add_document(self, product_data: dict):
        """ method for adding new product to posting """
        self.__name_input.set_value(product_data['title']).press_tab()
        self.__new_product_area.should(be.visible)
        self.__set_product_category(product_data['category'])
        if product_data.get('serials'):
            self.__set_product_quantity(product_data['quantity'], serial_numbers=product_data['serials'])
        else:
            self.__set_product_quantity(product_data['quantity'], serial_numbers=None)

        purchase_price = product_data['price']
        self.__set_product_price(purchase=purchase_price)
        self.__new_product_add_button.should(be.clickable).click()

    def __set_product_price(self, purchase, zero=0, repair=0, retail=0):
        self.__new_product_price_purchase_input.should(be.clickable).click().set_value(purchase)
        if zero:
            self.__new_product_price_zero_input.set_value(zero)
        if repair:
            self.__new_product_price_repair_input.set_value(repair)
        if retail:
            self.__new_product_price_retail_input.set_value(retail)

    def __set_product_category(self, category):
        self.__new_product_category_dropdown.should(be.clickable).click()
        target_category = self.__get_product_category_element(category)
        target_category.should(be.clickable).click()

    def __get_product_category_element(self, category_name):
        if category_name == 'parts':
            target_category_element = s(self.__new_product_category_parts)
        elif category_name == 'store':
            target_category_element = s(self.__new_product_category_store)
        else:
            target_category_element = s(self.__new_product_category_custom.format(category_name))
        return target_category_element

    def __create_new_supplier(self, supplier, quick=True):
        # for now, supplier is supplier name. In future, it be dict with enhanced data
        self.__add_new_client_dropdown_button.click()
        self.__client_dialog.should(be.visible)
        self.__client_dialog_name_input.set_value(supplier)
        if quick:
            self.__client_dialog_submit_button.click()
            self.__client_dialog.should(be.not_.visible)
        else:
            # todo: get data from 'supplier' dict and fill all needed fields
            pass

    def __add_serial_numbers(self, serial_numbers: list):
        added_numbers = []
        for i in range(len(serial_numbers)):
            serial_for_adding = serial_numbers[i]
            added_numbers.append(serial_for_adding)
            self.__serial_number_input.should(be.visible).type(serial_for_adding).press_tab()
            s(self.__serial_number_added.format(serial_for_adding)).should(be.visible)
        return added_numbers

    def __set_product_quantity(self, quantity: int, serial_numbers: list or None):
        if serial_numbers:
            if not self.__new_product_is_serial_checkbox_input().is_selected():
                self.__new_product_is_serial_checkbox_label.click()
                self.__serial_numbers_frame.should(be.visible)
                added_numbers = self.__add_serial_numbers(serial_numbers)
                return added_numbers
        else:
            self.__new_product_quantity_input.set_value(quantity)
