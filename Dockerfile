FROM python:3.8.1-buster

ARG WORKDIR=/home/orderry
RUN mkdir $WORKDIR
WORKDIR = $WORKDIR
ADD . $WORKDIR

#RUN mkdir /.selene && mkdir /.selene/screenshots
#RUN chmod -R ugo-+rw /.selene
RUN chmod -R ugo-+rw /home

RUN cd $WORKDIR && python -m venv env && . ./env/bin/activate
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r $WORKDIR/requirements.txt

# Install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update
RUN apt-get -qqy install google-chrome-stable vim mc

# Install chromedriver
RUN python $WORKDIR/install_chromedriver.py
