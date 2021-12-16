#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: ReaderFactory.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from KindleSystem.Format import Format
from KindleSystem.TException import NotSupportFormatError


class ReaderFactory(object):
    @classmethod
    def create_reader(cls, book):
        if book.get_format() == Format.PDF:
            return PdfReader()

        elif book.get_format() == Format.PUB:
            return PubReader()

        elif book.get_format() == Format.MOBI:
            return MobiReader()

        raise NotSupportFormatError(
            f'{book.get_format()} is not in supported list')


class Reader(object):
    def __init__(self):
        pass

    def display(self, book):
        raise NotImplementedError


class PdfReader(Reader):
    def __init__(self):
        super(PdfReader, self).__init__()

    def display(self, book):
        return 'pdf'


class MobiReader(Reader):
    def __init__(self):
        super(MobiReader, self).__init__()

    def display(self, book):
        return 'mobi'


class PubReader(Reader):
    def __init__(self):
        super(PubReader, self).__init__()

    def display(self, book):
        return 'pub'
