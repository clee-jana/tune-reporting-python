#!/bin/bash

sudo python setup.py sdist --format=zip,gztar
sudo python setup.py bdist_egg
sudo python3 setup.py bdist_egg