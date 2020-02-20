REFUND_DIALOG = 'div[data-cid="SupplierRefundsEditor"] .js-dialog-face'
REFUND_COMMENT = f'{REFUND_DIALOG} textarea'
REFUND_DIALOG_CLOSE_BUTTON = f'{REFUND_DIALOG} .b-close'
REFUND_DIALOG_X = "//div[@data-cid='SupplierRefundsEditor']/div[contains(@class, 'js-dialog-face')]"
REFUND_TARGET_ROW_X = "{0}//div[label[contains(@class, 'b-label')][contains(text(),'{1}')]]" \
                      "//ancestor::div[contains(@class, 'la-2form__row')]"
REFUND_DOCUMENT_ROW_X = REFUND_TARGET_ROW_X.format(REFUND_DIALOG_X, 'Оприходование')
REFUND_SUPPLIER_ROW_X = REFUND_TARGET_ROW_X.format(REFUND_DIALOG_X, 'Поставщик')
REFUND_DIALOG_SUPPLIER_PASSPORT = 'div[data-cid="client_dialog"]'
REFUND_DIALOG_SUPPLIER_PASSPORT_CLOSE_BUTTON = f'{REFUND_DIALOG_SUPPLIER_PASSPORT} .js-ceditor-cancel'

REFUND_STOCK_SELECTOR = f'{REFUND_DIALOG} .js-dialog-face select[name="warehouse_id"]'
REFUND_TARGET_GOODS_X_F = REFUND_DIALOG_X + '//span[contains(@id, "_viewer_link")][text()="{}"]'
REFUND_TARGET_GOODS_ROW_F = REFUND_TARGET_GOODS_X_F + "//ancestor::tr"

REFUND_GOODS = f'{REFUND_DIALOG} span[id$="_viewer_link"]'
REFUND_GOODS_CURR_QUANTITY_X_F = REFUND_TARGET_GOODS_ROW_F + "//input[@data-cid='item_quantity_text_from_fltable']"
REFUND_GOODS_AVAL_QUANTITY_X_F = REFUND_TARGET_GOODS_ROW_F + "//div[contains(@class, 'h-c-muted')]"
REFUND_GOODS_SERIAL_ICON = '//div[contains(@class, "i-sn")]'
REFUND_GOODS_PRICE_X_F = REFUND_TARGET_GOODS_ROW_F + "//div[@data-cid='price_item_from_fltable']"
REFUND_GOODS_SUM_X_F = REFUND_TARGET_GOODS_ROW_F + "//div[@data-cid='total_price_item_from_fltable']"

REFUND_GOODS_EDIT_BUTTON_X_F = REFUND_TARGET_GOODS_ROW_F + "//div[@data-cid='edit_item_from_fltable']"
REFUND_GOODS_EDIT_MODAL_X = '//div[@data-cid="winbox-modal-root"]'
REFUND_GOODS_EDIT_MODAL = 'div[data-cid="winbox-modal-root"]'
REFUND_GOODS_EDIT_MODAL_QUANTITY_SINGLE_INPUT = f'{REFUND_GOODS_EDIT_MODAL} .js-qtypicker-qty-input'

REFUND_GOODS_EDIT_MODAL_SERIAL_NUMBER_INPUT = f'{REFUND_GOODS_EDIT_MODAL} input[name="serial_numbers"]'
REFUND_GOODS_EDIT_MODAL_SERIAL_NUMBER_DROPDOWN = f'{REFUND_GOODS_EDIT_MODAL} .js-snresidpicker-view-root'
REFUND_GOODS_EDIT_MODAL_SERIAL_NUMBER_ITEM_X_F = "//tr[contains(@class, 'js-snresidpicker-li')]/td[text()='{}']"
REFUND_GOODS_EDIT_MODAL_SERIAL_NUMBER_LABEL_X_F = "//div[@class='b-tags__tag-text'][text()='{}']"
REFUND_GOODS_EDIT_MODAL_SERIAL_ITEMS_TOTAL_COUNT = '.js-serialpicker-total-count'

REFUND_GOODS_EDIT_MODAL_PRICE_INPUT = f'{REFUND_GOODS_EDIT_MODAL} input[name="price"]'
REFUND_GOODS_EDIT_MODAL_COMMENT_INPUT = f'{REFUND_GOODS_EDIT_MODAL} textarea[name="comment"]'
REFUND_GOODS_EDIT_MODAL_SAVE_BUTTON = f'{REFUND_GOODS_EDIT_MODAL} .js-prodedit-submit'
REFUND_GOODS_EDIT_MODAL_CLOSE_BUTTON = f'{REFUND_GOODS_EDIT_MODAL} #modal1_close'
REFUND_GOODS_EDIT_MODAL_ADD_ALL_X = '//span[contains(@class, "js-qtypicker-add-all")]'
REFUND_GOODS_EDIT_MODAL_ADD_ALL = 'span.js-qtypicker-add-all'
REFUND_GOODS_EDIT_MODAL_ADD_ALL_SERIAL_X = '//span[contains(@class, "js-qtypicker-add-all")]'

REFUND_CASH_INCOME_CHECKBOX_ELEMENT = "//label[contains(@for, '_with_cbox_tran')]//ancestor::div[@class='b-checkbox']"
REFUND_CASH_INCOME_CHECKBOX_LABEL = f'{REFUND_CASH_INCOME_CHECKBOX_ELEMENT}/label'
REFUND_CASH_INCOME_CHECKBOX_INPUT = f'{REFUND_CASH_INCOME_CHECKBOX_ELEMENT}/input'

REFUND_SUBMIT_BUTTON = f'{REFUND_DIALOG} .js-dialog-face button[type="submit"]'
