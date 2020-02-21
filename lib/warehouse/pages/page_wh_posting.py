from selene.api import s, by, be
from selene.browser import driver
from selene.support.shared import browser
from selenium.webdriver import ActionChains

from lib.global_.helper.h_methods import get_fresh_document_label, PRELOADER_SPINNER, DIALOG_MASK_JS, \
    is_element_displayed
from lib.global_.selectors import NOTIFIES
from lib.url.lib_url import WH_POSTING_URL
from lib.warehouse.helper.h_wh_posting import WarehousePostingHelper
from lib.warehouse.pages.page_wh_core import PageWarehouse
from lib.warehouse.selectors.s_wh_posting import *
from lib.warehouse.selectors.s_wh_refunds import REFUND_DIALOG, REFUND_DIALOG_CLOSE_BUTTON
from lib.warehouse.test_data.td_wh_posting import get_random_goods_data, get_mixed_random_goods_data


class PageWarehousePosting(WarehousePostingHelper):
    warehouse_page = PageWarehouse()

    def __init__(self, page_url=None):
        super().__init__()
        if page_url:
            self.__page_url = page_url
        self._create_refund_dialog = s(REFUND_DIALOG)
        self.__page_url = WH_POSTING_URL
        self.__preloader = s(PRELOADER_SPINNER)
        self.__document = POSTING_DOCUMENT_LABEL_X
        self.__document_view_dialog = s(POSTING_VIEW_DIALOG)
        self.__document_close_button = s(POSTING_VIEW_DIALOG_CLOSE_BUTTON)
        self.__create_refund_button = CREATE_REFUND_BUTTON
        self.__close_refund_dialog_button = s(REFUND_DIALOG_CLOSE_BUTTON)
        self.__submit_button = s(POSTING_SUBMIT_BUTTON)
        self.__info_notifier = s(NOTIFIES['blue'])
        self.__dialog_mask_active = s(DIALOG_MASK_JS)

    def create_random_posting(self,
                              supplier=None,
                              stock: str = 'Склад',
                              serial: bool = False,
                              goods_qty: int = 1,
                              comment=None,
                              invoice=None,
                              category=None,  # Should be 'parts' or 'store'. Default: 'parts'
                              barcode=None,

                              mixed: bool = False,
                              # if mixed goods is True
                              normal_goods_qty: int = 1,
                              serial_goods_qty: int = 1,
                              serial_numbers_qty: int = None):

        if mixed:
            data = get_mixed_random_goods_data(serial_goods_qty=serial_goods_qty,
                                               normal_goods_qty=normal_goods_qty,
                                               numbers_qty=serial_numbers_qty)
        else:
            data = get_random_goods_data(serial=serial, quantity=goods_qty, numbers_qty=serial_numbers_qty)

        if supplier:
            data['supplier']['name'] = supplier
        if stock:
            data['stock'] = stock
        if comment:
            data.update(dict(comment=comment))
        if invoice:
            data.update(dict(invoice=invoice))
        if category:
            data['category'] = category

        self._open_create_posting_dialog()
        self._fill_posting_data(supplier=data['supplier']['name'], stock=data['stock'])
        for goods in data['goods']:
            self._add_document(product_data=goods)
        self.__submit_button.click().should(be.not_.visible)

        label = get_fresh_document_label()
        data.update({'label': label})

        return data

    def open_page(self):
        browser.open(self.__page_url)

    def open_document(self, label):
        sel = self.__document.format(label)
        target = s(by.xpath(sel))
        s(DIALOG_MASK_JS).should(be.not_.visible)
        target.should(be.clickable).click()
        self.__document_view_dialog.should(be.visible)
        return True

    def close_document_by_button(self):
        if is_element_displayed(self.__document_view_dialog):
            self.__document_close_button.should(be.visible).click()
        self.__document_view_dialog.should(be.not_.visible)
        return True

    def close_document_by_mask(self):
        if is_element_displayed(self.__document_view_dialog):
            self.__dialog_mask_active.should(be.visible).click()
        self.__document_view_dialog.should(be.not_.visible)
        return True

    def open_refund_dialog(self):
        element = s(self.__create_refund_button).should(be.clickable)()
        self.__click_by_chains(element)
        self._create_refund_dialog.should(be.visible)

    def close_refund_dialog(self):
        if is_element_displayed(self._create_refund_dialog):
            self.__close_refund_dialog_button.should(be.clickable).click()
        self._create_refund_dialog.should(be.not_.visible)
        return True

    @staticmethod
    def __click_by_chains(element):
        ActionChains(driver()).move_to_element(element).click().release().perform()
