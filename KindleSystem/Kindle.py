#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Kindle.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from KindleSystem.Book import Book
from KindleSystem.Format import Format
from KindleSystem.ReaderFactory import ReaderFactory


class Kindle(object):
    def __init__(self):
        self._books = []

    def upload(self, book):
        # upload book to website
        return

    def download(self, book):
        # get book, return a Book instance
        book = Book('mock', Format.MOBI)
        self._books.append(book)
        return book

    def read(self, book):
        reader = ReaderFactory.create_reader(book)
        ret = reader.display(book)
        return ret

    def delete(self, book):
        if book not in self._books:
            return

        self._books.remove(book)
