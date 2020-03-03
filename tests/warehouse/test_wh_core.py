import pytest
from lib.auth.fixtures.f_browser import FixturesRegister
from lib.global_.fixtures.f_browser_settings import FixturesSettings
from lib.warehouse.pages.page_wh_core import PageWarehouse


@pytest.mark.skip
class TestWarehousePage(FixturesSettings, FixturesRegister):

    @pytest.mark.parametrize('tab', PageWarehouse().tabs)
    def test_wh_open_tabs(self, tab, warehouse=PageWarehouse()):
        opened = warehouse.open_tab(tab_selector=tab)
        assert opened
