# -*- coding: utf-8 -*-
from tinydb import TinyDB

from data.user import User


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
