# -*- coding: utf-8 -*-

import pytest

from selenium import webdriver
from webium.driver import close_driver
import webium.settings

from data.user import User
from pages.drag_and_drop import DraganddropPage
from pages.registration import RegistrationPage


@pytest.fixture(scope='session')
def reg_page():
    return RegistrationPage()


@pytest.fixture(scope='session')
def user():
    return User()


@pytest.fixture(scope='session')
def dnd_page():
    return DraganddropPage()


@pytest.fixture(scope='session', autouse=True)
def setup_webdriver(request):
    def sauce_lab():
        desired_cap = {
            'platform': "Windows 7",
            'browserName': "firefox",
            'version': "47",
        }

        driver = webdriver.Remote(
            command_executor=('http://Sausage:Party'
                              '@ondemand.saucelabs.com:80/wd/hub'),
            desired_capabilities=desired_cap)

        return driver

    webium.settings.driver_class = sauce_lab

    def fin():
        close_driver()

    request.addfinalizer(fin)
