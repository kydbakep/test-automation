""" 'F' is mark for elem should be formatted. Example: SOME_ELEMENT_SELECTOR_F """

POSTING_CREATE_DIALOG = '[data-cid="create_posting_dialog"]'
POSTING_VIEW_DIALOG = '[data-cid="view_income_dialog"]'
POSTING_VIEW_DIALOG_CLOSE_BUTTON = f'{POSTING_VIEW_DIALOG} .b-close'
POSTING_GOODS_CATEGORIES = {'store': '[data-node-id="361222"]', 'parts': '[data-node-id="361223"]'}
POSTING_CREATE_DIALOG_FACE = f'{POSTING_CREATE_DIALOG} .js-dialog-face'
POSTING_CREATE_NEW_BUTTON = '#warehouse_posting_table [data-cid="table-btn-add"]'
POSTING_SUBMIT_BUTTON = f'{POSTING_CREATE_DIALOG} button[type="submit"]'

# NEW POSTING DIALOG
POSTING_SUPPLIER_INPUT = 'input#js-wh-supplier'

POSTING_SUPPLIER_DROPDOWN_TARGET_X_F = "//li[contains(@class, 'b-dropdown__item')]" \
                                       "/span[contains(text(), '{}')]"

POSTING_ADD_NEW_CLIENT_PLUS_BUTTON = '[data-input-id="js-wh-supplier"] .h-plus.js-create-client'
POSTING_ADD_NEW_CLIENT_DROPDOWN_BUTTON = '[data-input-id="js-wh-supplier"] .b-dropdown__content .js-create-client'
POSTING_WAREHOUSE_SELECT = f'{POSTING_CREATE_DIALOG_FACE} select[name="warehouse"]'

# PRODUCT
POSTING_PRODUCT_NAME_INPUT = f'{POSTING_CREATE_DIALOG_FACE} #js-wh-title'
POSTING_NEW_PRODUCT_AREA = '.js-wh-income-product-create-new'
POSTING_NEW_PRODUCT_CATEGORY_DROPDOWN = f'{POSTING_NEW_PRODUCT_AREA} .b-sel'
POSTING_NEW_PRODUCT_CATEGORY_TARGET_PARTS = POSTING_NEW_PRODUCT_AREA + ' .b-tree__node[data-node-title="Запчасти"]'
POSTING_NEW_PRODUCT_CATEGORY_TARGET_STORE = POSTING_NEW_PRODUCT_AREA + ' .b-tree__node[data-node-title="Магазин"]'
POSTING_NEW_PRODUCT_CATEGORY_TARGET_CUSTOM = POSTING_NEW_PRODUCT_AREA + ' .b-tree__node[data-node-title="{}"]'
POSTING_NEW_PRODUCT_QUANTITY_INPUT = f'{POSTING_CREATE_DIALOG} #l-wh-quantity'
# prices
POSTING_NEW_PRODUCT_PRICE_PURCHASE_INPUT = 'input[name="price"]'
POSTING_NEW_PRODUCT_PRICE_ZERO_INPUT = 'input[name="146511"]'
POSTING_NEW_PRODUCT_PRICE_REPAIR_INPUT = 'input[name="146509"]'
POSTING_NEW_PRODUCT_PRICE_RETAIL_INPUT = 'input[name="146510"]'
# serial accounting
POSTING_NEW_PRODUCT_IS_SERIAL_CHECKBOX_INPUT = '.js-wh-income-product-create-new .b-checkbox input'
POSTING_NEW_PRODUCT_IS_SERIAL_CHECKBOX_LABEL = '.js-wh-income-product-create-new .b-checkbox label'
POSTING_NEW_PRODUCT_SERIAL_NUMBERS_FRAME = '.js-sernum-root'
POSTING_NEW_PRODUCT_SERIAL_NUMBERS_INPUT = f'{POSTING_NEW_PRODUCT_SERIAL_NUMBERS_FRAME} input.js-labeler-input'
POSTING_NEW_PRODUCT_SERIAL_NUMBERS_ADDED_NUMBER_F = '.js-labeler-badges [data-tag-text="{}"]'
# ADD TO POSTING
POSTING_NEW_PRODUCT_ADD_BUTTON = '.js-wh-income-create-add'

# POSTING VIEW DIALOG
POSTING_VIEW_PRODUCT_TITLE = 'div[data-cid="item_title_from_fltable"]'

# CLIENT DIALOG
POSTING_CLIENT_DIALOG = '[data-cid="client_dialog"]'
POSTING_CLIENT_DIALOG_NAME_INPUT = f'{POSTING_CLIENT_DIALOG} input[name="name"]'
POSTING_CLIENT_DIALOG_SUBMIT_BUTTON = f'{POSTING_CLIENT_DIALOG} button[type="submit"]'

POSTING_DOCUMENT_LINK_X = '//a[@data-cid="table-body-show-link"]'
POSTING_DOCUMENT_LABEL_X = POSTING_DOCUMENT_LINK_X + "[.='{}']"

# REFUNDS
CREATE_REFUND_BUTTON = '.js-create-refund'
