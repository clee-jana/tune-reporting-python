# TUNE Reporting SDK for Python
# Dockerfile for Jenkins CI
# Update:  $Date: 2015-07-30 12:49:27 $

FROM docker-dev.ops.tune.com/itops/base_centos6:latest

MAINTAINER Jeff Tanner jefft@tune.com

RUN echo -----------------------------
lsb_release -a
RUN echo -----------------------------

# install system packages
RUN yum -y update && \
    yum -y install gcc curl zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tar && \
    yum -y clean all

# change to root home
WORKDIR /root

# install pyenv
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

# set pyenv variables
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# install python
RUN pyenv install 3.4.2 && \
    pyenv global 3.4.2 && \
    pyenv rehash && \
    python -V && \
    mkdir -p /data/tune-reporting-python && \
    mkdir -p /var/has/data/tune-reporting-python

COPY . /data/tune-reporting-python

CMD echo "image tunesdk/tune-reporting-python-setup"