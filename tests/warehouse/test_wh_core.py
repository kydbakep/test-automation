import pytest
from lib.auth.fixtures.f_browser import RegisterFixture
from lib.warehouse.pages.page_wh_core import PageWarehouse


class TestWarehousePage(RegisterFixture):

    @pytest.mark.parametrize('tab', PageWarehouse().tabs)
    def test_wh_open_tabs(self, tab, warehouse=PageWarehouse()):
        opened = warehouse.open_tab(tab_selector=tab)
        assert opened
