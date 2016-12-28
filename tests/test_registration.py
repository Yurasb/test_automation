# -*- coding: utf-8 -*-
import allure


@allure.feature('Registration')
@allure.story('Valid user')
def test_register_user(reg_page, valid_user):
    reg_page.open()
    reg_page.register_user(valid_user)
    assert reg_page.is_registration_success(), (
        'Registration failed with user:'
        ' first name - {first_name},'
        ' last name - {last_name},'
        ' phone - {phone},'
        ' password - {password},'
        ' confirm password - {confirm_password}'.format(
            first_name=valid_user.first_name,
            last_name=valid_user.last_name,
            phone=valid_user.phone,
            password=valid_user.password,
            confirm_password=valid_user.confirm_password
        )
    )


@allure.feature('Registration')
@allure.story('Invalid user')
def test_not_register_user(reg_page, invalid_user):
    reg_page.open()
    reg_page.register_user(invalid_user)
    assert reg_page.is_registration_failed(), (
        'Registration is not failed with user:'
        ' first name - {first_name},'
        ' last name - {last_name},'
        ' phone - {phone},'
        ' password - {password},'
        ' confirm password - {confirm_password}'.format(
            first_name=invalid_user.first_name,
            last_name=invalid_user.last_name,
            phone=invalid_user.phone,
            password=invalid_user.password,
            confirm_password=invalid_user.confirm_password
        )
    )
