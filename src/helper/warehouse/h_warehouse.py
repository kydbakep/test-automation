from src.helper.warehouse.h_wh_core import WarehouseCoreHelper as Core
from src.helper.warehouse.h_wh_orders import WarehouseOrdersHelper as Orders
from src.helper.warehouse.h_wh_posting import WarehousePostingHelper as Posting
from src.helper.warehouse.h_wh_refunds import WarehouseRefundsHelper as Refunds
from src.helper.warehouse.h_wh_residue import WarehouseResidueHelper as Residue


class WarehouseHelper(Core, Orders, Posting, Refunds, Residue):
    pass
