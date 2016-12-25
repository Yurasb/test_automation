# -*- coding: utf-8 -*-
import utils


class User(object):
    def __init__(
            self, first_name, last_name, phone, password,
            confirm_password
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.username = utils.random_string()
        self.email = '{0}@mail.com'.format(
            utils.random_string()
        )
        self.description = 'About me'
        self.image = 'Upload_image.jpg'
        self.password = password
        self.confirm_password = confirm_password
