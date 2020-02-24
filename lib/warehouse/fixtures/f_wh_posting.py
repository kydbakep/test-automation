import pytest

from lib.warehouse.pages.page_wh_posting import PageWarehousePosting


class FixturesWarehousePosting:
    page = PageWarehousePosting()

    @pytest.fixture(scope='class', name='single_posting_class')
    def create_random_single_posting_class_fixture(self):
        self.page.open_page()
        posting = self.page.create_random_posting()
        yield posting

    @pytest.fixture(scope='class', name='multiple_posting_class')
    def create_random_mixed_posting_class_fixture(self):
        self.page.open_page()
        posting = self.page.create_random_posting(mixed=True, normal_goods_qty=2,
                                                  serial_goods_qty=0,
                                                  serial_numbers_qty=4)
        yield posting
