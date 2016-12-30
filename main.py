# -*- coding: utf-8 -*-

import yaml


with open('../config.yaml', 'r') as stream:
    configuration = yaml.load(stream)
