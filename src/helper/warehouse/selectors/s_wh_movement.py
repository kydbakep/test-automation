from selene.api import by

MOVEMENT_ADD_NEW_BUTTON = '#warehouse_move_table [data-cid="table-btn-add"]'
MOVEMENT_CREATE_FRAME = by.xpath("//div[text()='Новое перемещение']//ancestor::div[contains(@class, 'js-header-root')]")

MOVEMENT_STOCK_FROM = 'select[id$="move"]'
MOVEMENT_STOCK_TO = 'select[id$="move-target"]'

MOVEMENT_NAME_INPUT = '.js-prodpicker-prod-drop input'
MOVEMENT_DROPDOWN_TARGET = "//tr[contains(@class, 'b-dropdown__item')]//div[text()='{}']"

MOVEMENT_QUANTITY_MODAL = '[data-cid="winbox-modal-root"]'
MOVEMENT_QUANTITY_MODAL_INPUT = f'{MOVEMENT_QUANTITY_MODAL} input[name^="qty"]'
MOVEMENT_QUANTITY_MODAL_INPUT_SERIAL = f'{MOVEMENT_QUANTITY_MODAL} input[name="serial_numbers"]'
MOVEMENT_QUANTITY_ADD_ALL_BUTTON = '.js-qtypicker-cell span[class*="add-all"]'
MOVEMENT_QUANTITY_ADD_ALL_BUTTON_SERIAL = '.js-serialpicker-root span[class*="add-all"]'
MOVEMENT_SUBMIT_QUANTITY_MODAL_BUTTON = '.js-prodedit-submit'

MOVEMENT_COMMENTS_AREA = '#l-wh-comments'

MOVEMENT_SUBMIT_BUTTON = '.js-wh-move-create-submit'
