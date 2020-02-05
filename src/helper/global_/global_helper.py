from selenium.webdriver.support.select import Select


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


def set_select_option(select_element_selector, name: str):
    node = select_element_selector
    select = Select(node)
    select.select_by_visible_text(name)
