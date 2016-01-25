#!/bin/bash

export TZ=America/Los_Angeles

changed_files=`git diff --name-only`
deleted_files=`git ls-files --deleted`
added_files=`git ls-files --others --exclude-standard`

today=`date +%F' '%T' '%Z`

echo $today

for f in $changed_files
do
    if [ -f $f ]; then
        printf -v sed_repl 's/Date: [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [A-Z]{3}/Date: %q/g' "$today"
        sed -r -i "$sed_repl" $f
    fi
done


for f in $added_files
do
    if [ -f $f ]; then
        printf -v sed_repl 's/Date: [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [A-Z]{3}/Date: %q/g' "$today"
        sed -r -i "$sed_repl" $f
    fi
done

