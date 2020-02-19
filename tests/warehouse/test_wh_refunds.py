import pytest

from lib.auth.fixtures.f_browser import RegisterFixture
from lib.sales.pages.page_sales_core import PageSales
from lib.warehouse.pages.page_wh_core import PageWarehouse
from lib.warehouse.pages.page_wh_posting import PageWarehousePosting
from lib.warehouse.pages.page_wh_refunds import PageWarehousePostingRefunds


class TestWarehousePostingRefunds(RegisterFixture):

    @pytest.mark.s03t140
    def test_salt_goods_not_displayed_in_table(self):
        warehouse_page = PageWarehouse()
        warehouse_page.open_settings_tab()

        warehouse_page.open_posting_tab()
        posting_page = PageWarehousePosting()
        data = posting_page.create_random_posting(products=2)
        goods = data['goods']
        goods_for_sale = goods[0]
        goods_for_check = goods[1]
        posting_doc = data['label']

        sales_page = PageSales()
        sales_page.open_page()
        sales_page.create_sale(goods_name=goods_for_sale['title'], quantity=goods_for_sale['quantity'])

        posting_page.open_page()
        posting_page.open_document(posting_doc)
        posting_page.open_refund_dialog()

        refunds_page = PageWarehousePostingRefunds()
        products = refunds_page.get_available_goods_for_refund()
        is_passport_opened = refunds_page.open_supplier_card()
        is_passport_closed = refunds_page.close_supplier_card()
        is_dialog_closed = refunds_page.close_dialog_by_button()

        assert all([goods_for_check['title'] in products, not goods_for_sale['title'] in products,
                    is_passport_opened, is_passport_closed, is_dialog_closed])
