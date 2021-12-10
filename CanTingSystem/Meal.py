#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Meal.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Meal(object):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def name(self):
        return self._name

    def price(self):
        return self._price
