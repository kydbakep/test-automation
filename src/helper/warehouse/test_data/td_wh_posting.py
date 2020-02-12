from src.helper.global_.randomizer import *


def __get_random_items_data(serial=False):
    random_suffix = get_random_low_string(5, with_digits=True)
    quantity = get_random_int(10, 20)
    data = {
        'quantity': quantity,
        'price': get_random_int(101, 999),
        'category': 'parts'}
    if serial:
        data.update({'title': f'Goods_serial_{random_suffix}'})
        data.update(get_random_serial_numbers(quantity))
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


def get_random_goods_data(serial=False, quantity=10):
    data = __get_random_posting_data()
    for _ in range(quantity):
        data['goods'].append(__get_random_items_data(serial))
    return data


def get_mixed_random_goods_data(serial_goods_qty=1, normal_goods_qty=1):
    data = __get_random_posting_data()
    for _ in range(serial_goods_qty):
        data['goods'].append(__get_random_items_data(serial=True))
    for _ in range(normal_goods_qty):
        data['goods'].append(__get_random_items_data(serial=False))
    return data
