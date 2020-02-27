from lib.sales.pages.page_sales_core import PageSales
from lib.settings.pages.page_settings_core import PageSettings
from lib.warehouse.pages.page_wh_core import PageWarehouse
from lib.warehouse.pages.page_wh_posting import PageWarehousePosting
from lib.warehouse.pages.page_wh_refunds import PageWarehousePostingRefunds


class WarehousePages:
    def __init__(self):
        self.sales = PageSales()
        self.settings = PageSettings()
        self.warehouse = PageWarehouse()
        self.posting = PageWarehousePosting()
        self.refunds = PageWarehousePostingRefunds()
