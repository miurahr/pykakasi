# -*- coding: utf-8 -*-
#  nop.py
#
# Copyright 2011 Hiroshi Miura <miurahr@linux.com>

class NOP(object):
    def __init__(self):
        pass

    def isRegion(self, char):
        return False

    def convert(self, text):
        return ("", 0) # pragma: no cover

