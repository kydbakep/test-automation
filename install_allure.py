import os

link = 'https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.2/allure-commandline-2.13.2.zip'

os.system(f"wget {link}")
os.system("unzip allure-commandline-2.13.2.zip")
os.system("rm -rf allure-commandline-2.13.2.zip")

os.system("mkdir /usr/share/allure")
os.system("cp -r allure-2.13.2/* /usr/share/allure")
os.system("rm -rf allure-2.13.2")

os.system("ln -s /usr/share/allure/bin/allure /usr/local/bin/allure")
