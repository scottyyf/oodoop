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
        # [row1, row2, row3]
        self._list_rows = []

    def get_available_count(self):
        return self._available_count

    def add_available_count(self, ticket):
        for _ in ticket.spots():
            self._available_count += 1
            _.leave_spot()

    def release_available_count(self, ticket):
        for _ in ticket.spots():
            self._available_count -= 1
            _.take_spot()

    def find_spots_for_vehicle(self, vehicle):
        # TODO
        pass


class Rows:
    def __init__(self, spots: list):
        self._spots = spots

    def spots(self):
        return self._spots
