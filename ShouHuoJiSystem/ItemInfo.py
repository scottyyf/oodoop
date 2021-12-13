#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: ItemInfo.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from TException import NoEnoughItemError


class ItemInfo(object):
    def __init__(self, price, items=None):
        self._price = price
        self._items = items if items else []

    def get_price(self):
        return self._price

    def add_item(self, item):
        self._items.append(item)

    def get_and_remove_item(self):
        if not self._items:
            raise NoEnoughItemError('no goods any more, refill needed')

        item = self._items.pop(0)
        return item

    def clean_item(self):
        ret = self._items
        self._items = []
        return ret
