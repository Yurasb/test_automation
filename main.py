# !/usr/bin/python

import sys

import pytest

configuration = [sys.argv[1], sys.argv[2]]

pytest.main(['./tests/', '--alluredir=./report/'])
