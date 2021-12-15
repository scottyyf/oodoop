#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: CoffeePack.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from typing import Optional


class CoffeePack(object):
    def __init__(self, price, desc):
        self._price = price
        self._desc = desc

    def get_price(self):
        return self._price

    def add(self, num=1):
        for _ in range(num):
            self._price += self._price

    def get_desc(self):
        return self._desc


class CatShitCoffeePack(CoffeePack):
    def __init__(self, price=5, desc='cat_shit'):
        super(CatShitCoffeePack, self).__init__(price, desc)


class JpCoffeePack(CoffeePack):
    def __init__(self, price=0.5, desc='jp_coffee'):
        super(JpCoffeePack, self).__init__(price, desc)


class KuBaCoffeePack(CoffeePack):
    def __init__(self, price=2, desc='kuba_coffee'):
        super(KuBaCoffeePack, self).__init__(price, desc)
