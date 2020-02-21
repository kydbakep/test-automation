import pytest

from lib.warehouse.pages.page_wh_posting import PageWarehousePosting


class FixturesWarehousePosting:

    @pytest.fixture(scope='function', name='create_posting')
    def create_random_posting(self):
        page = PageWarehousePosting()
        page.open_page()
        posting = page.create_random_posting()
        yield posting
