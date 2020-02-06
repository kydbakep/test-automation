from src.helper.global_.fixtures.f_browser import RegisterFixture
from src.pages.warehouse.page_wh_core import PageWarehouse
from src.pages.warehouse.page_wh_residue import PageWarehouseResidue


class TestWarehousePage(RegisterFixture):

    def test_warehouse_residue_tab(self):
        warehouse = PageWarehouse()
        warehouse.open_residue_tab()
        residue = PageWarehouseResidue(None)
        loaded = residue.is_page_loaded()
        assert loaded
