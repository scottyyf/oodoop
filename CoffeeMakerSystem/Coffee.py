#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Coffee.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Coffee(object):
    def __init__(self, coffee_pack):
        self._price = coffee_pack.get_price()
        self._extra_desc = [coffee_pack.get_desc()]

        self._coffee_pack = coffee_pack

    def get_price(self):
        return self._price

    def add(self, extra):
        self._price += extra.get_price()
        self._extra_desc.append(extra.get_desc())

    def get_desc(self):
        return ', '.join(self._extra_desc)
