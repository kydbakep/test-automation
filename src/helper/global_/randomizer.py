import random
import string
from time import strftime
from datetime import datetime

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
