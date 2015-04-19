# TUNE Reporting SDK for Python
# Dockerfile for Jenkins CI
# Update:  $Date: 2015-04-17 16:00:00 $

FROM docker-dev.ops.tune.com/itops/base_centos6:latest

MAINTAINER jefft@tune.com

# EPEL (Extra Packages for Enterprise Linux) repository that
# is available for CentOS and related distributions.

RUN yum -y update && \
    yum -y install tar && \
    yum -y clean all 
    
RUN yum groupinstall "Development tools"
RUN yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel kernel-devel
RUN yum install -y which redhat-lsb-core wget gcc gcc-c++ make xz-libs tar

RUN wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tar.bz2
RUN tar xf Python-2.7.6.tar.bz2
RUN cd Python-2.7.6
RUN ./configure --prefix=/usr/local

# should display now 2.7.5 or later: 
RUN python -V 

# now install pip for 2.7 
RUN curl http://peak.telecommunity.com/dist/ez_setup.py > /tmp/ez_setup.py
RUN python /tmp/ez_setup.py -U setuptools

RUN easy_install virtualenv
RUN easy_install virtualenvwrapper

# should display current versions:
RUN pip -V && virtualenv --version

# Install pip module configparser required for tune-reporting-python
RUN     pip install -r configparser
RUN     pip freeze | grep 'configparser'

# Build tune-reporting Python module
RUN     python setup.py clean
RUN     python setup.py build
RUN     python setup.py install

# Build
RUN make build

# Perform tests
RUN make test api_key=b951b30cc17b6a77dad4f1ef1471bd5d