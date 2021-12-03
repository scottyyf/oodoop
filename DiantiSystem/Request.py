#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Request.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from utils import Direction


class Request(object):
    def __init__(self, request_level):
        self.request_level = request_level


class ExternalRequest(Request):
    def __init__(self, direction, request_level):
        self._direction = direction
        super(ExternalRequest, self).__init__(request_level)

    @property
    def towards_up(self):
        return self._direction == Direction.UP

    @property
    def towards_down(self):
        return self._direction == Direction.DOWN

    @property
    def towards_idle(self):
        return self._direction == Direction.IDLE


class InternalRequest(Request):
    def __init__(self, request_level):
        super(InternalRequest, self).__init__(request_level)
