# -*- coding: utf-8 -*-

import pytest
import webium.settings
from selenium import webdriver
from webium.driver import close_driver

from data.user import User
from pages.home_page import HomePage
from pages.drag_and_drop import DraganddropPage
from pages.registration import RegistrationPage
from utils.user_storage import get_valid_user_by, get_invalid_user_by


@pytest.fixture(scope='session')
def reg_page():
    return RegistrationPage()


@pytest.fixture(scope='session', params=range(4))
def valid_user(request):
    return get_valid_user_by(request.param)


@pytest.fixture(scope='session', params=range(7))
def invalid_user(request):
    return get_invalid_user_by(request.param)


@pytest.fixture(scope='session')
def dnd_page():
    return DraganddropPage()


@pytest.fixture(scope='session')
def home_page():
    return HomePage()


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
