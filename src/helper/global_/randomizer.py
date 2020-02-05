import random
import string

from faker import Faker


def get_random_low_string(ln=16, with_digits=False):
    if with_digits:
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(ln))
    else:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(ln))


def get_random_int(a=1, b=2):
    return random.randint(a, b)


def get_random_float(a=1, b=2):
    return round(random.uniform(a, b), 2)


def get_random_phone_number():
    return random.randint(1000000000, 9999999999)


def get_random_login():
    return f'Test-{Faker().user_name()}'


def get_random_branch_name():
    return f'Location-{get_random_low_string(7, with_digits=True)}'


def get_random_item_name():
    return f'Item-{get_random_low_string(8)}'


def get_random_spare_part():
    return f'Spare-{get_random_low_string(8)}'


def get_random_service_name():
    return f'Service-{get_random_low_string(8)}'


def get_random_cashbox_name():
    return f'box_{Faker().user_name()}'


def get_random_address():
    return Faker('ru_RU').street_address()


def get_random_client_name():
    sex = get_random_int(0, 1)
    fake = Faker("ru_RU")
    if sex:
        name = f'{fake.first_name_male()} {fake.last_name_male()}'
    else:
        name = f'{fake.first_name_female()} {fake.last_name_female()}'
    return name


def get_random_orders_type_name():
    return Faker('ru_RU').word()


def get_random_goods_type():
    return f'Новый {Faker("ru_RU").word()}'


def get_random_first_name():
    return Faker().first_name()


def get_random_last_name():
    return Faker().last_name()


def get_random_email():
    fake = Faker()
    first_n = fake.random.choice([fake.first_name_male(), fake.first_name_female()])
    last_n = fake.random.choice([fake.last_name_male(), fake.last_name_female()])
    random_letter = random.choice(string.ascii_letters).lower()
    username = "{0}{1}{2}@mail.com".format(first_n, random_letter, last_n).lower()
    return username
