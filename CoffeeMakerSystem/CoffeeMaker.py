#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: CoffeeMaker.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from Coffee import Coffee
from CoffeePack import CatShitCoffeePack
from CondiMent import Milk


class CoffeeMaker(object):
    def __init__(self):
        self._list_coffee = []

    def brew_coffee(self, coffee_pack):
        coffee = Coffee(coffee_pack)
        return coffee

    def add(self, coffee, condiment):
        coffee.add(condiment)
        return coffee

    def check_out(self, coffee):
        price = coffee.get_price()
        return price


if __name__ == '__main__':
    cm = CoffeeMaker()
    cp = CatShitCoffeePack()
    cf = cm.brew_coffee(cp)
    cf.add(cp)
    print(cf.get_price())
    cdm = Milk()
    cf.add(cdm)
    cf.add(cdm)
    cf.add(cdm)
    cf.add(cdm)
    print(cf.get_price())
    print(cf.get_desc())