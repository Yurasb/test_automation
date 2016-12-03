# -*- coding: utf-8 -*-


def test_register_user(reg_page, user):
    reg_page.open()
    reg_page.register_user(user)
    assert reg_page.is_registration_success()
