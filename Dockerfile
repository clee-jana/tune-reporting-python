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

# Install Python 2.7
RUN yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel mysql-devel
RUN yum install -y which redhat-lsb-core wget gcc gcc-c++ make kernel-devel

RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
RUN export PATH="$HOME/.pyenv/bin:$PATH"
RUN eval "$(pyenv init -)"
RUN eval "$(pyenv virtualenv-init -)"
RUN which pyenv
RUN pyenv --version

RUN pyenv install -l | grep 2.7
RUN pyenv install 2.7.8
RUN pyenv local 2.7.8
RUN python --version

# Install pip
RUN     yum install -y python-pip
RUN     pip --version

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