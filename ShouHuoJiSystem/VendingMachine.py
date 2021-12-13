#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: VendingMachine.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from Coin import Coin, TenYuan
from Item import Coffee
from ItemInfo import ItemInfo
from State import (HasNoSelectionState, HasSelectionState, HasNoCoinState,
                   HasCoinState, NoConfirmState, SoldOutState,
                   NoEnoughCoinState, ConfirmState)
from TException import NoItemError, NoEnoughCoinError


class VendingMachine(object):
    def __init__(self):
        self._refund_coins = []
        self._current_coins = 0
        self._item_location_info = {}
        self._current_selection = None

        self._HasNoSelectionState = HasNoSelectionState(self)
        self._HasSelectionState = HasSelectionState(self)
        self._HasNoCoinState = HasNoCoinState(self)
        self._HasCoinState = HasCoinState(self)
        self._NoConfirmState = NoConfirmState(self)
        self._SoldOutState = SoldOutState(self)
        self._NoEnoughCoinState = NoEnoughCoinState(self)
        self._ConfirmState = ConfirmState(self)

        self._current_state = self._HasNoCoinState

    def insert_coins(self, coins):
        self._current_state.insert_coins(coins)

    def select_items(self, str_item):
        self._current_state.select_items(str_item)

    def execute_transaction(self):
        return self._current_state.execute_transaction()

    def cancel_transaction(self):
        self._current_state.cancel_transaction()

    def off_funds(self, cancel=True):
        if cancel:
            self._current_selection = None
            funds, self._current_coins = self._current_coins, 0
            return funds
        else:
            return self._refund()

    def change_to_no_selection_state(self):
        self._current_state = self._HasNoSelectionState()
        return self._current_state

    def change_to_selection_state(self):
        self._current_state = self._HasSelectionState()
        return self._current_state

    def change_to_no_coin_state(self):
        self._current_state = self._HasNoCoinState()
        return self._current_state

    def change_to_coin_state(self):
        self._current_state = self._HasCoinState()
        return self._current_state

    def change_to_no_confirm_state(self):
        self._current_state = self._NoConfirmState()
        return self._current_state

    def change_to_no_enough_coin_state(self):
        self._current_state = self._NoEnoughCoinState()
        return self._current_state

    def change_to_sold_out_state(self):
        self._current_state = self._SoldOutState()
        return self._current_state

    def change_to_confirm_state(self):
        self._current_state = self._ConfirmState()
        return self._current_state

    def refill_item(self, item):
        if not self._current_selection:
            return

        self._current_selection.add(item)

    def _refund(self):
        if self._current_coins < self._current_selection.get_price():
            raise NoEnoughCoinError('No more coin')

        return self._current_coins - self._current_selection.get_price()

    def add_coins(self, coins):
        if isinstance(coins, list):
            for coin in coins:
                self._current_coins += coin.get_point()
        elif isinstance(coins, Coin):
            self._current_coins += coins.get_point()

        else:
            raise TypeError('Not a Coin type')

    def get_item(self, str_item):
        if str_item not in self._item_location_info:
            raise NoItemError(f'there is no item at {str_item}')

        item_info = self._item_location_info.get(str_item)
        self._current_selection = item_info
        return item_info

    def transact_item(self):
        item_info = self._current_selection

        fund = self._refund()
        return item_info.get_and_remove_item(), fund


if __name__ == '__main__':
    vm = VendingMachine()
    coin = TenYuan()
    item = Coffee()
    iteminfo = ItemInfo(9, [item])
    vm._item_location_info['A1'] = iteminfo

    print(vm._current_state)
    vm.insert_coins(coin)
    print(vm._current_state)

    vm.select_items('A1')
    print(vm._current_state)
    r = vm.execute_transaction()
    print(r)
    print(vm._current_state)
