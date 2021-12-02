#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: ElevatorSystem.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from DiantiSystem.utils import SimpleQueue
from DiantiSystem.Elevator import Elevator


class ElevatorSystem(object):
    """a elevator system manage a few elevators"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance

        cls.__instance = super(ElevatorSystem, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.elevator_list = SimpleQueue()

    def hand_request(self, request):
        pass

    def add_elevator(self, elevator):
        self.elevator_list.put(elevator, elevator)

    def remove_elevator(self, elevator):
        self.elevator_list.delete(elevator)


if __name__ == '__main__':
    ele = ElevatorSystem()
    et = Elevator()
    et._curren_level = 1
    et2 = Elevator()
    et2._curren_level = 2
    ele.add_elevator(et)
    ele.add_elevator(et2)
    ele.remove_elevator(et2)
    print(ele.elevator_list.exist_node)