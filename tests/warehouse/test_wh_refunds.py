import pytest

from lib.auth.fixtures.f_browser import RegisterFixture
from lib.randomizer import get_random_int
from lib.warehouse.fixtures.f_wh_posting import FixturesWarehousePosting
from lib.warehouse.wh_suite import WarehousePages


class TestWarehousePostingRefunds(RegisterFixture, FixturesWarehousePosting):
    pages = WarehousePages()

    @pytest.mark.s03t054
    def test_open_close_refund(self, create_posting):
        self.pages.posting.open_document(create_posting['label'])
        closed_by_mask = self.pages.posting.close_document_by_mask()
        self.pages.posting.open_document(create_posting['label'])
        closed_by_button = self.pages.posting.close_document_by_button()

        assert all([closed_by_mask, closed_by_button])

    @pytest.mark.s03t140
    def test_salt_goods_not_displayed_in_table(self):
        self.pages.warehouse.open_settings_tab()
        self.pages.warehouse.open_posting_tab()

        data = self.pages.posting.create_random_posting(goods_qty=2)
        goods = data['goods']
        goods_for_sale = goods[0]
        goods_for_check = goods[1]
        posting_doc = data['label']

        self.pages.sales.open_page()
        self.pages.sales.create_sale(goods_name=goods_for_sale['title'], quantity=goods_for_sale['quantity'])

        self.pages.posting.open_page()
        self.pages.posting.open_document(posting_doc)
        self.pages.posting.open_refund_dialog()

        products = self.pages.refunds.get_available_goods_for_refund()
        is_passport_opened = self.pages.refunds.open_supplier_card()
        is_passport_closed = self.pages.refunds.close_supplier_card()
        is_dialog_closed = self.pages.refunds.close_refund_dialog_by_button()

        self.pages.posting.close_document_by_button()

        assert all([goods_for_check['title'] in products, not goods_for_sale['title'] in products,
                    is_passport_opened, is_passport_closed, is_dialog_closed])

    @pytest.mark.s03t141
    def test_edit_product_with_cells_enabled(self):
        self.pages.posting.open_page()
        data = self.pages.posting.create_random_posting(mixed=True, serial_numbers_qty=get_random_int(3, 7))
        goods = data['goods']
        label = data['label']

        self.pages.settings.open_page()
        self.pages.settings.enable_address_storage_usage()

        self.pages.posting.open_page()
        self.pages.posting.open_document(label)
        self.pages.posting.open_refund_dialog()

        can_be_edited_with_addressed_storage = self.pages.refunds.is_products_can_be_edited(goods)

        self.pages.posting.close_refund_dialog()
        self.pages.posting.close_document_by_button()
        assert can_be_edited_with_addressed_storage

    @pytest.mark.s03t141
    def test_edit_product_with_cells_disabled(self):
        self.pages.posting.open_page()
        data = self.pages.posting.create_random_posting(mixed=True, serial_numbers_qty=get_random_int(3, 7))
        goods = data['goods']
        label = data['label']

        self.pages.settings.open_page()
        self.pages.settings.disable_address_storage_usage()

        self.pages.posting.open_page()
        self.pages.posting.open_document(label)
        self.pages.posting.open_refund_dialog()

        can_be_edited_with_addressed_storage = self.pages.refunds.is_products_can_be_edited(goods)

        self.pages.posting.close_refund_dialog()
        self.pages.posting.close_document_by_button()
        assert can_be_edited_with_addressed_storage
