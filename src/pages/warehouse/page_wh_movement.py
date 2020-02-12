from selene.api import s, be
from selene.support.shared import browser

from src.helper.global_.h_methods import set_select_option
from src.helper.warehouse.selectors.s_wh_movement import *


class PageWarehouseMovement:

    def __init__(self):
        self.__select_move_from = MOVE_STOCK_FROM
        self.__select_move_to = MOVE_STOCK_TO
        self.__create_movement_button = s(ADD_NEW_MOVEMENT_BUTTON)
        self.__create_movement_dialog = s(CREATE_MOVEMENT_FRAME)
        self.__close_movement_dialog_button = s(CREATE_MOVEMENT_FRAME).s('.b-close')

    def open_movement_dialog(self):
        self.__create_movement_button.should(be.clickable).click()
        self.__create_movement_dialog.should(be.visible)
        return True

    def close_movement_dialog(self):
        element = self.__close_movement_dialog_button.click()
        element.should(be.not_.visible)
        return True

    def select_stock_from(self, stock_name):
        set_select_option(self.__select_move_from, stock_name)
        pass

    def select_stock_to(self, stock_name):
        set_select_option(self.__select_move_to, stock_name)
        pass

    def select_goods_from_dropdown(self, goods_name: str):
        pass

    def set_comment(self, comment_text: str):
        pass

    def finish(self):
        pass
