#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Reservation.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Reservation(object):
    def __init__(self, tables, timeslot):
        self._tables = tables
        self._timeslot = timeslot

    def tables(self):
        return self._tables

    def timeslot(self):
        return self._timeslot
