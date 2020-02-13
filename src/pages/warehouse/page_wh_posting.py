from selene.api import s, be
from selene.support.shared import browser

from src.helper.global_.h_methods import get_fresh_document_label
from src.helper.warehouse.h_wh_posting import WarehousePostingHelper
from src.helper.warehouse.selectors.s_wh_posting import POSTING_SUBMIT_BUTTON
from src.helper.warehouse.test_data.td_wh_posting import get_random_goods_data, get_mixed_random_goods_data
from src.pages.warehouse.page_wh_core import PageWarehouse
from src.lib.lib_url import WH_POSTING_URL


class PageWarehousePosting(WarehousePostingHelper):
    warehouse_page = PageWarehouse()

    def __init__(self):
        super().__init__()
        self.url = WH_POSTING_URL
        self.__submit_button = s(POSTING_SUBMIT_BUTTON)

    def create_random_posting(self,
                              supplier=None,
                              stock=None,
                              serial=False,
                              quantity=1,
                              comment=None,
                              invoice=None,
                              category=None,  # Should be 'parts' or 'store'. Default: 'parts'
                              barcode=None,
                              mixed=False,
                              mixed_serials=1,
                              mixed_normal=1):

        if mixed:
            data = get_mixed_random_goods_data(serial_goods_qty=mixed_serials, normal_goods_qty=mixed_normal)
        else:
            data = get_random_goods_data(serial=serial, quantity=quantity)

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
        browser.open(self.url)
