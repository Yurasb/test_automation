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

    def __str__(self):
        return (
            'User[firstname={first_name},'
            ' lastname={last_name},'
            ' phone={phone},'
            ' username={username},'
            ' email={email},'
            ' description={description},'
            ' password={password},'
            ' confirm password={confirm_password}]'.format(
                first_name=self.first_name,
                last_name=self.last_name,
                phone=self.phone,
                username=self.username,
                email=self.email,
                description=self.description,
                password=self.password,
                confirm_password=self.confirm_password
            )
        )
