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

# Install EPEL Repository.
RUN     yum install epel-release

# Install Python 2.7
RUN     yum install -y which redhat-lsb-core wget gcc-c++ make kernel-devel
RUN     yum install -y python27
RUN     yum install -y python27-devel
RUN     python --version

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
RUN     pip freeze | grep 'tune-reporting'

# Build
RUN make build

# Perform tests
RUN make test api_key=b951b30cc17b6a77dad4f1ef1471bd5d