#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Board.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from TicTacToe.TException import OutSideError, AlreadyOccupyError


class Board(object):
    def __init__(self, row=3, col=3):
        self._row, self._col = row, col
        self._board = [['' for _ in range(row)] for _ in range(col)]

    def init_board(self):
        self._board = [['' for _ in range(self._row)] for _ in range(self._col)]

    def make_move(self, current_player, row, col):
        if row < 0 or row >= self._row or col < 0 or col >= self._col:
            raise OutSideError(
                f'row line: {row} or col line: {col} out of bounds')

        if self._board[row][col]:
            raise AlreadyOccupyError(
                f'current location {row}/{col} is occupied')

        self._board[row][col] = current_player.shape
        self.check_win()

    def is_board_full(self):
        pass

    def check_win(self):
        pass
