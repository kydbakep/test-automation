from selene.api import s, by, be
from selene.support.shared import browser

from lib.global_.helper.h_methods import get_fresh_document_label
from lib.url.lib_url import WH_POSTING_URL
from lib.warehouse.helper.h_wh_posting import WarehousePostingHelper
from lib.warehouse.pages.page_wh_core import PageWarehouse
from lib.warehouse.selectors.s_wh_posting import *
from lib.warehouse.selectors.s_wh_refunds import REFUND_DIALOG
from lib.warehouse.test_data.td_wh_posting import get_random_goods_data, get_mixed_random_goods_data


class PageWarehousePosting(WarehousePostingHelper):
    warehouse_page = PageWarehouse()

    def __init__(self, page_url=None):
        super().__init__()
        self.__page_url = WH_POSTING_URL
        if page_url:
            self.__page_url = page_url
        self.__document = POSTING_DOCUMENT_LABEL_X
        self.__document_view_dialog = s(POSTING_VIEW_DIALOG)
        self.__create_refund_button = s(CREATE_REFUND_BUTTON)
        self._create_refund_dialog = s(REFUND_DIALOG)
        self.__submit_button = s(POSTING_SUBMIT_BUTTON)

    def create_random_posting(self,
                              supplier=None,
                              stock: str = 'Склад',
                              serial: bool = False,
                              products: int = 1,
                              comment=None,
                              invoice=None,
                              category=None,  # Should be 'parts' or 'store'. Default: 'parts'
                              barcode=None,
                              mixed: bool = False,
                              mixed_serials: int = 1,
                              mixed_normal: int = 1):

        if mixed:
            data = get_mixed_random_goods_data(serial_goods_qty=mixed_serials, normal_goods_qty=mixed_normal)
        else:
            data = get_random_goods_data(serial=serial, quantity=products)

        if supplier:
            data['supplier']['name'] = supplier
        if stock:
            data['stock'] = stock
        if comment:
            data.update({'comment': comment})
        if invoice:
            data.update({'invoice': invoice})
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
        s('.js-dialog-mask').should(be.not_.visible)
        target.should(be.clickable).click()
        self.__document_view_dialog.should(be.visible)
        return True

    def open_refund_dialog(self):
        self.__create_refund_button.should(be.clickable).click()
        self._create_refund_dialog.should(be.visible)
