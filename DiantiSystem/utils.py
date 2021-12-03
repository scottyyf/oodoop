#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: utils.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from enum import Enum

from TException import QueueAlreadyFullError


class Direction(Enum):
    UP = 1
    DOWN = 2
    IDLE = 3


class GateStatus(Enum):
    OPEN = 1
    CLOSE = 2


class Button(object):
    def __init__(self, level):
        self._to_level = level

    def inner_request(self):
        return self._to_level


class LinkNode(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class SimpleQueue(object):
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.size = 0

        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.exist_node = {}

    def get(self, key):
        if key not in self.exist_node:
            return -1

        node = self.exist_node[key]
        return node.value

    def put(self, key, value):
        if key in self.exist_node:
            return

        if self.size >= self.capacity:
            raise QueueAlreadyFullError('queue already Full')

        node = LinkNode(key, value)
        self.exist_node[key] = node
        self.size += 1
        self.move_to_head(node)

    def delete(self, key):
        if key not in self.exist_node:
            return

        node = self.exist_node.get(key)
        self.exist_node.pop(key)
        self.remove_node(node)

    def move_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def list(self):
        for node in self.exist_node.values():
            yield node.value
