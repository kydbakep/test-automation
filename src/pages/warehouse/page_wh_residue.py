from selene.api import s, by
from selene.support.conditions.be import visible, in_dom

from src.helper.warehouse.selectors.s_wh_residue import TABLE_BODY


class PageWarehouseResidue:
    def __init__(self):
        """
        __goods_row should be formatted in methods (with goods name)
        example: __goods_row.format(goods_name)

        """
        self.__goods_row = TABLE_BODY['row_by_title']
        self.__row_checkbox = self.__get_checkbox_element_for_target_row(self.__get_order_id())

    def __get_order_id(self, goods_name):
        order_id = s(self.__goods_row.format(goods_name)).get_attribute('data-order-id')
        return order_id

    @staticmethod
    def __get_checkbox_element_for_target_row(order_id):
        return f'label[for="residue_table-checkbox-{order_id}"]'
