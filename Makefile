# Makefile for django-ldap-basic-auth

# default:
#   @awk -F\: '/^[a-z_]+:/ && !/default/ {printf "- %-20s %s\n", $$1, $$2}' Makefile
	
help:
	@echo
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "	 clean		to clean garbage left by builds and installation"
	@echo "	 compile	to compile .py files (just to check for syntax errors)"
	@echo "	 install	to install"
	@echo "	 build		to build without installing"
	@echo "	 dist		to create egg for distribution"
	@echo "	 test		to run tests"
	@echo "	 publish	to publish the package to PyPI"
	@echo "	 register	to register the package to PyPI"
	@echo

clean:
	@echo "Cleaning..."
	@rm -rf build dist *.egg-info *.pyc **/*.pyc *~

test: test
	@cd testproject; python manage.py test simple_app

compile: compile
	@echo "Compiling source code..."
	@python -tt -m compileall simple_audit
	@python -tt -m compileall tests

register: register
	@python setup.py register

install: install
	@python setup.py install

build: build
	@python setup.py build

dist: clean
	@python setup.py sdist

upload: upload
	@python setup.py sdist upload -r pypi

publish: upload
	@bash make_tag.sh
