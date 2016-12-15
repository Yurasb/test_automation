# -*- coding: utf-8 -*-

from tinydb import TinyDB

from data.user import User


user_db = TinyDB(
    '../data/user_db.json',
    default_table='valid_user_data'
)


class Collection(object):
    VALID = user_db.table(name='valid_user_data')


def get_user_by(collection, index):
    return User(
        first_name=collection.get(eid=index)['first_name'],
        last_name=collection.get(eid=index)['last_name'],
        phone=collection.get(eid=index)['phone'],
        password=collection.get(eid=index)['password'],
        confirm_password=collection.get(eid=index)['confirm_password']
    )
