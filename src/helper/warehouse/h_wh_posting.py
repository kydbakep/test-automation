from selene.api import s, be, by

from src.helper.global_.h_methods import is_element_displayed, set_select_option
from src.helper.warehouse.selectors.s_wh_posting import *


class WarehousePostingHelper:

    def __init__(self):
        self.__create_new_posting_dialog = s(POSTING_CREATE_DIALOG)
        self.__create_new_posting_button = s(POSTING_CREATE_NEW_BUTTON)
        self.__supplier_input = s(POSTING_SUPPLIER_INPUT)
        self.__supplier_dropdown_target = POSTING_SUPPLIER_DROPDOWN_TARGET_XPATH_F
        self.__add_new_client_plus_button = s(POSTING_ADD_NEW_CLIENT_PLUS_BUTTON)
        self.__add_new_client_dropdown_button = s(POSTING_ADD_NEW_CLIENT_DROPDOWN_BUTTON)
        self.__client_dialog = s(POSTING_CLIENT_DIALOG)
        self.__client_dialog_name_input = s(POSTING_CLIENT_DIALOG_NAME_INPUT)
        self.__client_dialog_submit_button = s(POSTING_CLIENT_DIALOG_SUBMIT_BUTTON)
        self.__warehouse_select = POSTING_WAREHOUSE_SELECT
        # product
        self.__name_input = s(POSTING_PRODUCT_NAME_INPUT)
        self.__new_product_area = s(POSTING_NEW_PRODUCT_AREA)
        self.__new_product_category_dropdown = s(POSTING_NEW_PRODUCT_CATEGORY_DROPDOWN)
        self.__new_product_category_parts = POSTING_NEW_PRODUCT_CATEGORY_TARGET_PARTS
        self.__new_product_category_store = POSTING_NEW_PRODUCT_CATEGORY_TARGET_STORE
        self.__new_product_category_custom = POSTING_NEW_PRODUCT_CATEGORY_TARGET_CUSTOM
        self.__new_product_is_serial_checkbox_input = s(POSTING_PRODUCT_IS_SERIAL_CHECKBOX_INPUT)()
        self.__new_product_is_serial_checkbox_label = s(POSTING_PRODUCT_IS_SERIAL_CHECKBOX_LABEL)

    def __add_document(self, product_data):
        self.__name_input.set_value(product_data['title']).press_tab()
        self.__new_product_area.should(be.visible)
        self.__set_product_category([product_data['category']])
        if product_data.get('serials'):
            self.__set_product_quantity(product_data['quantity'], serial=True)
        else:
            self.__set_product_quantity(product_data['quantity'], serial=False)

    def __open_create_posting_dialog(self):
        if not is_element_displayed(self.__create_new_posting_dialog, 0.1):
            self.__create_new_posting_button.should(be.clickable).click()
            self.__create_new_posting_dialog.should(be.visible)

    def __fill_posting_data(self, supplier, stock):
        self.set_supplier(supplier)
        set_select_option(s(self.__warehouse_select)(), stock)

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
        self.__add_new_client_dropdown_button.click()
        self.__client_dialog.should(be.visible)
        self.__client_dialog_name_input.set(supplier)
        if quick:
            self.__client_dialog_submit_button.click()
            self.__client_dialog.should(be.not_.visible)
        else:
            pass

    def set_supplier(self, supplier, quick=True):
        self.__supplier_input.should(be.clickable).type(supplier)
        target = by.xpath(self.__supplier_dropdown_target.format(supplier))
        if is_element_displayed(target):
            s(target).should(be.match.element_has_text(supplier)).click()
        else:
            self.__create_new_supplier(supplier, quick)

    def __set_product_quantity(self, quantity, serial=False):
        if serial:
            if not self.__new_product_is_serial_checkbox_input.is_selected():
                self.__new_product_is_serial_checkbox_label.click()
        else:
            pass
