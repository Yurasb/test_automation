# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from webium import BasePage, Find


class TopMenu(BasePage):
    def __init__(self):
        super(TopMenu, self).__init__(
            url='http://demoqa.com/'
        )

    demo_li = Find(by=By.XPATH,
                   value='//li[@id=\'menu-item-66\']'
                   )
    draggable_a = Find(by=By.LINK_TEXT,
                       value='Draggable'
                       )
    tags_a = Find(by=By.LINK_TEXT,
                  value='Tabs'
                  )

    def is_demo_dropdown_valid(self):
        self.demo_li.click()
        return self.is_element_present('draggable_a') and\
            self.is_element_present('tags_a')
