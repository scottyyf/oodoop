#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Book.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Book(object):
    def __init__(self, name, format):
        self._name = name
        self._format = format

    def get_name(self):
        return self._name

    def get_format(self):
        return self._format
