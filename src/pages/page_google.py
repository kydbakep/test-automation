from selene.api import s, ss
from selene import browser

from src.helper.global_.selectors.sel_google_page import GOOGLE_SEARCH_INPUT
from src.lib.lib_url import GOOGLE_URL


class GoogleSearch:
    def __init__(self):
        browser.open(GOOGLE_URL)

    @staticmethod
    def find(search_string, result_index=0):
        s(GOOGLE_SEARCH_INPUT).set(search_string).press_enter()
        results = []
        for result in ss('a>h3[class]'):
            results.append(result.text)
        return results[result_index]
