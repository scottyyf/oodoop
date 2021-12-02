#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: TException.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Error(Exception):
    pass


class NotAllowedDirectionError(Error):
    pass


class QueueAlreadyFullError(Error):
    pass