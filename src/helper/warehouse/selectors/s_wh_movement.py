from selene.api import by

ADD_NEW_MOVEMENT_BUTTON = '#warehouse_move_table [data-cid="table-btn-add"]'
CREATE_MOVEMENT_FRAME = by.xpath("//div[text()='Новое перемещение']//ancestor::div[contains(@class, 'js-header-root')]")
