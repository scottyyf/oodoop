#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Party.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Party(object):
    def __init__(self, capacity):
        self._capacity = capacity

    def get_capacity(self):
        return self._capacity
