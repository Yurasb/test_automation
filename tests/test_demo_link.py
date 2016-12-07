# -*- coding: utf-8 -*-


def test_demo_link(top_menu):
    top_menu.open()
    assert top_menu.is_demo_dropdown_valid()
