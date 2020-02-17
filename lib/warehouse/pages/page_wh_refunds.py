from selene.api import s, be

from lib.warehouse.pages.page_wh_posting import PageWarehousePosting
from lib.warehouse.selectors.s_wh_refunds import *


class PageWarehousePostingRefunds(PageWarehousePosting):
    def __init__(self):
        super().__init__()

        self.__close_refund_dialog_button = s(REFUND_DIALOG_CLOSE_BUTTON)
        self.__make_refund_button = s(REFUND_SUBMIT_BUTTON)

    def close_dialog_by_button(self):
        self._create_refund_dialog.should(be.visible)
        self.__close_refund_dialog_button.should(be.clickable).click()
        self._create_refund_dialog.should(be.not_.visible)
        return True
