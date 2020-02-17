# FILTERS
WAREHOUSE_FILTER_SELECT = 'select[name="warehouse"]'
CATEGORY_FILTER_DROPDOWN = '.js-c-categories'
CATEGORY_FILTER_ITEMS_FRAME = f'{CATEGORY_FILTER_DROPDOWN} .b-tree__leaf'
CATEGORY_FILTER_TARGET_OPTION = '.b-tree__node[data-node-title="{name}"]'
AVAILABILITY_FILTER_SELECT = 'select#ls-wh-availability'
IMPORT_EXPORT_BUTTON = '.la-grid__item.h-p-r button'
IMPORT_OPTION = '.js-import'
EXPORT_GOODS_OPTION = '.js-export'
EXPORT_RESIDUE_OPTION = '.js-export-residue'
TABLE_COLUMNS_FILTER_BUTTON = 'button[data-cid="table-btn-column"]'
TABLE_COLUMNS_CHECKBOXES = {'code': '[data-cid="table-column-dp"] label[for="code"]',
                            'article': '[data-cid="table-column-dp"] label[for="article"]',
                            'image': '[data-cid="table-column-dp"] label[for="image"]',
                            'residue': '[data-cid="table-column-dp"] label[for="residue"]',
                            'min_residue': '[data-cid="table-column-dp"] label[for="min_residue"]',
                            'retail': '[data-cid="table-column-dp"] label[for="price-145041"]',
                            'zero': '[data-cid="table-column-dp"] label[for="price-145042"]',
                            'repair': '[data-cid="table-column-dp"] label[for="price-145040"]',
                            'warranty': '[data-cid="table-column-dp"] label[for="warranty"]'}

# TABLE
TABLE_BODY = {'table': '#residue_table',
              'row': 'div[data-cid="table-body-row"]',
              'row_by_title': "//div[@data-body-cell='title'][.='{}']//ancestor::div[@data-cid='table-body-row']",
              'title': 'div[data-body-cell="title"]',
              'code': 'div[data-body-cell="code"]',
              'article': 'div[data-body-cell="article"]',
              'image': 'div[data-body-cell="image"]',
              'residue': 'div[data-body-cell="residue"]',
              'min_residue': 'div[data-body-cell="min_residue"]',
              'retail': 'div[data-body-cell="price-145041"]',
              'zero': 'div[data-body-cell="price-145042"]',
              'repair': 'div[data-body-cell="price-145040"]',
              'warranty': 'div[data-body-cell="warranty"]'}

TARGET_GOODS_DIALOG_XPH_F = "//div[contains(@class, 'js-header-lside')]//div[@class='b-ddd-title__title'][text()='{}']"
