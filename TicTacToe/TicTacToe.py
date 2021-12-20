#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: TicTacToe.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from Board import Board
from Player import Player


class TicTacToe(object):
    def __init__(self, row=3, col=3):
        self._board = Board(row, col)
        self._players = Player()
        self._current_player = self._players

    def make_move(self, row, col):
        self._board.make_move(self._current_player.current_player(), row, col)
        self._change_player()

    def _change_player(self):
        self._players.switch_player()


if __name__ == '__main__':
    ttt = TicTacToe()
    try:
        ttt.make_move(0, 0)
        ttt.make_move(1, 1)
        ttt.make_move(0, 1)
        ttt.make_move(0, 2)
        ttt.make_move(1, 0)
        ttt.make_move(2, 0)
        ttt.make_move(1, 2)
        ttt.make_move(2, 2)
        ttt.make_move(2, 1)
    except:
        pass