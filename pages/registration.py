# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from webium import Find

from pages.home_page import HomePage


class RegistrationPage(HomePage):
    def __init__(self):
        super(HomePage, self).__init__(
            url='http://www.demoqa.com/registration/'
        )

    first_name_input = Find(
        by=By.NAME, value='first_name'
    )
    last_name_input = Find(
        by=By.NAME, value='last_name'
    )
    radiobutton_input = Find(
        by=By.NAME, value='radio_4[]'
    )
    checkbox_input = Find(
        by=By.XPATH, value='//input[@value=\'reading\']'
    )
    country_drop_down = Find(
        by=By.XPATH, value='//option[@value=\'Belarus\']'
    )
    month_drop_down = Find(by=By.XPATH,
                           value=('//select[@id="mm_date_8"]'
                                  '/option[@value="6"]')
                           )
    day_drop_down = Find(
        by=By.XPATH, value='//option[@value=\'15\']'
    )
    year_drop_down = Find(
        by=By.XPATH, value='//option[@value=\'1990\']'
    )
    phone_input = Find(
        by=By.NAME, value='phone_9'
    )
    username_input = Find(
        by=By.NAME, value='username'
    )
    email_input = Find(
        by=By.NAME, value='e_mail'
    )
    description_input = Find(
        by=By.NAME, value='description'
    )
    image_input = Find(
        by=By.XPATH,
        value='//input[@id=\'profile_pic_10\']'
    )
    password_input = Find(
        by=By.NAME, value='password'
    )
    confirm_password_input = Find(
        by=By.XPATH,
        value=('//input[@id="'
               'confirm_password_password_2"]')
    )
    submit_button = Find(
        by=By.NAME, value='pie_submit'
    )

    registration_message = Find(
        by=By.CLASS_NAME, value='piereg_message'
    )

    def register_user(self, data):
        self.first_name_input.send_keys(data.first_name)
        self.last_name_input.send_keys(data.last_name)
        self.radiobutton_input.click()
        self.checkbox_input.click()
        self.country_drop_down.click()
        self.month_drop_down.click()
        self.day_drop_down.click()
        self.year_drop_down.click()
        self.phone_input.send_keys(data.phone)
        self.username_input.send_keys(data.username)
        self.email_input.send_keys(data.email)
        self.description_input.send_keys(data.description)
        self.image_input.send_keys(data.image)
        self.password_input.send_keys(data.password)
        self.confirm_password_input.send_keys(
            data.confirm_password
        )
        self.submit_button.click()

    def is_registration_success(self):
        return self.registration_message.text == ('Thank you'
                                                  ' for your registration')
