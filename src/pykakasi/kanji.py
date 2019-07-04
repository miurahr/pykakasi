# -*- coding: utf-8 -*-
# j2.py
#
# Copyright 2011-2019 Hiroshi Miura <miurahr@linux.com>

import re
import threading

from klepto.archives import file_archive

from .properties import Configurations
from .scripts import H2


class J2(object):
    _kanwa = None
    _itaiji = None

    _cl_table = ["", "aiueow", "aiueow", "aiueow", "aiueow", "aiueow", "aiueow", "aiueow",
                 "aiueow", "aiueow", "aiueow", "k", "g", "k", "g", "k", "g", "k", "g", "k",
                 "g", "s", "zj", "s", "zj", "s", "zj", "s", "zj", "s", "zj", "t", "d", "tc",
                 "d", "aiueokstchgzjfdbpw", "t", "d", "t", "d", "t", "d", "n", "n", "n", "n",
                 "n", "h", "b", "p", "h", "b", "p", "hf", "b", "p", "h", "b", "p", "h", "b",
                 "p", "m", "m", "m", "m", "m", "y", "y", "y", "y", "y", "y", "rl", "rl",
                 "rl", "rl", "rl", "wiueo", "wiueo", "wiueo", "wiueo", "w", "n", "v", "k",
                 "k", "", "", "", "", "", "", "", "", ""]

    def __init__(self, mode, method="Hepburn"):
        self._kanwa = Kanwa()
        self._itaiji = Itaiji()
        if mode == "H":
            self.convert = self.convert_H
        elif mode in ("a", "K"):
            self._hconv = H2(mode, method)
            self.convert = self.convert_nonH
        else:
            self.convert = self.convert_noop

    def isRegion(self, c):
        return 0x3400 <= ord(c[0]) < 0xe000 or 0xf900 <= ord(c[0]) < 0xfa2e

    def isCletter(self, l, c):
        if (0x3041 <= ord(c) <= 0x309f) and (l in self._cl_table[ord(c) - 0x3040]):  # ぁ:= u\3041
            return True
        return False

    def itaiji_conv(self, text):
        r = []
        for c in text:
            if self._itaiji.haskey(c):
                r.append(c)
        for c in r:
            text = re.sub(c, self._itaiji.lookup(c), text)
        return text

    def convert_H(self, text):
        max_len = 0
        Hstr = ""
        text = self._itaiji.convert(text)
        table = self._kanwa.load(text[0])
        if table is None:
            return "", 0
        for (k, v) in table.items():
            length = len(k)
            if len(text) >= length:
                if text.startswith(k):
                    for (yomi, tail) in v:
                        if tail == '':
                            if max_len < length:
                                Hstr = yomi
                                max_len = length
                        elif max_len < length + 1 and len(text) > length \
                                and self.isCletter(tail, text[length]):
                            Hstr = ''.join([yomi, text[length]])
                            max_len = length + 1
        return (Hstr, max_len)

    def convert_nonH(self, text):
        if not self.isRegion(text[0]):
            return "", 0

        (t, l1) = self.convert_H(text)
        if l1 <= 0:  # pragma: no cover
            return "", 0

        m = 0
        otext = ""

        while True:
            if m >= len(t):
                break
            (s, n) = self._hconv.convert(t[m:])
            if n <= 0:  # pragma: no cover
                m = m + 1
            else:
                m = m + n
                otext = otext + s

        return otext, l1

    def convert_noop(self, text):
        return text[0], 1


class Itaiji(object):

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
                    itaijipath = Configurations().dictpath(Configurations().jisyo_itaiji)
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


# This class is Borg/Singleton
# It provides same results becase lookup from a static dictionary.
# There is no state rather dictionary dbm.
class Kanwa(object):
    _shared_state = {
        '_lock': threading.Lock(),
        '_jisyo_table': None
    }

    def __new__(cls, *p, **k):
        self = object.__new__(cls, *p, **k)
        self.__dict__ = cls._shared_state
        return self

    def __init__(self):
        if self._jisyo_table is None:
            with self._lock:
                if self._jisyo_table is None:
                    dictpath = Configurations().dictpath(Configurations().jisyo_kanwa)
                    self._jisyo_table = file_archive(dictpath, {}, serialized=True)
                    self._jisyo_table.load()

    def load(self, char):
        key = "%04x" % ord(char)
        return self._jisyo_table.get(key, None)
