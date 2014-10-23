#!/bin/bash

if [ $# -ne 1 ]; then
    echo usage: $0 directory
    exit 1
fi

directory=$1

pylint --rcfile ./scripts/pclintrc $directory
