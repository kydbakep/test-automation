import pytest
from src.helper.global_.fixtures.f_browser import RegisterFixture
from src.pages.warehouse.page_wh_core import PageWarehouse
from src.pages.warehouse.page_wh_movement import PageWarehouseMovement


class TestWarehouseMovement(RegisterFixture):

    @pytest.mark.s03t131
    def test_movement_open_close_dialog(self):
        warehouse = PageWarehouse()
        warehouse.open_movements_tab()
        movement = PageWarehouseMovement()
        opened = movement.open_movement_dialog()
        closed = movement.close_movement_dialog()

        assert all([opened, closed])
