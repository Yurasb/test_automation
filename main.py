# -*- coding: utf-8 -*-
import pytest
import yaml


with open('./config.yaml', 'r') as stream:
    configuration = yaml.load(stream)

pytest.main(['./tests/',  '--alluredir=./allure-report/'])
