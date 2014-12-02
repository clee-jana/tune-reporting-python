#   Makefile
#
#   Copyright (c) 2014 Tune, Inc
#   All rights reserved.
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.
#
# category  Tune
# package   tune.tests
# author    Jeff Tanner <jefft@tune.com>
# copyright 2014 Tune (http://www.tune.com)
# license   http://opensource.org/licenses/MIT The MIT License (MIT)
# update    $Date: 2014-12-02 12:30:00 $
# version   $Version: 0.9.16 $
# link      https://developers.mobileapptracking.com
#

.PHONY: clean venv install analysis examples tests tests-travis-ci tests-install build dist register docs-sphinx docs-doxygen

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install . --use-mirrors

tests-install: install
	. venv/bin/activate; pip install -r tests/requirements.txt

clean:
	sudo rm -fR ./build/*
	sudo rm -fR ./docs/doxygen/*
	sudo rm -fR ./docs/sphinx/_build
	sudo rm -fR build/*
	rm -rf venv

dist-install:
	sudo pip install -r requirements.txt

dist:
	sudo rm -fR ./dist/*
	sudo python setup.py sdist --format=zip,gztar
	sudo python setup.py bdist_egg
	sudo python setup.py bdist_wheel

build:
	sudo python setup.py clean
	sudo python setup.py build
	sudo python setup.py install

register:
	sudo python setup.py register

tests:
	python ./tests/tune_tests.py $(api_key)
	
tests-travis-ci:
	flake8 --ignore=F401,E265,E129 tune
	flake8 --ignore=E123,E126,E128,E265,E501 tests
	python ./tests/tune_tests.py $(api_key)

examples:
	python ./examples/tune_examples.py $(api_key)

analysis: install
	. venv/bin/activate; flake8 --ignore=E123,E126,E128,E265,E501 examples
	. venv/bin/activate; flake8 --ignore=E123,E126,E128,E265,E501 tests
	. venv/bin/activate; flake8 --ignore=F401,E265,E129 tune
	. venv/bin/activate; pylint --rcfile ./tools/pylintrc tune

docs-install:
	. venv/bin/activate; pip install -r docs/sphinx/requirements.txt

docs-sphinx: docs-install
	sudo rm -fR ./docs/sphinx/_build
	cd docs/sphinx && make html
	x-www-browser docs/sphinx/_build/html/index.html

docs-doxygen:
	sudo rm -fR ./docs/doxygen/*
	sudo doxygen docs/Doxyfile
	x-www-browser docs/doxygen/html/index.html

