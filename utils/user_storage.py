# -*- coding: utf-8 -*-
from tinydb import TinyDB

from utils import random_string


VALID = 'valid_user_data'
INVALID = 'invalid_user_data'

user_db = TinyDB(
    '../data/user_db.json',
    default_table=VALID
)


def get_valid_user_by(index):
    user_data = user_db.table(name=VALID).get(eid=index)
    return User(**user_data)


def get_invalid_user_by(index):
    user_data = user_db.table(name=INVALID).get(eid=index)
    return User(**user_data)


class User(object):
    def __init__(
            self, first_name, last_name, phone, password,
            confirm_password
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.username = random_string()
        self.email = '{0}@mail.com'.format(random_string())
        self.description = 'About me'
        self.image = '../data/upload_image.jpg'
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
