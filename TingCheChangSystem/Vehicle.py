#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Vehicle.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from enum import Enum

from TException import NotIntOrEnumError


class VehicleSize(Enum):
    MOTOCYCLE = 1
    CAR = 2
    BUS = 4


class Vehicle(object):
    _size = None

    def get_size(self):
        if isinstance(self._size, int):
            return self._size
        elif isinstance(self._size, Enum):
            return self._size.value

        raise NotIntOrEnumError('int or enum object needed')


class Bus(Vehicle):
    _size = VehicleSize.BUS


class Car(Vehicle):
    _size = VehicleSize.CAR


class MotoCycle(Vehicle):
    _size = VehicleSize.MOTOCYCLE
