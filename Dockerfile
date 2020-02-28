FROM python:3.8.2-buster

EXPOSE 9091

ARG WORKDIR=/home/orderry
RUN mkdir $WORKDIR
RUN mkdir $WORKDIR/.local
RUN mkdir $WORKDIR/.local/bin

ADD requirements.txt $WORKDIR
ADD install_chromedriver.py $WORKDIR

RUN useradd -ms /bin/bash orderry
RUN chown -R orderry $WORKDIR
ENV PATH="$WORKDIR/.local/bin:$PATH"

WORKDIR = $WORKDIR
#USER orderry
RUN cd $WORKDIR && python -m venv env && . ./env/bin/activate
RUN pip install --upgrade pip setuptools wheel

RUN pip install -r $WORKDIR/requirements.txt

# Install google chrome
#USER root
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update
RUN apt-get -qqy install google-chrome-stable vim mc

# Install chromedriver
RUN python $WORKDIR/install_chromedriver.py

# TODO: VOLUMES
# todo: link folder to get tests
# todo: link folder to save results and screenshots
# todo: use that container on host machine