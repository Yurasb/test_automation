# -*- coding: utf-8 -*-


def test_register_user(reg_page, valid_user):
    reg_page.open()
    reg_page.register_user(valid_user)
    assert reg_page.is_registration_success()
