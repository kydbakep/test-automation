import pytest

from lib.global_.helper.h_methods import is_numbers_in_string
from lib.randomizer import *


@pytest.mark.tests_for_helper
class TestRandomise:

    def test_random_float(self):
        num = get_random_float(5, 10)
        assert all([num >= 5, num <= 10, type(num) is float])

    def test_random_int(self):
        num = get_random_int(1, 5)
        assert all([num >= 1, num <= 5, type(num) is int])

    def test_random_string(self):
        random_string_1 = get_random_low_string(5)
        random_string_2 = get_random_low_string(5)
        assert all([len(random_string_1) == 5, random_string_1 != random_string_2, type(random_string_1) is str])

    def test_random_string_with_digits(self):
        random_string = get_random_low_string(30, with_digits=True)
        assert all([is_numbers_in_string(random_string), type(random_string) is str])

    def test_random_phone_number(self):
        number = get_random_phone_number()
        assert len(str(number)) == 10

    def test_random_login(self):
        login = get_random_login()
        assert all([login.startswith('Test'), len(login) > 5])

    def test_random_branch_name(self):
        branch = get_random_branch_name()
        assert all([branch.startswith('Location'), len(branch) == 16])

    def test_random_item_name(self):
        item = get_random_item_name()
        assert all([item.startswith('Item'), len(item) == 13])

    def test_random_spare_part(self):
        item = get_random_spare_part()
        assert all([item.startswith('Spare'), len(item) == 14])

    def test_random_service_name(self):
        service = get_random_service_name()
        assert all([service.startswith('Service'), len(service) == 16])

    def test_random_name(self):
        name = get_random_client_name()
        assert all([len(name) > 8, type(name) is str])

    def test_random_email(self):
        email = get_random_email()
        assert all([len(email) > 6, type(email) is str, '@' in email])
