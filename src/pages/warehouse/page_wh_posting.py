from src.helper.warehouse.h_wh_posting import WarehousePostingHelper
from src.helper.warehouse.test_data.td_wh_posting import get_random_goods_data
from src.pages.warehouse.page_wh_core import PageWarehouse


class PageWarehousePosting(WarehousePostingHelper):
    warehouse_page = PageWarehouse()

    def __init__(self):
        super().__init__()

    def create_random_posting(self,
                              supplier=None,
                              stock=None,
                              serial=False,
                              quantity=1,
                              comment=None,
                              invoice=None,
                              category=None,  # Should be 'parts' or 'store'. Default: 'parts'
                              barcode=None):

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

        self.__open_create_posting_dialog()
        self.__fill_posting_data(data['supplier']['name'], data['stock'])
        for goods in data['goods']:
            self.__add_document(product_data=goods)
        return data
