from selene.api import s, by
from selene.support.conditions.be import visible, in_dom

from src.helper.global_.selectors.sel_main_page import AVATAR_SEL


class PageMain:
    def __init__(self):
        self.__avatar = s(AVATAR_SEL)

    def is_current_user(self, first_name, last_name):
        self.__avatar.should_be(visible)
        s(by.xpath(f"//li[contains(text(), '{first_name} {last_name}')]")).should_be(in_dom)
        return True
