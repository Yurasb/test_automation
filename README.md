# test_automation
This is my task for test automation

### requirements
Project is optimized for running on Unix systems. Please, use virtual machine if it's needed.

### preparation
At first, install needed libs -`pip`, `virtualenv` and `Allure CLI`:
> sudo apt-get install python-pip

> sudo apt-get update

> sudo pip install virtualenv

 > sudo apt-add-repository ppa:yandex-qatools/allure-framework

 > sudo apt-get update

 > sudo apt-get install allure-commandline

### configuration
Open config.yaml and add platform, browser and its version, e.g.:
> platform:  Windows 7

> browser: chrome

> version: '52'

Note that `version` should be presented as string.

You could use [Saucelabs Platform Configurator] (https://wiki.saucelabs.com/display/DOCS/Platform+Configurator#/) for help.

Fill out `username` and `access_key` fields with provided Saucelabs username and access key.

### running
From root directory of the project run:
> make all

This will prepare virtualenv, install needed packages, run tests, generate report and open it.
