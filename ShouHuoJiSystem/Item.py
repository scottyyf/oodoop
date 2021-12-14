#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Item.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Item(object):
    _name = None

    @property
    def name(self):
        return self._name


class Coffee(Item):
    _name = 'Coffee'


class Water(Item):
    _name = 'Water'
