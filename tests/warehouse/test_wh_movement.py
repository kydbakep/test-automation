import pytest
from src.helper.global_.fixtures.f_browser import RegisterFixture
from src.pages.warehouse.page_wh_core import PageWarehouse
from src.pages.warehouse.page_wh_movement import PageWarehouseMovement
from src.pages.warehouse.page_wh_posting import PageWarehousePosting
from src.pages.warehouse.page_wh_residue import PageWarehouseResidue
from src.pages.warehouse.page_wh_stock import PageWarehouseStock


class TestWarehouseMovement(RegisterFixture):

    @pytest.mark.s03t131
    def test_movement_open_close_dialog(self):
        warehouse_page = PageWarehouse()
        warehouse_page.open_movements_tab()

        movement_page = PageWarehouseMovement()
        opened = movement_page.open_movement_dialog()
        closed = movement_page.close_movement_dialog()

        assert all([opened, closed])

    @pytest.mark.s03t132
    def test_create_movement(self):
        stock_page = PageWarehouseStock()
        default_stock = stock_page.get_default_stock()
        new_stock = stock_page.create_local_stock()

        posting_page = PageWarehousePosting()
        goods = posting_page.create_random_posting(stock=default_stock)

        movement_page = PageWarehouseMovement()
        movement_page.select_stock_from(default_stock)
        movement_page.select_stock_to(new_stock)
        movement_page.select_goods_from_dropdown(goods_name=goods['name'])
        movement_page.finish()

        residue_page = PageWarehouseResidue()
        residue = residue_page.get_current_residue(goods_name=goods['name'])

        assert residue == goods['count']
