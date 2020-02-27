# STOCKS
STOCK_CREATE_BUTTON = '.js-wh-add'
STOCK_EDIT_BUTTON = '.js-wh-edit'
STOCK_DELETE_BUTTON = '.js-wh-remove'
STOCK_WAREHOUSE_SELECT = 'select[name="warehouse"]'

# STOCK GOODS CATEGORIES
STOCK_CREATE_CATEGORY_BUTTON = '.js-category-add'
STOCK_EDIT_CATEGORY_BUTTON = '.js-edit-button'
STOCK_DELETE_CATEGORY_BUTTON = '.js-remove-button'

# CREATE STOCK DIALOG
STOCK_CREATE_DIALOG = 'div[data-cid="warehouse_item_dialog"]'
STOCK_CREATE_TITLE_INPUT = f'{STOCK_CREATE_DIALOG} #l-wh-title'
STOCK_CREATE_RADIO_BUTTON_LOCAL = 'label[for="l-wh-type-local"] .h-radio'
STOCK_CREATE_RADIO_BUTTON_GLOBAL = 'label[for="l-wh-type-global_"] .h-radio'

STOCK_USER_ACCESS_CHECKBOX_ALL = '.js-employees label[for="cb"] span'
STOCK_USER_ACCESS_CHECKBOX_USER_XPATH = "//div[@class='b-table__body'][.='{user}']//label/span[@class='h-checkbox']"

# CREATE CATEGORY DIALOG
STOCK_CREATE_CATEGORY_DIALOG = 'div[data-cid="category_dialog"]'
STOCK_CREATE_CATEGORY_TITLE_INPUT = f'{STOCK_CREATE_CATEGORY_DIALOG} input#js-wh-title'
STOCK_CREATE_CATEGORY_WARNING = f'{STOCK_CREATE_CATEGORY_DIALOG} span.b-warning__text'
STOCK_CREATE_CATEGORY_PERCENT_CHECKBOX = 'label[for="l-operation-earnings-pct"] span'
STOCK_CREATE_CATEGORY_PERCENT_INPUT = 'input[name="earnings_pct"]'
STOCK_CREATE_CATEGORY_PERCENT_OPTION_FROM_SUM = f'{STOCK_CREATE_CATEGORY_DIALOG} button[data-value="1"]'
STOCK_CREATE_CATEGORY_PERCENT_OPTION_FROM_PROFIT = f'{STOCK_CREATE_CATEGORY_DIALOG} button[data-value="0"]'

STOCK_CREATE_CATEGORY_SUM_CHECKBOX = 'label[for="l-operation-earnings-sum"] span'
STOCK_CREATE_CATEGORY_SUM_INPUT = 'input[name="earnings_sum"]'

# ============================================================
STOCK_SAVE_BUTTON = f'{STOCK_CREATE_DIALOG} .js-submit-dialog'
STOCK_CLOSE_BUTTON = f'{STOCK_CREATE_DIALOG} .js-close-dialog'
