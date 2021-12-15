#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: State.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from TException import StateError, NoEnoughCoinError
# from VendingMachine import VendingMachine


class AbstractState(object):
    def __init__(self, vending_machine):
        self._vending_machine = vending_machine

    def select_items(self, str_item):
        raise StateError('invalid state for select items ')

    def insert_coins(self, coins):
        raise StateError('invalid state for insert coins')

    def execute_transaction(self):
        raise StateError('invalid state for execute transaction')

    def cancel_transaction(self):
        raise StateError('invalid state for cancel transaction')

    def __call__(self, *args, **kwargs):
        ret = self
        if hasattr(self, 'direct_change') and callable(self.direct_change):
            ret = self.direct_change()

        return ret


class HasNoSelectionState(AbstractState):
    def __init__(self, vending_machine):
        super(HasNoSelectionState, self).__init__(vending_machine)

    def insert_coins(self, coins):
        self._vending_machine.add_coins(coins)

    def select_items(self, str_item):
        self._vending_machine.get_item(str_item)
        self._vending_machine.change_to_selection_state()

    def cancel_transaction(self):
        return self._vending_machine.off_funds()


class HasSelectionState(AbstractState):
    def __init__(self, vending_machine):
        super(HasSelectionState, self).__init__(vending_machine)

    def direct_change(self):
        ret = self._vending_machine.change_to_no_confirm_state()
        return ret


class HasNoCoinState(AbstractState):
    def __init__(self, vending_machine):
        super(HasNoCoinState, self).__init__(vending_machine)

    def insert_coins(self, coins):
        self._vending_machine.add_coins(coins)
        self._vending_machine.change_to_coin_state()

    def cancel_transaction(self):
        return


class HasCoinState(AbstractState):
    def __init__(self, vending_machine):
        super(HasCoinState, self).__init__(vending_machine)

    def direct_change(self):
        ret = self._vending_machine.change_to_no_selection_state()
        return ret


class NoConfirmState(AbstractState):
    def __init__(self, vending_machine):
        super(NoConfirmState, self).__init__(vending_machine)

    def insert_coins(self, coins):
        self._vending_machine.add_coins(coins)

    def execute_transaction(self):
        try:
            self._vending_machine.transact_item()
        except NoEnoughCoinError as e:
            self._vending_machine.change_to_no_enough_coin_state()
            print(f'more money {e}')
            return

        self._vending_machine.change_to_confirm_state()
        return self._vending_machine.off_funds(False)

    def cancel_transaction(self):
        return self._vending_machine.off_funds()


class ConfirmState(AbstractState):
    def __init__(self, vending_machine):
        super(ConfirmState, self).__init__(vending_machine)


class NoEnoughCoinState(AbstractState):
    def __init__(self, vending_machine):
        super(NoEnoughCoinState, self).__init__(vending_machine)

    def insert_coins(self, coins):
        self._vending_machine.add_coins(coins)
        self._vending_machine.change_to_no_confirm_state()

    def cancel_transaction(self):
        return self._vending_machine.off_funds()


class SoldOutState(AbstractState):
    def __init__(self, vending_machine):
        super(SoldOutState, self).__init__(vending_machine)
