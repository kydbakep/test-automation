from lib.warehouse.helper.h_wh_core import WarehouseCoreHelper as Core
from lib.warehouse.helper.h_wh_orders import WarehouseOrdersHelper as Orders
from lib.warehouse.helper.h_wh_posting import WarehousePostingHelper as Posting
from lib.warehouse.helper.h_wh_refunds import WarehouseRefundsHelper as Refunds
from lib.warehouse.helper.h_wh_residue import WarehouseResidueHelper as Residue


class WarehouseHelper(Core, Orders, Posting, Refunds, Residue):
    pass
