.PHONY: all help venv deps test

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  all            => to execute all targets"
	@echo "  venv           => to create a virtualenv"
	@echo "  deps           => to install Python packages"
	@echo "  test           => to execute all tests"

venv:
	@virtualenv venv

deps:
	@venv/bin/pip install -U -r .meta/packages

test:
	@venv/bin/python main.py
	@allure generate allure-report/
	@allure report open

all: venv deps test