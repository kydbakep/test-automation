REFUND_DIALOG = 'div[data-cid="SupplierRefundsEditor"] .js-dialog-face'
REFUND_DIALOG_CLOSE_BUTTON = f'{REFUND_DIALOG} .b-close'
REFUND_DIALOG_X = "//div[@data-cid='SupplierRefundsEditor']/div[contains(@class, 'js-dialog-face')]"
REFUND_TARGET_ROW_X = "{0}//div[label[contains(@class, 'b-label')][contains(text(),'{1}')]]" \
                      "//ancestor::div[contains(@class, 'la-2form__row')]"
REFUND_DOCUMENT_ROW_X_F = REFUND_TARGET_ROW_X.format(REFUND_DIALOG_X, 'Оприходование')
REFUND_SUPPLIER_ROW_X_F = REFUND_TARGET_ROW_X.format(REFUND_DIALOG_X, 'Поставщик')

REFUND_STOCK_SELECTOR = f'{REFUND_DIALOG} .js-dialog-face select[name="warehouse_id"]'
REFUND_GOODS = f'{REFUND_DIALOG} .js-dialog-face span[id$="_viewer_link"]'
REFUND_TARGET_GOODS_X_F = REFUND_DIALOG_X + '//span[contains(@id, "_viewer_link")][text()="{}"]'
REFUND_TARGET_GOODS_ROW_F = REFUND_TARGET_GOODS_X_F + "//ancestor::tr"

REFUND_GOODS_QUANTITY_F = REFUND_TARGET_GOODS_ROW_F + "//input[@data-cid='item_quantity_text_from_fltable']"
REFUND_GOODS_SERIAL_ICON = '//div[contains(@class, "i-sn")]'
REFUND_GOODS_PRICE_X_F = REFUND_TARGET_GOODS_ROW_F + "//div[@data_cid='price_item_from_fltable']"
REFUND_GOODS_SUM_X_F = REFUND_TARGET_GOODS_ROW_F + "//div[@data_cid='total_price_item_from_fltable']"
REFUND_GOODS_EDIT_BUTTON_X_F = REFUND_TARGET_GOODS_ROW_F + "//div[@data_cid='edit_item_from_fltable']"
REFUND_GOODS_EDIT_MODAL_X = '//div[@data-cid="winbox-modal-root"]'
REFUND_GOODS_EDIT_MODAL_ADD_ALL_X = '//span[contains(@class, "js-qtypicker-add-all")]'
REFUND_GOODS_EDIT_MODAL_ADD_ALL_SERIAL_X = '//span[contains(@class, "js-qtypicker-add-all")]'

REFUND_SUBMIT_BUTTON = f'{REFUND_DIALOG} .js-dialog-face button[type="submit"]'
REFUND_CASH_INCOME_CHECKBOX_ELEMENT = "//label[contains(@for, '_with_cbox_tran')]//ancestor::div[@class='b-checkbox']"
REFUND_CASH_INCOME_CHECKBOX_LABEL = f'{REFUND_CASH_INCOME_CHECKBOX_ELEMENT}/label'
REFUND_CASH_INCOME_CHECKBOX_INPUT = f'{REFUND_CASH_INCOME_CHECKBOX_ELEMENT}/input'
