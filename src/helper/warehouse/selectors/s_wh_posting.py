POSTING_DIALOG = '[data-cid="create_posting_dialog"]'
POSTING_GOODS_CATEGORIES = {'store': '[data-node-id="361222"]', 'parts': '[data-node-id="361223"]'}
POSTING_CREATE_DIALOG = f'{POSTING_DIALOG} .js-dialog-face'
POSTING_CREATE_NEW_BUTTON = '#warehouse_posting_table [data-cid="table-btn-add"]'

# NEW POSTING DIALOG
POSTING_SUPPLIER_INPUT = 'input#js-wh-supplier'

POSTING_SUPPLIER_DROPDOWN_TARGET_XPATH_F = "//li[contains(@class, 'b-dropdown__item')]" \
                                           "/span[contains(text(), '{}')]"  # 'F' is mark for elem should be formatted

POSTING_ADD_NEW_CLIENT_PLUS_BUTTON = '[data-input-id="js-wh-supplier"] .h-plus.js-create-client'
POSTING_ADD_NEW_CLIENT_DROPDOWN_BUTTON = '[data-input-id="js-wh-supplier"] .b-dropdown__content .js-create-client'

POSTING_WAREHOUSE_SELECT = f'{POSTING_CREATE_DIALOG} select[name="warehouse"]'

# PRODUCT
POSTING_PRODUCT_NAME_INPUT = f'{POSTING_CREATE_DIALOG} #js-wh-title'
POSTING_NEW_PRODUCT_AREA = '.js-wh-income-product-create-new'
POSTING_NEW_PRODUCT_CATEGORY_DROPDOWN = f'{POSTING_NEW_PRODUCT_AREA} .b-sel'
POSTING_NEW_PRODUCT_CATEGORY_TARGET_PARTS = POSTING_NEW_PRODUCT_AREA + ' .b-tree__node[data-node-title="Запчасти"]'
POSTING_NEW_PRODUCT_CATEGORY_TARGET_STORE = POSTING_NEW_PRODUCT_AREA + ' .b-tree__node[data-node-title="Магазин"]'
POSTING_NEW_PRODUCT_CATEGORY_TARGET_CUSTOM = POSTING_NEW_PRODUCT_AREA + ' .b-tree__node[data-node-title="{}"]'
POSTING_PRODUCT_IS_SERIAL_CHECKBOX_INPUT = '.js-wh-income-product-create-new .b-checkbox input'
POSTING_PRODUCT_IS_SERIAL_CHECKBOX_LABEL = '.js-wh-income-product-create-new .b-checkbox label'

# CLIENT DIALOG
POSTING_CLIENT_DIALOG = '[data-cid="client_dialog"]'
POSTING_CLIENT_DIALOG_NAME_INPUT = f'{POSTING_CLIENT_DIALOG} input[name="name"]'
POSTING_CLIENT_DIALOG_SUBMIT_BUTTON = f'{POSTING_CLIENT_DIALOG} button[type="submit"]'
