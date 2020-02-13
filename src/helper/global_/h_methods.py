from selene.api import browser, be, s, ss, query
from selene.core.configuration import Config
from selene.core.entity import Element, Collection

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    StaleElementReferenceException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from src.helper.global_.selectors.sel_global_project import *


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
            displayed = selector_or_element.with_(Config(timeout=timeout)).matching(be.visible)
        elif type(selector_or_element) is Collection:
            displayed = selector_or_element[0].with_(Config(timeout=timeout)).matching(be.visible)
        elif type(selector_or_element) in (str, tuple):
            displayed = browser.with_(Config(timeout=timeout)).element(selector_or_element).matching(be.visible)
        else:
            raise TypeError(f'\nUnknown element or selector type: {selector_or_element}')
    except (TypeError, TimeoutException, NoSuchElementException,
            ElementNotVisibleException, StaleElementReferenceException) as e:
        print(f'\n\n!!! Exception handled:{e}\n\n')
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
        s(PRELOADER_SPINNER).should(be.not_.visible, 10)


def get_fresh_document_label():
    new_item_yellow = s(NEW_DOCUMENT_YELLOW_ROW)
    new_item_yellow.should(be.visible)
    document = new_item_yellow.get(query.text)
    label = document.split('\n')[0]
    return label
