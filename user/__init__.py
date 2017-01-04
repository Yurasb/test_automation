# -*- coding: utf-8 -*-
import random
import string


def random_string():
    return ''.join(
        random.choice(string.ascii_uppercase +
                      string.digits) for _ in range(7)
    )
