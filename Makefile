.PHONY: all help venv deps test

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  all            => to execute all targets"
	@echo "  venv           => to create a virtualenv"
	@echo "  deps           => to install Python packages"
	@echo "  test           => to execute all tests"

venv:
ifndef IS_VIRTUALENV_INSTALLED
	$(error "Please, install virtualenv with python 2.7")
endif
	@virtualenv venv

deps:
	@venv/bin/pip install -U -r .meta/packages
	@sudo make apt-add-repository ppa:yandex-qatools/allure-framework
	@sudo make apt-get update
	@sudo make apt-get install allure-commandline

test:
	@venv/bin/python main.py
	@allure generate allure-report/
	@allure report open

all: venv deps test