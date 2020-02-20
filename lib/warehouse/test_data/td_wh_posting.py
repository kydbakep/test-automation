from lib.randomizer import *


def __get_random_items_data(serial: bool = False, numbers_qty: int = None):
    random_suffix = get_random_low_string(5, with_digits=True)
    if serial:
        quantity = numbers_qty or get_random_int(10, 20)
    else:
        quantity = get_random_int(10, 20)
    data = {
        'quantity': quantity,
        'price': get_random_int(101, 999),
        'category': 'parts'}
    if serial:
        data.update({'title': f'Goods_serial_{random_suffix}'})
        data.update(get_random_serial_numbers(numbers_qty or quantity))
    else:
        data.update({'title': f'Goods_{random_suffix}'})
    return data


def __get_random_posting_data():
    data = {
        'supplier': {'name': f'{get_random_first_name()} {get_random_last_name()}'},
        'stock': get_random_stock_name(),
        'goods': []
    }
    return data


def get_random_goods_data(serial: bool = False, quantity: int = 10, numbers_qty: int = None):
    data = __get_random_posting_data()
    for _ in range(quantity):
        data['goods'].append(__get_random_items_data(serial, numbers_qty=numbers_qty))
    return data


def get_mixed_random_goods_data(serial_goods_qty: int = 1,
                                normal_goods_qty: int = 1,

                                # for serial goods
                                numbers_qty: int = None):
    data = __get_random_posting_data()
    for _ in range(serial_goods_qty):
        data['goods'].append(__get_random_items_data(serial=True, numbers_qty=numbers_qty))
    for _ in range(normal_goods_qty):
        data['goods'].append(__get_random_items_data(serial=False))
    return data
