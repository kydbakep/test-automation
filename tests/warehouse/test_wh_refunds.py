from lib.auth.fixtures.f_browser import RegisterFixture
from lib.warehouse.pages.page_wh_core import PageWarehouse
from lib.warehouse.pages.page_wh_posting import PageWarehousePosting
from lib.warehouse.pages.page_wh_refunds import PageWarehousePostingRefunds


class TestWarehousePostingRefunds(RegisterFixture):

    def test_x(self):
        warehouse_page = PageWarehouse()
        warehouse_page.open_settings_tab()

        warehouse_page.open_posting_tab()
        posting_page = PageWarehousePosting()
        data = posting_page.create_random_posting()
        goods = data['goods'][0]
        label = data['label']
        posting_page.open_document(label)
        posting_page.open_refund_dialog()

        refunds_page = PageWarehousePostingRefunds()
        dialog_closed = refunds_page.close_dialog_by_button()
        assert dialog_closed
