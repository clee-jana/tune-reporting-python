#!/bin/bash

sudo rm -fR build/*
sudo python setup.py clean
sudo python setup.py build
sudo python setup.py install
# sudo python3 setup.py publish