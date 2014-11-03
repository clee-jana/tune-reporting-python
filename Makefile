.PHONY: clean venv install analysis tests tests-install build dist register docs-sphinx docs-doxygen

path_to_python3=$(which python3)

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install . --use-mirrors

tests-install: install
	. venv/bin/activate; pip install -r tests/requirements.txt

clean:
	sudo rm -fR ./doc/doxygen/*
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

tests: build
	python ./tests/tune_tests.py $(api_key)

examples: build
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
	
docs-doxygen:
	sudo rm -fR ./docs/doxygen/*
	sudo doxygen docs/Doxyfile
