# -*- coding: utf-8 -*-
from uuid import uuid4
import hashlib


def get_next_username():
    code = str(uuid4())
    return hashlib.md5(code).hexdigest()[:30]