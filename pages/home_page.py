# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find


class TopMenu(WebElement):
    logo_a = Find(by=By.CLASS_NAME, value='site-anchor')
    home_a = Find(by=By.LINK_TEXT, value='Home')
    about_us_a = Find(by=By.LINK_TEXT, value='About us')
    services_a = Find(by=By.LINK_TEXT, value='Services')
    demo_li = Find(
        by=By.XPATH, value='//li[@id=\'menu-item-66\']'
    )
    draggable_a = Find(
        by=By.LINK_TEXT, value='Draggable'
    )
    tabs_a = Find(by=By.LINK_TEXT, value='Tabs')
    blog_a = Find(by=By.LINK_TEXT, value='Blog')
    contact_a = Find(by=By.LINK_TEXT, value='Contact')


class SideMenu(WebElement):
    registration_a = Find(
        by=By.LINK_TEXT, value='Registration'
    )
    draggable_a = Find(
        by=By.LINK_TEXT, value='Draggable'
    )
    droppable_a = Find(
        by=By.LINK_TEXT, value='Droppable'
    )
    resizable_a = Find(by=By.LINK_TEXT, value='Resizable')
    selectable_a = Find(
        by=By.LINK_TEXT, value='Selectable'
    )
    sortable_a = Find(by=By.LINK_TEXT, value='Sortable')
    accordion_a = Find(
        by=By.LINK_TEXT, value='Accordion'
    )
    autocomplete_a = Find(
        by=By.LINK_TEXT, value='Autocomplete'
    )
    datepicker_a = Find(
        by=By.LINK_TEXT, value='Datepicker'
    )
    menu_a = Find(by=By.LINK_TEXT, value='Menu')
    slider_a = Find(by=By.LINK_TEXT, value='Slider')
    tabs_a = Find(by=By.LINK_TEXT, value='Tabs')
    tooltip_a = Find(by=By.LINK_TEXT, value='Tooltip')
    frames_and_windows_a = Find(
        by=By.LINK_TEXT, value='Frames and windows'
    )


class HomePage(BasePage):
    top_menu = Find(
        TopMenu, By.CSS_SELECTOR, 'div.collapse'
    )
    side_menu = Find(SideMenu, By.ID, 'secondary')

    def __init__(self):
        super(HomePage, self).__init__(
            url='http://demoqa.com/'
        )

    def is_demo_dropdown_valid(self):
        self.top_menu.demo_li.click()
        return (
            self.top_menu.is_element_present('draggable_a')
            and
            self.top_menu.is_element_present('tabs_a')
        )
