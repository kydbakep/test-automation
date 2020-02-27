import os
import requests
from scrapy import Selector
import subprocess as s

job = s.Popen(['/opt/google/chrome/chrome', '--version'], stdout=s.PIPE)
browser_version = str(job.communicate(None)[0]).split(' ')[2]
version_without_minor = browser_version[:-4:]

page = requests.get('https://chromedriver.chromium.org/downloads').text
parsed = Selector(text=page).xpath(f"//a[contains(@name, '{version_without_minor}')]//ancestor::h2/span/a").get()
download_page = parsed.split('"')[1]
file_link = str(download_page).replace('index.html?path=', '') + 'chromedriver_linux64.zip'

os.system(f"wget {file_link}")
os.system("unzip chromedriver_linux64.zip")
os.system("rm -rf chromedriver_linux64.zip")

os.system("mkdir /usr/share/chromedriver")
os.system("cp -r chromedriver /usr/share/chromedriver")
os.system("rm -rf chromedriver")

os.system("ln -s /usr/share/chromedriver/chromedriver /usr/local/bin/chromedriver")
