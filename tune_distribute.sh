#!/bin/bash

sudo python3 setup.py sdist --format=zip,gztar
sudo python3 setup.py bdist_egg