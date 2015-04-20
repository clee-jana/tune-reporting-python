# TUNE Reporting SDK for Python
# Dockerfile for Jenkins CI
# Update:  $Date: 2015-04-17 16:00:00 $

FROM docker-dev.ops.tune.com/itops/base_centos6:latest

MAINTAINER jefft@tune.com

RUN echo -----------------------------
lsb_release -a
RUN echo -----------------------------


RUN yum -y update && \
    yum -y clean all

RUN yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel kernel-devel which redhat-lsb-core wget gcc gcc-c++ make xz-libs tar

RUN wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz && \
    tar zxvf Python-2.7.9.tgz && \
    cd Python-2.7.9 && \
    ./configure && \
    make && \
    make install && \
    python2.7 -V && \
    python2.7 -m ensurepip && \
    mkdir -p /data/tune-reporting-python && \
    mkdir -p /var/has/data/tune-reporting-python

COPY . /data/tune-reporting-python

WORKDIR /data/tune-reporting-python

RUN pip install -r requirements.txt && \
    python2.7 setup.py clean && \
    python2.7 setup.py build && \
    python2.7 setup.py install && \
    python2.7 ./tests/tune_reporting_tests.py b951b30cc17b6a77dad4f1ef1471bd5d