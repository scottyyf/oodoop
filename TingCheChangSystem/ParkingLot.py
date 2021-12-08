#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: ParkingLot.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from datetime import datetime

from TException import SpotOccupiedError, NoSuitableSpotsError
from Ticket import Ticket
from Utils import CalculateTime


class ParkingLot:
    def __init__(self, hourly_rate):
        self._levels = []
        self._hourly_rate = hourly_rate

    def get_available_count(self):
        count = 0
        for level in self._levels:
            count += level.get_available_count()

        return count

    def park_vehicle(self, vehicle):
        try:
            spots = self._find_spots_for_vehicle(vehicle)
        except NoSuitableSpotsError:
            # go to another Lot
            raise

        for spot in spots:
            try:
                spot.take_spot()
            except SpotOccupiedError:
                # need refind spots
                raise

        ticket = Ticket(spots, vehicle)
        return ticket

    def _find_spots_for_vehicle(self, vehicle):
        # ret = []
        for level in self._levels:
            spots = level.find_spots_for_vehicle(vehicle)
            if spots:
                return spots

        raise NoSuitableSpotsError('can not find spots for vehicle')

    def clear_spot(self, ticket):
        spots = ticket.spots()
        for spot in spots:
            spot.leave_spot()

    def calculate_price(self, ticket):
        end_time = datetime.now()
        start_time = ticket.start_time()

        cal_inst = CalculateTime(start_time, end_time)
        if cal_inst.in_free_time():
            return 0

        else:
            return self._hourly_rate * cal_inst.get_hours()
