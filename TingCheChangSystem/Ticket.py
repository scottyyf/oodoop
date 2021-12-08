#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Ticket.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from datetime import datetime


class Ticket(object):
    def __init__(self, spots, vehicle):
        self._spots = spots
        self._vehicle = vehicle
        self._start_time = datetime.now()

    def spots(self):
        return self._spots

    def vehicle(self):
        return self._vehicle

    def start_time(self):
        return self._start_time
