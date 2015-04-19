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
RUN yum install -y which redhat-lsb-core wget gcc gcc-c++ make kernel-devel xz-libs tar
# install build tools 
sudo yum install make automake gcc gcc-c++ kernel-devel git-core -y 

# install python 2.7 and change default python symlink 
RUN yum install python27-devel -y 
RUN rm /usr/bin/python
RUN ln -s /usr/bin/python2.7 /usr/bin/python 

# yum still needs 2.6, so write it in and backup script 
RUN cp /usr/bin/yum /usr/bin/_yum_before_27 
RUN sed -i s/python/python2.6/g /usr/bin/yum 
RUN sed -i s/python2.6/python2.6/g /usr/bin/yum 

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