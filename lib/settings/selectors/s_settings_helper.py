from selene.api import by, s, ss

FIELD_ID = 'l-auth-login'
ELEMENTS = {'css': f'#{FIELD_ID}',
            'xpath': f"//input[@id='{FIELD_ID}']",
            'selenium_element': 'web_element',
            'selene_element': s(f'#{FIELD_ID}'),
            'selene_collection': ss(f'#{FIELD_ID}'),
            'by': by.xpath(f"//input[@id='{FIELD_ID}']")}
