# -*- coding: utf-8 -*-
# k2.py
#
# Copyright 2011-2019 Hiroshi Miura <miurahr@linux.com>
#
# Original copyright:
# * KAKASI (Kanji Kana Simple inversion program)
# * $Id: jj2.c,v 1.7 2001-04-12 05:57:34 rug Exp $
# * Copyright (C) 1992
# * Hironobu Takahashi (takahasi@tiny.or.jp)
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either versions 2, or (at your option)
# * any later version.
# *
# * This program is distributed in the hope that it will be useful
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with KAKASI, see the file COPYING.  If not, write to the Free
# * Software Foundation Inc., 59 Temple Place - Suite 330, Boston, MA
# * 02111-1307, USA.
# */

from six import unichr
from six.moves import xrange

from .exceptions import UnsupportedRomanRulesException
from .jisyo import jisyo


class K2 (object):

    _kanadict = None

    _diff = 0x30a1 - 0x3041  # KATAKANA LETTER A - HIRAGANA A

    def __init__(self, mode, method="Hepburn"):
        if mode == "a":
            if method == "Hepburn":
                self._kanadict = jisyo('hepburndict2.pickle')
            elif method == "Passport":
                self._kanadict = jisyo('passportdict2.pickle')
            elif method == "Kunrei":
                self._kanadict = jisyo('kunreidict2.pickle')
            else:
                raise UnsupportedRomanRulesException("Unsupported roman rule")  # pragma: no cover

            self.convert = self.convert_a
        elif mode == "H":
            self.convert = self.convert_H
        else:
            self.convert = self.convert_noop

    def isRegion(self, char):
        return 0x30a0 < ord(char[0]) < 0x30fd

    def convert_a(self, text):
        Hstr = ""
        max_len = -1
        r = min(self._kanadict.maxkeylen(), len(text))
        for x in xrange(1, r + 1):
            if self._kanadict.haskey(text[:x]):
                if max_len < x:
                    max_len = x
                    Hstr = self._kanadict.lookup(text[:x])
            else:  # pragma: no cover
                break
        return Hstr, max_len

    def convert_H(self, text):
        Hstr = ""
        max_len = 0
        r = len(text)
        for x in xrange(r):
            if self.isRegion(text[x]) and ord(text[x]) < 0x30f7:
                Hstr = Hstr + unichr(ord(text[x]) - self._diff)
                max_len = max_len + 1
            elif self.isRegion(text[x]):
                Hstr = Hstr + text[x]
                max_len = max_len + 1
            else:  # pragma: no cover
                break
        return (Hstr, max_len)

    def convert_noop(self, text):
        return text[0], 1
