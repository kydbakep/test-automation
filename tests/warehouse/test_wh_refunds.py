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
        # sale goods here
        sales_page = PageSales()
        sales_page.open_page()
        sale_doc = sales_page.create_sale(goods_name=goods_for_sale['title'], quantity=goods_for_sale['quantity']-1)

        posting_page.open_page()
        posting_page.open_document(posting_doc)
        posting_page.open_refund_dialog()
        refunds_page = PageWarehousePostingRefunds()
        data = refunds_page._get_refund_goods_details(goods_for_check['title'])
        dialog_closed = refunds_page.close_dialog_by_button()
        assert dialog_closed
