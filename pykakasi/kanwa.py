# -*- coding: utf-8 -*-
#  kanwa.py
#
# Copyright 2011-2018 Hiroshi Miura <miurahr@linux.com>
from zlib import decompress
from pkg_resources import resource_filename
from marshal import loads
import six
import semidbm as dbm

class kanwa (object):

# This class is Borg/Singleton
# It provides same results becase lookup from a static dictionary.
# There is no state rather dictionary dbm.
    _shared_state = {}

    _kanwadict = None
    _jisyo_table = {}

# FIXME: there is no invalidate mechanism for _jisyo_table data.
#        It can lead a large memory consumption in long live process.
#        but max size are limited to a size of a dictionary.

    def __new__(cls, *p, **k):
        self = object.__new__(cls, *p, **k)
        self.__dict__ = cls._shared_state
        return self

    def __init__(self):
        if self._kanwadict is None:
            dictpath = resource_filename(__name__, 'kanwadict3.db') # FIXME: no hardcoded filename
            self._kanwadict = dbm.open(dictpath,'r')

    def load(self, char):
        if six.PY2:
            key = "%04x"%ord(unicode(char))
        else:
            key = "%04x"%ord(char)
        if key in self._jisyo_table:
            return self._jisyo_table[key]
        else:
            try:
                self._jisyo_table[key]  = loads(decompress(self._kanwadict[key]))
                return self._jisyo_table[key]
            except:
                return None

