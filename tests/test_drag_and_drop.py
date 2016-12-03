# -*- coding: utf-8 -*-


def test_drag_and_drop(dnd_page):
    dnd_page.open()
    dnd_page.drag_and_drop(dnd_page.drag_div,
                           dnd_page.drop_div
                           )
    assert dnd_page.is_drag_and_drop_success()
