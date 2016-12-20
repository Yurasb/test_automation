# -*- coding: utf-8 -*-

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webium import Find

from pages.home_page import HomePage


class DraganddropPage(HomePage):
    def __init__(self):
        super(HomePage, self).__init__(
            url='http://demoqa.com/droppable/'
        )

    drag_div = Find(by=By.XPATH,
                    value='//div[@id=\'draggableview\']')
    drop_div = Find(by=By.XPATH,
                    value='//div[@id=\'droppableview\']')
    dropped_message = Find(by=By.XPATH,
                           value='//div[@id=\'droppableview\']/p')

    def drag_and_drop(self, drag, drop):
        ActionChains(self._driver).drag_and_drop(drag,
                                                 drop).perform()

    def is_drag_and_drop_success(self):
        return self.dropped_message.text == 'Dropped!'
