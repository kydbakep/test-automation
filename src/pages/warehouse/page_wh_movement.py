from selene.api import s, be
from selene.support.shared import browser

from src.helper.global_.h_methods import set_select_option
from src.helper.global_.selectors.sel_global_project import PRELOADER_SPINNER
from src.helper.warehouse.selectors.s_wh_movement import *
from src.lib.lib_url import WH_MOVE_URL


class PageWarehouseMovement:

    def __init__(self):
        self.__page_url = WH_MOVE_URL
        self.__movement_select_from = s(MOVEMENT_STOCK_FROM)
        self.__movement_select_to = s(MOVEMENT_STOCK_TO)
        self.__movement_name_input = s(MOVEMENT_NAME_INPUT)
        self.__movement_dropdown_element = MOVEMENT_DROPDOWN_TARGET
        # quantity
        self.__movement_quantity_modal = s(MOVEMENT_QUANTITY_MODAL)
        self.__movement_quantity_input = s(MOVEMENT_QUANTITY_MODAL_INPUT)
        self.__movement_quantity_add_all_button = s(MOVEMENT_QUANTITY_ADD_ALL_BUTTON)
        self.__movement_quantity_input_serial = s(MOVEMENT_QUANTITY_MODAL_INPUT_SERIAL)
        self.__movement_quantity_add_all_button_serial = s(MOVEMENT_QUANTITY_ADD_ALL_BUTTON_SERIAL)
        self.__serial_tag_f = '.b-tags__tag[data-tag-text="{}"]'

        self.__movement_create_button = s(MOVEMENT_ADD_NEW_BUTTON)
        self.__movement_create_dialog = s(MOVEMENT_CREATE_FRAME)
        self.__movement_close_dialog_button = s(MOVEMENT_CREATE_FRAME).s('.b-close')

    def open_page(self):
        browser.open(self.__page_url)
        self.__assure_page_loaded()

    def __assure_page_loaded(self, wait_time=4):
        self.__movement_create_button.should(be.visible, wait_time)
        s(PRELOADER_SPINNER).should(be.not_.visible)

    def open_movement_dialog(self):
        self.__movement_create_button.should(be.clickable).click()
        self.__movement_create_dialog.should(be.visible)
        return True

    def close_movement_dialog(self):
        element = self.__movement_close_dialog_button.click()
        element.should(be.not_.visible)
        return True

    def select_stock_from(self, stock_name):
        self.__movement_select_from.should(be.clickable)
        set_select_option(self.__movement_select_from(), stock_name)

    def select_stock_to(self, stock_name):
        self.__movement_select_to.should(be.clickable)
        set_select_option(self.__movement_select_to(), stock_name)

    def select_goods_from_dropdown(self, goods_name: str):
        self.__movement_name_input.should(be.visible).set_value(goods_name)
        target = by.xpath(self.__movement_dropdown_element.format(goods_name))
        s(target).should(be.clickable).click()

    def set_quantity(self, quantity: int, serials: list = None):
        """goods data used for get serial numbers if product is serial"""
        self.__movement_quantity_modal.should(be.visible)
        if serials:
            added_serials = []
            for _ in range(quantity):
                num = serials.pop(0)
                self.__movement_quantity_input_serial.type(num).press_tab()
                s(self.__serial_tag_f.format(num)).should(be.visible)
            return tuple(added_serials)
        else:
            self.__movement_quantity_input.should(be.clickable).set_value(quantity)

    def set_comment(self, comment_text: str):
        pass

    def finish(self):
        pass
