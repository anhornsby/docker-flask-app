FROM ubuntu:latest
MAINTAINER Adam Hornsby "adamhornn@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install curl
RUN apt-get -y install sudo
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get -y install nodejs
RUN apt-get -y install build-essential
RUN npm install
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt