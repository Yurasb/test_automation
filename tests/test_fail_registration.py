# -*- coding: utf-8 -*-


def test_register_user(reg_page, invalid_user):
    reg_page.open()
    reg_page.register_user(invalid_user)
    assert reg_page.is_registration_failed()
