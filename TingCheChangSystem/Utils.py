#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Utils.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import math
from datetime import datetime


class CalculateTime:
    def __init__(self, start_time, end_time):
        assert isinstance(start_time, datetime)
        assert isinstance(end_time, datetime)
        self._start_time = start_time
        self._end_time = end_time

    def in_free_time(self, free=30):
        # 30 minutes is free for charge
        between_minutes = (self._end_time - self._start_time).total_seconds(
            ) / 60
        return between_minutes < free

    def get_hours(self):
        return math.ceil(
            (self._end_time - self._start_time).total_seconds() / 3600)


if __name__ == '__main__':
    t1 = datetime.now()
    import time
    time.sleep(2)
    # t2 = datetime.strptime('2021-12-05 00:00:00', '%Y-%m-%d %H:%M:%S')
    t2 ='2021-12-05 00:00:00', '%Y-%m-%d %H:%M:%S'
    c = CalculateTime(t2, t1)
    x = c.in_free_time()
    print(x)
    print(c.get_hours())