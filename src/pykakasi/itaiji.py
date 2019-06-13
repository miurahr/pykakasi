# -*- coding: utf-8 -*-
# itaiji.py
#
# Copyright 2015-2019 Hiroshi Miura <miurahr@linux.com>
#

import re
import threading

from pkg_resources import resource_filename
from six.moves import cPickle


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
                    itaijipath = resource_filename(__name__, 'itaijidict2.pickle')
                    with open(itaijipath, 'rb') as itaiji_pkl:
                        (self._itaijidict, self._itaijidict_len) = cPickle.load(itaiji_pkl)

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
