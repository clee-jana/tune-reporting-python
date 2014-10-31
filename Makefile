.PHONY: clean venv install analysis tests tests-install build dist register

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install . --use-mirrors

tests-install: install
	. venv/bin/activate; pip install -r tests/requirements.txt

clean:
	sudo rm -fR build/*
	rm -rf venv

dist-install:
	sudo pip install -r requirements.txt
	
dist:
	sudo rm -fR ./dist/*
	sudo python setup.py sdist --format=zip,gztar
	sudo python setup.py bdist_egg
	sudo python3 setup.py bdist_egg
	sudo python setup.py bdist_wheel

build: analysis
	sudo rm -fR ./build/*
	sudo python setup.py clean
	sudo python setup.py build
	sudo python setup.py install

register:
	sudo python setup.py register

tests:
	. venv/bin/activate; python ./tests/tune_tests.py $(api_key)

examples: install
	. venv/bin/activate; python ./examples/tune_examples.py $(api_key)

analysis:
	. venv/bin/activate; flake8 --ignore=E123,E126,E128,E265,E501 examples
	. venv/bin/activate; flake8 --ignore=E123,E126,E128,E265,E501 tests
	. venv/bin/activate; flake8 --ignore=F401 tune

docs:
	sudo rm -fR ./doc/doxygen/*
	sudo doxygen ./doc/Doxyfile

