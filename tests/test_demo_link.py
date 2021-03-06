# -*- coding: utf-8 -*-
import allure


@allure.feature('Top menu')
@allure.story('Demo dropdown')
def test_demo_link(home_page):
    home_page.open()
    assert home_page.is_demo_dropdown_valid(), (
        'Expected elements are not found'
    )
