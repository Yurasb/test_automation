# -*- coding: utf-8 -*-
import allure


@allure.feature('Failure')
@allure.story('Simple failed test')
def test_fail(home_page):
    home_page.open()
    assert home_page.is_page_name_expected(), ('Failed'
                                               ' just as planned')
