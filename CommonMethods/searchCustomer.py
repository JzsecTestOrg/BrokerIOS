# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

import re


def search(condition, result):
    m = re.search(str(condition), str(result))
    if m is not None:
        return True
    else:
        return False
