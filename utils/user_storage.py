# -*- coding: utf-8 -*-
from tinydb import TinyDB

from data.user import User


user_db = TinyDB(
    '../data/user_db.json',
    default_table='valid_user_data'
)


def get_user_by(index):
    user_data = user_db.get(eid=index)
    return User(**user_data)
