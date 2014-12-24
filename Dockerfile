# TUNE Reporting SDK for Python
# Dockerfile for Jenkins CI
# Update:  $Date: 2014-12-24 09:23:13 $

FROM docker-dev.ops.tune.com/itops/base_centos6:latest

MAINTAINER Jeff Tanner jefft@tune.com

# EPEL (Extra Packages for Enterprise Linux) repository that
# is available for CentOS and related distributions.

# Update the system applications
RUN     yum -y update

# Install EPEL Repository.
RUN     yum install epel-release

# Install Python 2.7
RUN     yum install python27
RUN     yum install python27-devel
RUN     python --version

# Install pip
RUN     yum -y install python-pip
RUN     pip --version

# Install pip module configparser required for tune-reporting-python
RUN     pip install -r configparser
RUN     pip freeze | grep 'configparser'

# Build tune-reporting Python module
RUN     python setup.py clean
RUN     python setup.py build
RUN     python setup.py install
RUN     pip freeze | grep 'tune-reporting'

# Perform tests
RUN     python ./tests/tune_reporting_tests.py