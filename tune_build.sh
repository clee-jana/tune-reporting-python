#!/bin/bash

sudo rm -fR build/*
sudo python3 setup.py clean
sudo python3 setup.py build
sudo python3 setup.py install
# sudo python3 setup.py publish