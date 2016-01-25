#!/bin/bash

find tune_reporting/ -type f -name '*.py' -exec sed -i 's/ *$//' '{}' ';'
find tune_reporting/ -type f -name '*.md' -exec sed -i 's/ *$//' '{}' ';'

find examples/ -type f -name '*.py' -exec sed -i 's/ *$//' '{}' ';'
find examples/ -type f -name '*.md' -exec sed -i 's/ *$//' '{}' ';'

find tests/ -type f -name '*.py' -exec sed -i 's/ *$//' '{}' ';'
find tests/ -type f -name '*.md' -exec sed -i 's/ *$//' '{}' ';'

find . -type f -name '*.sh' -exec sed -i 's/ *$//' '{}' ';'
find . -type f -name 'README.*' -exec sed -i 's/ *$//' '{}' ';'