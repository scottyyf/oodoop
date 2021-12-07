#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Spot.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from TException import SpotOccupiedError


class Spot:
    def __init__(self, level, available=True):
        self._level = level
        self._available = available

    def is_available(self):
        return self._available

    def take_spot(self):
        if not self._available:
            raise SpotOccupiedError('spot is not available now')

        self._available = False
        self._level.update_available_count()

    def leave_spot(self):
        if self._available:
            return

        self._available = True
        self._level.update_available_count()