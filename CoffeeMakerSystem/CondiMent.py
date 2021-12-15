#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: CondiMent.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Condiment(object):
    def __init__(self, desc, price):
        self._desc = desc
        self._price = price

    def get_price(self):
        return self._price

    def get_desc(self):
        return self._desc

    def add(self, num=1):
        for _ in range(num):
            self._price += self._price


class Milk(Condiment):
    def __init__(self, desc='milk', price=1):
        super(Milk, self).__init__(desc, price)


class Coco(Condiment):
    def __init__(self, desc='coco', price=2):
        super(Coco, self).__init__(desc, price)
