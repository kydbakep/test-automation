from selene.api import browser, be, s, ss, query
from selene.core.entity import Element, Collection
from selene.core.exceptions import TimeoutException as TimeOut
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    StaleElementReferenceException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from lib.main.selectors.sel_global_project import *


# MASK
def __wait_for_mask_disappear():
    s(DIALOG_MASK_JS).should(be.not_.visible)
    s(DIALOG_MASK_H).should(be.not_.visible)


def is_element_displayed(selector_or_element, timeout=1):
    try:
        if type(selector_or_element) is WebElement:
            WebDriverWait(driver=browser, timeout=timeout).until(visibility_of(selector_or_element))
            displayed = True
        elif type(selector_or_element) is Element:
            selector_or_element.with_(timeout=timeout).should(be.visible)
            displayed = True
        elif type(selector_or_element) is Collection:
            selector_or_element[0].with_(timeout=timeout).should(be.visible)
            displayed = True
        elif type(selector_or_element) in (str, tuple):
            browser.with_(timeout=timeout).element(selector_or_element).should(be.visible)
            displayed = True
        else:
            raise TypeError(f'\nUnknown element or selector type: {selector_or_element}')
    except (TypeError, TimeOut, TimeoutException, NoSuchElementException, ElementNotVisibleException,
            StaleElementReferenceException):
        displayed = False

    return displayed


def is_numbers_in_string(string_):
    state = False
    nums = []
    for i in string_:
        try:
            nums.append(int(i))
            state = True
            break
        except ValueError:
            pass
    return state


def set_select_option(select_web_element, name: str):
    node = select_web_element
    select = Select(node)
    select.select_by_visible_text(name)


def navigate_to(*urls):
    for url in urls:
        url_selector = f'[href="{url}"]'
        __wait_for_mask_disappear()
        s(url_selector).should(be.clickable).click()
    update_table_component()


def update_table_component():
    try:
        if is_element_displayed(PRELOADER_SPINNER):
            loaders = ss(PRELOADER_SPINNER)
            for spinner in loaders:
                spinner.should(be.not_.visible)
    except(NoSuchElementException, TimeoutException, StaleElementReferenceException, TypeError):
        s(PRELOADER_SPINNER).with_(timeout=10).should(be.not_.visible)


def get_fresh_document_label():
    new_item_yellow = s(NEW_DOCUMENT_YELLOW_ROW)
    new_item_yellow.should(be.visible)
    document = new_item_yellow.get(query.text)
    label = document.split('\n')[0]
    return label
