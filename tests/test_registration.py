# -*- coding: utf-8 -*-
import allure


@allure.feature('Registration')
@allure.story('Valid user')
def test_register_user(reg_page, valid_user):
    reg_page.open()
    reg_page.register_user(valid_user)
    assert reg_page.is_registration_success(), (
        'User is not registered or confirmation text is wrong'
    )


@allure.feature('Registration')
@allure.story('Invalid user')
def test_not_register_user(reg_page, invalid_user):
    reg_page.open()
    reg_page.register_user(invalid_user)
    assert reg_page.is_registration_failed(), (
        'No error message found or user registered'
    )
