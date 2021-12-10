#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Restaurant.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from Party import Party
from TException import OutOfCurrentMaxCapacity
from Table import Table


class Restaurant(object):
    def __init__(self, tables: list):
        self._list_tables = tables
        self._menus = []
        self._list_reservation = {}

    def find_tables(self, party):
        ret = sorted(self._list_tables,
                     key=lambda item: item.current_capacity())
        index = self._binary_search(ret, party)
        _t = []
        if index == -2:
            _t.append(ret[0])

        elif index == -1:
            t, capacity = len(ret) - 1, ret[len(ret) - 1].current_capacity()
            while capacity < party.get_capacity():
                t -= 1
                capacity += ret[t].current_capacity()

            _t = ret[t:len(ret)]

        for _ in _t:
            _.mark_unavailable()

        return _t

    def take_order(self, order):
        self._menus.append(order)

    def check_out(self, order):
        pay = order.calculate_price()
        for _ in order.tables():
            _.mark_available()

        if order in self._menus:
            self._menus.remove(order)

        return pay

    def find_table_for_reservation(self, timeslot, party):
        # TODO
        pass

    def confirm_reservation(self, reserve):
        # TODO
        pass

    def add_table(self, table):
        self._list_tables.append(table)

    def _binary_search(self, tables, party):
        if party.get_capacity() > self._current_capacity():
            raise OutOfCurrentMaxCapacity('no enough table to serve')

        if party.get_capacity() > tables[-1].current_capacity():
            return -1

        if party.get_capacity() < tables[0].current_capacity():
            return -2

        left, right = 0, len(tables) - 1
        while left < right:
            pivot = left + (right - left) // 2
            if tables[pivot].current_capacity() == party.get_capacity():
                return pivot

            elif tables[pivot].current_capacity() > party.get_capacity():
                right = pivot
            else:
                left = pivot + 1

        return right

    def _current_capacity(self):
        ret = 0
        for table in self._list_tables:
            ret += table.current_capacity()

        return ret


if __name__ == '__main__':
    p1 = Party(2)
    p2 = Party(2)
    p3 = Party(1)

    t1 = Table(1)
    t2 = Table(3)
    t3 = Table(7)
    li = [Table(x) for x in range(100)]
    res = Restaurant(li)
    # res.add_table(p2)
    # res.add_table(p3)
    ret = res.find_tables(p3)
    print(ret)
