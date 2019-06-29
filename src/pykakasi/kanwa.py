# -*- coding: utf-8 -*-
#  kanwa.py
#
# Copyright 2011-2019 Hiroshi Miura <miurahr@linux.com>

import threading

from klepto.archives import file_archive
from pkg_resources import resource_filename


# This class is Borg/Singleton
# It provides same results becase lookup from a static dictionary.
# There is no state rather dictionary dbm.
class kanwa (object):
    _shared_state = {
        '_lock': threading.Lock(),
        '_jisyo_table': None
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
        if self._jisyo_table is None:
            with self._lock:
                if self._jisyo_table is None:
                    dictpath = resource_filename(__name__, 'kanwadict4.db')  # FIXME: no hardcoded filename
                    self._jisyo_table = file_archive(dictpath, {}, serialized=True)
                    self._jisyo_table.load()

    def load(self, char):
        key = "%04x" % ord(char)
        return self._jisyo_table.get(key, None)
