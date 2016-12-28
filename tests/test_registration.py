# -*- coding: utf-8 -*-
import allure


@allure.feature('Registration')
@allure.story('Valid user')
def test_register_user(reg_page, valid_user):
    reg_page.open()
    reg_page.register_user(valid_user)
    assert reg_page.is_registration_success(), (
        'Registration failed with {user}\n\n'.format(
            user=valid_user
        )
    )


@allure.feature('Registration')
@allure.story('Invalid user')
def test_not_register_user(reg_page, invalid_user):
    reg_page.open()
    reg_page.register_user(invalid_user)
    assert reg_page.is_registration_failed(), (
        'Registration did not fail with {user}\n\n'.format(
            user=invalid_user
        )
    )
