#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Board.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from TException import (OutSideError, AlreadyOccupyError,
                        NoBoardSpaceLeft, GameOverForWin)


class Board(object):
    def __init__(self, row=3, col=3):
        self._row, self._col = int(row), int(col)
        self._board = [['' for _ in range(self._row)] for _ in range(self._col)]
        self._size = self._row * self._col
        self._current_step = 0

    def init_board(self):
        self._board = [['' for _ in range(self._row)] for _ in range(self._col)]

    def make_move(self, current_player, row, col):
        if row < 0 or row >= self._row or col < 0 or col >= self._col:
            raise OutSideError(
                f'row line: {row} or col line: {col} out of bounds')

        if self._board[row][col]:
            raise AlreadyOccupyError(
                f'current location {row}/{col} is occupied')

        self._current_step += 1
        self._board[row][col] = current_player.shape

        try:
            self.check_win(current_player, [row, col])
        except GameOverForWin as e:
            print(f'{current_player.chess} win')
            self.print_board()
            raise

        self.is_board_full()
        self.print_board()

    def is_board_full(self):
        print('steps: {}, total steps: {}'.format(self._current_step,
                                                  self._size))
        if self._current_step >= self._size:
            self.print_board()
            raise NoBoardSpaceLeft(
                'No winner for board full, current space: {}, totabl space:'
                ' {}'.format(self._current_step, self._size))

    def check_win(self, current_player, location):
        row, col = location
        self._check_row(current_player, row)
        self._check_col(current_player, col)
        self._check_diagonal(current_player)

    def _check_row(self, current_player, row):
        for col in range(self._col):
            if self._board[row][col] != current_player.shape:
                return

        raise GameOverForWin(f'{current_player.chess} win')

    def _check_col(self, current_player, col):
        for row in range(self._row):
            if self._board[row][col] != current_player.shape:
                return

        raise GameOverForWin(f'{current_player.chess} win')

    def _check_diagonal(self, current_player):
        self._check_positive_diagnonal(current_player)
        self._check_negative_diagnonal(current_player)

    def _check_positive_diagnonal(self, current_player):
        for i in range(self._row):
            if self._board[i][i] != current_player.shape:
                return

        raise GameOverForWin(f'{current_player.chess} win')

    def _check_negative_diagnonal(self, current_player):
        for c in range(self._row):
            if self._board[c][self._col - c - 1] != current_player.shape:
                return

        raise GameOverForWin(f'{current_player.chess} win')

    def print_board(self):
        for row in range(self._row):
            _bds = ' | '.join([shape for shape in self._board[row]])
            print(_bds)