#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Coin.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Coin(object):
    _point = None

    @classmethod
    def get_point(cls):
        assert cls._point is not None
        return cls._point


class Fen(Coin):
    _point = 0.01


class Jiao(Coin):
    _point = 0.1


class Yuan(Coin):
    _point = 1


class FiveYuan(Coin):
    _point = 5


class TenYuan(Coin):
    _point = 10


class TwentyYuan(Coin):
    _point = 20


class FiftyYuan(Coin):
    _point = 50


class HundredYuan(Coin):
    _point = 100
