# -*- coding: utf-8 -*-
#  kanwa.py
#
# Copyright 2011-2015 Hiroshi Miura <miurahr@linux.com>
from zlib import decompress
from pkg_resources import resource_filename
from marshal import loads
import six

try:
    import anydbm as dbm
except:
    import dbm

class kanwa (object):

    _kanwadict = None
    _jisyo_table = {}

# this class is Borg/Singleton
    _shared_state = {}

    def __new__(cls, *p, **k):
        self = object.__new__(cls, *p, **k)
        self.__dict__ = cls._shared_state
        return self

    def __init__(self):
        if self._kanwadict is None:
            dictpath = resource_filename(__name__, 'kanwadict2.db')
            self._kanwadict = dbm.open(dictpath,'r')

    def load(self, char):
        if six.PY2:
            key = "%04x"%ord(unicode(char))
        else:
            key = "%04x"%ord(char)
        try: #already exist?
            table = self._jisyo_table[key]
        except:
            try:
                table = self._jisyo_table[key]  = loads(decompress(self._kanwadict[key]))
            except:
                return None
        return table

