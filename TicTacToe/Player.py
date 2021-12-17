#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Batter.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from enum import Enum
from itertools import cycle


class BattleSide(Enum):
    RED = 'RED'
    WHITE = 'WHITE'


class RedPlayer(object):
    chess = BattleSide.RED
    shape = 'X'


class WhitePlayer(object):
    chess = BattleSide.WHITE
    shape = 'O'


class Player(object):
    def __init__(self):
        self._players = cycle([WhitePlayer, RedPlayer])
        self._current_player = next(self._players)

    def switch_player(self):
        self._current_player = next(self._players)

    def current_player(self):
        return self._current_player
