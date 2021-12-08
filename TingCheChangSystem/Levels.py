#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Levels.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Levels:
    def __init__(self):
        self._available_count = 0
        self._list_rows = []

    def get_available_count(self):
        return self._available_count

    def update_available_count(self):
        pass

    def find_spots_for_vehicle(self, vehicle):
        # 这里应该是一个岛屿的问题,连续问题
        pass


class Rows:
    def __init__(self, spots):
        self._spots = spots
