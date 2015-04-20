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
    make install