from selene.api import s, ss


class SelectorsSales:
    SALES_TABLE = '#shop_table'
    SALES_CREATE_BUTTON = f'{SALES_TABLE} button[data-cid="table-btn-add"]'
    SALES_CREATE_DIALOG = 'div[data-cid="create_sale_dialog"] .js-dialog-face'

    SALES_DIALOG_CLIENT_INPUT = '.js-wh-sale-create-client-picker input'
    SALES_DIALOG_DROPDOWN_CLIENT_ELEMENT_F = "//div[@class='js-picker-holder']//span[text()='{}']//ancestor::li"
    SALES_DIALOG_STOCK_SELECT = 'select[name="warehouse"]'
    SALES_DIALOG_PRODUCT_INPUT = '.js-prodpicker-prod-drop input'
    SALES_DIALOG_PRODUCT_DROPDOWN_ELEMENT_F = "//div[contains(@class, 'b-dropdown_type_list')]" \
                                              "//div[text()='{}']//ancestor::tr"
    SALES_DIALOG_DESCRIPTION_INPUT = ''
    SALES_DIALOG_SAVE_BUTTON = f'{SALES_CREATE_DIALOG} button[type="submit"]'

    SALES_MODAL_FRAME = 'div[data-cid="winbox-modal-root"]'
    SALES_MODAL_QUANTITY_TOTAL_INPUT = f'{SALES_MODAL_FRAME} .js-qtypicker-total-count'
    SALES_MODAL_QUANTITY_SINGLE_INPUT = f'{SALES_MODAL_FRAME} .js-qtypicker-qty-input'
    SALES_MODAL_QUANTITY_TOTAL_ADD_ALL_BUTTON = f'{SALES_MODAL_FRAME} .js-qtypicker-add-all'
    SALES_MODAL_QUANTITY_SERIAL_ADD_ALL_BUTTON = f'{SALES_MODAL_FRAME} .js-serialpicker-add-all'
    SALES_MODAL_SERIAL_NUMBER_INPUT = f'{SALES_MODAL_FRAME} input[name="serial_numbers"]'
    SALES_MODAL_SERIAL_NUMBER_DROPDOWN = f'{SALES_MODAL_FRAME} .js-snresidpicker-view-root'
    SALES_MODAL_SERIAL_NUMBER_ITEM_X_F = "//tr[contains(@class, 'js-snresidpicker-li')]/td[text()='{}']"
    SALES_MODAL_SERIAL_NUMBER_LABEL_X_F = "//div[@class='b-tags__tag-text'][text()='{}']"
    SALES_MODAL_QUANTITY_INPUT_F = "//span[contains(text(), '{}')]" \
                                   "//ancestor::div[contains(@class, 'js-qtypicker-cell')]//input"  # by cell name
    SALES_MODAL_QUANTITY_ADD_ALL_BUTTON_F = "//span[.='{}']//ancestor::div[contains(@class, 'js-qtypicker-cell')]" \
                                            "//span[contains(@class, 'js-qtypicker-add-all-from-cell')]"  # by cell name
    SALES_MODAL_PRICE_INPUT = f'{SALES_MODAL_FRAME} input[name="price"]'
    SALES_MODAL_DISCOUNT_INPUT = f'{SALES_MODAL_FRAME} input[name="discount_value]'
    SALES_MODAL_DISCOUNT_BUTTON = f'{SALES_MODAL_FRAME} .js-discount-btns button'
    SALES_MODAL_WARRANTY_INPUT = f'{SALES_MODAL_FRAME} input[name="warranty_value]'
    SALES_MODAL_WARRANTY_BUTTON = f'{SALES_MODAL_FRAME} .js-prodedit-warranty button'
    SALES_MODAL_CLOSE_BUTTON = f'{SALES_MODAL_FRAME} .b-close'

    SALES_PAYMENT_DIALOG = 'div[data-cid="payment_for_document_dialog"]'
    SALES_PAYMENT_EMPLOYEE_SELECT = f'{SALES_PAYMENT_DIALOG} select[name="employee"]'
    SALES_PAYMENT_CASHBOX_SELECT = f'{SALES_PAYMENT_DIALOG} select[name="cashbox"]'
    SALES_PAYMENT_COMMENT_INPUT = f'{SALES_PAYMENT_DIALOG} textarea[name="description"]'
    SALES_PAYMENT_SUBMIT_BUTTON = f'{SALES_PAYMENT_DIALOG} button.js-cbp-submit'

    SALES_MODAL_SAVE_BUTTON = f'{SALES_MODAL_FRAME} button[type="submit"]'

    print(SALES_MODAL_SERIAL_NUMBER_DROPDOWN)


class Configured:
    def __init__(self, cell_name='Ячейка 1'):
        self._cell_quantity_input = s(SelectorsSales.SALES_MODAL_QUANTITY_INPUT_F.format(cell_name))
        self._cell_add_all_button = s(SelectorsSales.SALES_MODAL_QUANTITY_ADD_ALL_BUTTON_F.format(cell_name))
        self._warranty_by_days_button = ss(SelectorsSales.SALES_MODAL_WARRANTY_BUTTON)[0]
        self._warranty_by_months_button = ss(SelectorsSales.SALES_MODAL_WARRANTY_BUTTON)[1]
        self._modal_discount_absolute_button = ss(SelectorsSales.SALES_MODAL_DISCOUNT_BUTTON)[0]
        self._modal_discount_percent_button = ss(SelectorsSales.SALES_MODAL_DISCOUNT_BUTTON)[1]
