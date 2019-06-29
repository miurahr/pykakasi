# -*- coding: utf-8 -*-
# itaiji.py
#
# Copyright 2015-2019 Hiroshi Miura <miurahr@linux.com>
#

import re
import threading

from klepto.archives import file_archive
from pkg_resources import resource_filename


class itaiji (object):

    # this class is Borg/Singleton
    _shared_state = {
        '_itaijidict': None,
        '_itaijidict_len': 0,
        '_lock': threading.Lock()
    }

    def __new__(cls, *p, **k):
        self = object.__new__(cls, *p, **k)
        self.__dict__ = cls._shared_state
        return self

    def __init__(self):
        if self._itaijidict is None:
            with self._lock:
                if self._itaijidict is None:
                    itaijipath = resource_filename(__name__, 'itaijidict3.db')
                    self._itaijidict = file_archive(itaijipath, {}, serialized=True)
                    self._itaijidict.load()
                    self._itaijidict_len = self._itaijidict['_max_key_len_']

    def haskey(self, key):
        return key in self._itaijidict

    def lookup(self, key):
        return self._itaijidict[key]

    def convert(self, text):
        r = []
        for c in text:
            if self.haskey(c):
                r.append(c)
        for c in r:
            text = re.sub(c, self.lookup(c), text)
        return text
