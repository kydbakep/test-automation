FROM jenkins/jenkins:lts
LABEL maintainer="a.svarych@gmail.com"
EXPOSE 9090

USER root
RUN apt-get update && apt-get install apt-utils vim mc build-essential checkinstall libreadline-gplv2-dev \
libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev wget -y

# Install python 3.8.2
WORKDIR = /opt
RUN wget "https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz" && tar xzf Python-3.8.2.tgz && \
Python-3.8.2/configure --enable-optimizations && make altinstall

RUN python3.8 -m pip install --upgrade pip setuptools wheel

ADD requirements.txt .
ADD install_chromedriver.py .
RUN python3.8 -m pip install -r requirements.txt

# Install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
apt-get update && apt-get -qqy install google-chrome-stable vim mc apt-utils nano

# Install chromedriver
RUN python3.8 install_chromedriver.py

# Install Allure report
ARG ALLURE_LINK=https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.2/allure-commandline-2.13.2.zip
RUN wget $ALLURE_LINK && unzip allure-commandline-2.13.2.zip && chmod +x allure-2.13.2/bin/allure && \
ln allure-2.13.2/bin/allure /usr/local/bin/allure

RUN cd '/= ' && ./opt/allure-2.13.2/bin/allure --version

# Change user for Jenkins
USER jenkins
