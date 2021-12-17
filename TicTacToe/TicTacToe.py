#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: TicTacToe.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from TicTacToe.Board import Board
from TicTacToe.Player import Player


class TicTacToe(object):
    def __init__(self):
        self._board = Board()
        self._players = Player()
        self._current_player = self._players.current_player()

    def make_move(self, row, col):
        self._board.make_move(self._current_player, row, col)
        self._change_player()

    def _change_player(self):
        self._players.switch_player()
