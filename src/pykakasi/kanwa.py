# -*- coding: utf-8 -*-
#  kanwa.py
#
# Copyright 2011-2019 Hiroshi Miura <miurahr@linux.com>

import threading
from marshal import loads
from zlib import decompress

import semidbm as dbm
from pkg_resources import resource_filename


# This class is Borg/Singleton
# It provides same results becase lookup from a static dictionary.
# There is no state rather dictionary dbm.
class kanwa (object):
    _shared_state = {
        '_kanwadict': None,
        '_lock': threading.Lock(),
        '_jisyo_table': {}
    }

    # Note: there is no invalidate mechanism for _jisyo_table data.
    #       It can lead a large memory consumption in long live process.
    #       maximum memory consumption will be several megabytes which is
    #       a size of a dictionary.

    def __new__(cls, *p, **k):
        self = object.__new__(cls, *p, **k)
        self.__dict__ = cls._shared_state
        return self

    def __init__(self):
        if self._kanwadict is None:
            with self._lock:
                if self._kanwadict is None:
                    dictpath = resource_filename(__name__, 'kanwadict3.db')  # FIXME: no hardcoded filename
                    self._kanwadict = dbm.open(dictpath, 'r')  # readonly mode

    def load(self, char):
        key = "%04x" % ord(char)
        if key not in self._jisyo_table:
            with self._lock:
                if key not in self._jisyo_table:
                    try:
                        val = loads(decompress(self._kanwadict[key]))
                    except KeyError:
                        val = None
                    self._jisyo_table[key] = val
        return self._jisyo_table.get(key, None)
