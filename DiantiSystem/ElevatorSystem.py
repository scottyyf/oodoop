#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: ElevatorSystem.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import queue
from DiantiSystem.utils import SimpleQueue, Direction
from DiantiSystem.Elevator import Elevator
from DiantiSystem.Request import Request, ExternalRequest


class ElevatorSystem(object):
    """a elevator system manage a few elevators"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance

        cls.__instance = super(ElevatorSystem, cls).__new__(cls, *args,
                                                            **kwargs)
        return cls.__instance

    def __init__(self):
        self.elevator_list = SimpleQueue()

    def hand_request(self, request: ExternalRequest):
        data = queue.PriorityQueue()
        for elevator in self.elevator_list.list():
            data.put((CalculateStep(elevator, request).get_steps(), elevator))

        choose_elevator = None
        try:
            pri, choose_elevator = data.get(block=False)
        except queue.Empty:
            print('pls register a elevator first')

        return choose_elevator

    def add_elevator(self, elevator):
        self.elevator_list.put(elevator, elevator)

    def remove_elevator(self, elevator):
        self.elevator_list.delete(elevator)


class CalculateStep:
    def __init__(self, elevator, request):
        self._elevator = elevator
        self._request = request

    def get_steps(self):
        if self._request._direction == self._elevator._direction:
            if self._elevator.towards_up:
                if self._elevator._current_level <= self._request.request_level:
                    return SameDirectory(self._elevator, self._request).get_steps()
                else:
                    return DiffDirectory(self._elevator, self._request).get_steps()

            if self._elevator.towards_down:
                if self._elevator._current_level >= self._request.request_level:
                    return SameDirectory(self._elevator, self._request).get_steps()
                else:
                    return DiffDirectory(self._elevator, self._request).get_steps()

        if self._elevator._direction == Direction.IDLE:
            return SameDirectory(self._elevator, self._request).get_steps()

        return DiffDirectory(self._elevator, self._request).get_steps()


class SameDirectory(object):
    def __init__(self, elevator, request):
        self._elevator = elevator
        self._request = request

    def get_steps(self):
        print('Same', abs(self._request.request_level - self._elevator._current_level))
        return abs(self._request.request_level - self._elevator._current_level)


class DiffDirectory(object):
    def __init__(self, elevator, request):
        self._elevator = elevator
        self._request = request

    def get_steps(self):
        current_level = self._elevator._current_level
        down_queues = self._elevator._down_queues.queue
        up_queues = self._elevator._up_queues.queue
        request_level = self._request.request_level

        extra_level = current_level if not down_queues else min(down_queues)
        if self._elevator.towards_up:
            extra_level = current_level if not up_queues else max(up_queues)

        print('Diff: ', abs(current_level - extra_level) + abs(request_level - extra_level))
        return abs(current_level - extra_level) + abs(request_level - extra_level)


if __name__ == '__main__':
    ele = ElevatorSystem()

    et = Elevator(ele)
    et._direction = Direction.DOWN
    et._down_queues.put(-20)
    et._up_queues.put(20)
    et._current_level = 1

    et2 = Elevator(ele, name='slave1')
    et2._current_level = 2
    et2._direction = Direction.UP
    et2._up_queues.put(10)

    et3 = Elevator(ele, name='slave2')
    et3._current_level = 5
    et3._direction = Direction.UP
    et3._up_queues.put(19)

    request = ExternalRequest(Direction.UP, 11)
    request1 = ExternalRequest(Direction.DOWN, 5)
    request2 = ExternalRequest(Direction.DOWN, -5)
    request3 = ExternalRequest(Direction.UP, 50)

    ret = ele.hand_request(request)
    ret1 = ele.hand_request(request1)
    ret2 = ele.hand_request(request2)
    ret3 = ele.hand_request(request3)
    print(ret.name)
    print(ret1.name)
    print(ret2.name)
    print(ret3.name)
