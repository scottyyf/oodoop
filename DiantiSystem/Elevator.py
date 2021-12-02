#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Elevator.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from queue import PriorityQueue
from enum import Enum

from utils import GateStatus


class Elevator(object):
    """a elevator handle exacy require to up or down"""
    def __init__(self, weight_limit=2000):
        self._up_queues = PriorityQueue()
        self._down_queues = PriorityQueue()
        self._set = set()

        self._gate_status = GateStatus.CLOSE
        self._buttons = []
        self._weight_limit = weight_limit
        self._curren_level = 'x'
        self._direction = None

    def take_external_request(self, request):
        pass

    def take_internal_request(self, request):
        pass

    def open_gate(self):
        self._gate_status = GateStatus.OPEN

    def close_gate(self):
        self._gate_status = GateStatus.CLOSE
