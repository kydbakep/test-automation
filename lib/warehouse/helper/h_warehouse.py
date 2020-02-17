from src.helper import WarehouseCoreHelper as Core
from src.helper import WarehouseOrdersHelper as Orders
from src.helper import WarehousePostingHelper as Posting
from src.helper import WarehouseRefundsHelper as Refunds
from src.helper import WarehouseResidueHelper as Residue


class WarehouseHelper(Core, Orders, Posting, Refunds, Residue):
    pass
