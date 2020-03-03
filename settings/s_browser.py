import os

from selene.api import config
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options as Chrome

from lib.url.lib_url import NEXT_URL

BROWSER_NAME = 'chrome'
HEADLESS_MODE = True
SET_VALUES_BY_JS = False


def get_default_url(url=NEXT_URL):
    if os.environ.get('ci_url'):
        address = os.environ['ci_url']
    else:
        address = url
    return address


def get_driver_path(driver_='chromedriver'):
    if os.name == 'posix':
        path = f'/usr/local/bin/{driver_}'
    else:
        path = f'C:\\drivers\\{driver_}.exe'
    return path


def get_configured_chrome(headless=False):
    chrome_options = Chrome()
    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--enable-automation')
    chrome_options.add_argument('--window-size=1920,1080')
    configured = webdriver.Chrome(options=chrome_options, executable_path=get_driver_path('chromedriver'))
    return configured


class Settings:
    def __init__(self, url_: str = None):
        default_url = url_ or get_default_url()
        config.set_value_by_js = SET_VALUES_BY_JS
        config.base_url = default_url

        # Disable saving screenshots, because we use allure_screenshot fixture
        config.reports_folder = 'reports'
        config.save_page_source_on_failure = False
        config.save_screenshot_on_failure = False
        config.driver = get_configured_chrome(HEADLESS_MODE)
