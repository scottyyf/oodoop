#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Order.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from typing import List

from Meal import Meal


class Order(object):
    def __init__(self, tables, menu: List[Meal]):
        self._menu = menu
        self._tables = tables

    def calculate_price(self, init=0, off=1):
        ret = init
        for meal in self._menu:
            ret += meal.price()

        return ret * off

    def tables(self):
        return self._tables
