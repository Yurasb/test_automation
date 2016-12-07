# -*- coding: utf-8 -*-

import random
import string


class User(object):
    def __init__(self):
        self.first_name = 'First Name'
        self.last_name = 'Last Name'
        self.phone = '3751234567'

        def random_string():
            return ''.join(
                random.choice(string.ascii_uppercase +
                              string.digits) for _ in range(7)
            )

        self.username = random_string()
        self.email = random_string() + '@mail.com'
        self.description = 'About me'
        self.image = '../data/upload_image.jpg'
        self.password = 'password'
        self.confirm_password = 'password'
