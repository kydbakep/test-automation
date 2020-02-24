import pytest

from lib.auth.fixtures.f_browser import RegisterFixture
from lib.randomizer import get_random_int
from lib.sales.pages.page_sales_core import PageSales
from lib.settings.pages.page_settings_core import PageSettings
from lib.warehouse.pages.page_wh_core import PageWarehouse
from lib.warehouse.pages.page_wh_posting import PageWarehousePosting
from lib.warehouse.pages.page_wh_refunds import PageWarehousePostingRefunds


@pytest.mark.warehouse
class TestWarehousePostingRefunds(RegisterFixture):
    sales = PageSales()
    settings = PageSettings()
    warehouse = PageWarehouse()
    posting = PageWarehousePosting()
    refunds = PageWarehousePostingRefunds()

    @pytest.mark.s03t140
    def test_salt_goods_not_displayed_in_table(self):
        self.warehouse.open_settings_tab()
        self.warehouse.open_posting_tab()

        data = self.posting.create_random_posting(goods_qty=2)
        goods = data['goods']
        goods_for_sale = goods[0]
        goods_for_check = goods[1]
        posting_doc = data['label']

        self.sales.open_page()
        self.sales.create_sale(goods_name=goods_for_sale['title'], quantity=goods_for_sale['quantity'])

        self.posting.open_page()
        self.posting.open_document(posting_doc)
        self.posting.open_refund_dialog()

        products = self.refunds.get_available_goods_for_refund()
        is_passport_opened = self.refunds.open_supplier_card()
        is_passport_closed = self.refunds.close_supplier_card()
        is_dialog_closed = self.refunds.close_refund_dialog_by_button()

        self.posting.close_document()

        assert all([goods_for_check['title'] in products, not goods_for_sale['title'] in products,
                    is_passport_opened, is_passport_closed, is_dialog_closed])

    @pytest.mark.s03t141
    def test_edit_product_with_cells_enabled(self):
        self.posting.open_page()
        data = self.posting.create_random_posting(mixed=True, serial_numbers_qty=get_random_int(3, 7))
        goods = data['goods']
        label = data['label']

        self.settings.open_page()
        self.settings.enable_address_storage_usage()

        self.posting.open_page()
        self.posting.open_document(label)
        self.posting.open_refund_dialog()

        can_be_edited_with_addressed_storage = self.refunds.is_products_can_be_edited(goods)

        self.posting.close_refund_dialog()
        self.posting.close_document()
        assert can_be_edited_with_addressed_storage

    @pytest.mark.s03t141
    def test_edit_product_with_cells_disabled(self):
        self.posting.open_page()
        data = self.posting.create_random_posting(mixed=True, serial_numbers_qty=get_random_int(3, 7))
        goods = data['goods']
        label = data['label']

        self.settings.open_page()
        self.settings.disable_address_storage_usage()

        self.posting.open_page()
        self.posting.open_document(label)
        self.posting.open_refund_dialog()

        can_be_edited_with_addressed_storage = self.refunds.is_products_can_be_edited(goods)

        self.posting.close_refund_dialog()
        self.posting.close_document()
        assert can_be_edited_with_addressed_storage
