#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Request.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Request(object):
    def __init__(self):
        pass


class ExternalRequest(Request):
    def __init__(self, direction):
        self._direction = direction
        super(ExternalRequest, self).__init__()


class InternalRequest(Request):
    def __init__(self):
        super(InternalRequest, self).__init__()
