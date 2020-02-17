from selene.api import s, ss


class SelectorsSales:
    SALE_TABLE = '#shop_table'
    SALE_CREATE_BUTTON = f'{SALE_TABLE} button[data-cid="table-btn-add"]'
    SALE_CREATE_DIALOG = 'div[data-cid="create_sale_dialog"] .js-dialog-face'

    SALE_DIALOG_CLIENT_INPUT = '.js-wh-sale-create-client-picker input'
    SALE_DIALOG_DROPDOWN_CLIENT_ELEMENT_F = "//div[@class='js-picker-holder']//span[text()='{}']//ancestor::li"
    SALE_DIALOG_STOCK_SELECT = 'select[name="warehouse"]'
    SALE_DIALOG_PRODUCT_INPUT = '.js-prodpicker-prod-drop input'
    SALE_DIALOG_PRODUCT_DROPDOWN_ELEMENT_F = "//div[contains(@class, 'b-dropdown_type_list')]" \
                                             "//div[text()='{}']//ancestor::tr"
    SALE_DIALOG_DESCRIPTION_INPUT = ''

    SALE_MODAL_FRAME = 'div[data-cid="winbox-modal-root"]'
    SALE_MODAL_QUANTITY_TOTAL_INPUT = f'{SALE_MODAL_FRAME} .js-qtypicker-total-count'
    SALE_MODAL_QUANTITY_TOTAL_ADD_ALL_BUTTON = f'{SALE_MODAL_FRAME} .js-qtypicker-add-all'
    SALE_MODAL_QUANTITY_INPUT_F = "//span[contains(text(), '{}')]" \
                                  "//ancestor::div[contains(@class, 'js-qtypicker-cell')]//input"  # by cell name
    SALE_MODAL_QUANTITY_ADD_ALL_BUTTON_F = "//span[.='{}']//ancestor::div[contains(@class, 'js-qtypicker-cell')]" \
                                           "//span[contains(@class, 'js-qtypicker-add-all-from-cell')]"  # by cell name
    SALE_MODAL_PRICE_INPUT = f'{SALE_MODAL_FRAME} input[name="price"]'
    SALE_MODAL_DISCOUNT_INPUT = f'{SALE_MODAL_FRAME} input[name="discount_value]'
    SALE_MODAL_DISCOUNT_BUTTON = f'{SALE_MODAL_FRAME} .js-discount-btns button'
    SALE_MODAL_WARRANTY_INPUT = f'{SALE_MODAL_FRAME} input[name="warranty_value]'
    SALE_MODAL_WARRANTY_BUTTON = f'{SALE_MODAL_FRAME} .js-prodedit-warranty button'
    SALE_MODAL_CLOSE_BUTTON = f'{SALE_MODAL_FRAME} .b-close'
    SALE_MODAL_SAVE_BUTTON = f'{SALE_MODAL_FRAME} button[type="submit"]'


class Configured:
    def __init__(self, cell_name='Ячейка 1'):
        self._cell_quantity_input = s(SelectorsSales.SALE_MODAL_QUANTITY_INPUT_F.format(cell_name))
        self._cell_add_all_button = s(SelectorsSales.SALE_MODAL_QUANTITY_ADD_ALL_BUTTON_F.format(cell_name))
        self._warranty_by_days_button = ss(SelectorsSales.SALE_MODAL_WARRANTY_BUTTON)[0]
        self._warranty_by_months_button = ss(SelectorsSales.SALE_MODAL_WARRANTY_BUTTON)[1]
        self._modal_discount_absolute_button = ss(SelectorsSales.SALE_MODAL_DISCOUNT_BUTTON)[0]
        self._modal_discount_percent_button = ss(SelectorsSales.SALE_MODAL_DISCOUNT_BUTTON)[1]
