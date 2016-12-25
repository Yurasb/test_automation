# -*- coding: utf-8 -*-


def test_demo_link(home_page):
    home_page.open()
    assert home_page.is_demo_dropdown_valid()
