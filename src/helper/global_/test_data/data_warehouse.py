from src.helper.global_.randomizer import *


def get_random_items_data(serial=False):
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


def get_random_posting_data():
    data = {
        'supplier': f'{get_random_first_name()} {get_random_last_name()}',
        'stock': get_random_stock_name()
    }
    return data


def get_random_goods_data(serial=False):
    data = get_random_posting_data()
    data.update(get_random_items_data(serial))
    return data
