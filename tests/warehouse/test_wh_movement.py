import pytest

from lib.auth.fixtures.f_browser import RegisterFixture
from lib.warehouse.pages.page_wh_core import PageWarehouse
from lib.warehouse.pages.page_wh_movement import PageWarehouseMovement
from lib.warehouse.pages.page_wh_posting import PageWarehousePosting
from lib.warehouse.pages.page_wh_residue import PageWarehouseResidue
from lib.warehouse.pages.page_wh_stock import PageWarehouseStock


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
        quantity_for_move = 2
        warehouse_page = PageWarehouse()
        warehouse_page.open_settings_tab()

        stock_page = PageWarehouseStock()
        default_stock = stock_page.default_stock
        new_local_stock = stock_page.create_local_stock()

        warehouse_page.open_posting_tab()
        posting_page = PageWarehousePosting()
        goods_data = posting_page.create_random_posting(stock=default_stock, goods_qty=1, serial=True)['goods'][0]

        movement_page = PageWarehouseMovement()
        movement_page.open_page()
        movement_page.open_movement_dialog()
        movement_page.select_stock_from(default_stock)
        movement_page.select_stock_to(new_local_stock)
        movement_page.select_goods_from_dropdown(goods_name=goods_data['title'])
        movement_page.set_quantity(quantity_for_move, serials=goods_data['serials'])
        movement_page.move()

        residue_page = PageWarehouseResidue()
        residue_page.open_page()
        residue_new = residue_page.get_current_residue(product_name=goods_data['title'], stock_name=new_local_stock)
        residue_default = residue_page.get_current_residue(product_name=goods_data['title'], stock_name=default_stock)

        assert residue_default == goods_data['quantity'] - quantity_for_move
        assert residue_new == quantity_for_move
