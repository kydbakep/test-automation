import os

from selene.api import config
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options as Chrome

from lib.url.lib_url import DEV_URL, NEXT_URL

BROWSER_NAME = 'chrome'
HEADLESS_MODE = False


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


def set_base_url(url=get_default_url()):
    config.base_url = url


def get_configured_chrome(headless=HEADLESS_MODE):
    chrome_options = Chrome()
    if headless:
        print('\nBrowser will start in headless mode!')
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument("--enable-automation")
    chrome_options.add_argument("--start-maximized")
    configured = webdriver.Chrome(options=chrome_options, executable_path=get_driver_path('chromedriver'))
    return configured


class Settings:
    def __init__(self, headless=HEADLESS_MODE):
        set_base_url()
        if headless:
            browser.set_driver(get_configured_chrome(headless))
        else:
            browser.set_driver(get_configured_chrome(headless=False))
