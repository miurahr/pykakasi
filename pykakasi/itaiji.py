# -*- coding: utf-8 -*-
# itaiji.py
#
# Copyright 2015 Hiroshi Miura <miurahr@linux.com>
#
import re
from pkg_resources import resource_filename
from six.moves.cPickle import load

class itaiji (object):

    _itaijidict = None
    _itaijidict_len = 0

 # this class is Borg/Singleton
    _shared_state = {}

    def __new__(cls, *p, **k):
        self = object.__new__(cls, *p, **k)
        self.__dict__ = cls._shared_state
        return self

    def __init__(self):
        if self._itaijidict is None:
            itaijipath = resource_filename(__name__, 'itaijidict2.pickle')
            itaiji_pkl = open(itaijipath, 'rb')
            (self._itaijidict, self._itaijidict_len) = load(itaiji_pkl)

    def haskey(self, key):
        return key in self._itaijidict

    def lookup(self, key):
        return self._itaijidict[key]

    def canConvert(self, c):
        return ( 0x3400 <= ord(c[0]) and ord(c[0]) < 0xfa2e)

    def convert(self, text):
        r = []
        for c in text:
            if self.haskey(c):
                r.append(c)
        for c in r:
            text = re.sub(c, self.lookup(c), text)
        return text
