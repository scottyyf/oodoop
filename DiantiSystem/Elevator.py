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

from DiantiSystem.utils import GateStatus, Direction
from Request import ExternalRequest


class Elevator(object):
    """a elevator handle exacy require to up or down"""
    def __init__(self, elevator_system, weight_limit=2000, name="admin"):
        self._up_queues = PriorityQueue()
        self._down_queues = PriorityQueue()
        self._up_set = set()
        self._down_set = set()

        self._gate_status = GateStatus.CLOSE
        self._buttons = []
        self._weight_limit = weight_limit
        self.name = name
        self._current_level = 10
        self._direction = Direction.IDLE

        self.elevator_system = elevator_system
        self.elevator_system.add_elevator(self)

    def take_external_request(self, request: ExternalRequest):
        if request.towards_up:
            self._add_request_to_up_queue(request)

        if request.towards_down:
            self._add_request_to_down_queue(request)

    def take_internal_request(self, request):
        if not self._invalid_internal_request(request):
            return

        if self.towards_up:
            self._add_request_to_up_queue(request)

        if self.towards_down:
            self._add_request_to_down_queue(request)

    def open_gate(self):
        self._gate_status = GateStatus.OPEN

    def close_gate(self):
        self._gate_status = GateStatus.CLOSE

    @property
    def towards_up(self):
        return self._direction == Direction.UP

    @property
    def towards_down(self):
        return self._direction == Direction.DOWN

    @property
    def towards_idle(self):
        return self._direction == Direction.IDLE

    def __le__(self, other):
        return self._current_level < other._current_level

    def __gt__(self, other):
        return self._current_level > other._current_level

    def _invalid_internal_request(self, request):
        if self._direction == Direction.UP and request.request_level <= self._current_level:
            return False

        if self._direction == Direction.DOWN and request.request_level >= self._current_level:
            return False

        return True

    def _add_request_to_up_queue(self, request):
        if request.request_level not in self._up_set:
            self._up_queues.put(request.request_level)
            self._up_set.add(request.request_level)

    def _add_request_to_down_queue(self, request):
        if request.request_level not in self._down_set:
            self._down_set.add(request.request_level)
            self._down_queues.put(request.request_level)
