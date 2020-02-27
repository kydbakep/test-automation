from selene.api import s, by, be

from lib.main.selectors.sel_main_page import AVATAR_SEL


class PageMain:
    def __init__(self):
        self.__avatar = s(AVATAR_SEL)

    def is_current_user(self, first_name, last_name):
        self.__avatar.should(be.visible)
        s(by.xpath(f"//li[contains(text(), '{first_name} {last_name}')]")).should(be.in_dom)
        return True
