#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Table.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Table(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._available = True

    def is_available(self):
        return self._available

    def capacity(self):
        return self._capacity

    def current_capacity(self):
        return self._capacity

    def mark_unavailable(self):
        self._available = False

    def mark_available(self):
        self._available = True
