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

# Jenkins
VOLUME /jenkins_home
VOLUME /test_results

# Install Allure report
RUN apt-get install software-properties-common -y
RUN apt-add-repository ppa:qameta/allure && apt-get update && apt-get install allure

# Change user for Jenkins
USER jenkins
