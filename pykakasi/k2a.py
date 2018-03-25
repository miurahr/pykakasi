# -*- coding: utf-8 -*-
#  k2a.py
#
# Copyright 2011-2018 Hiroshi Miura <miurahr@linux.com>
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

from .jisyo import jisyo
from .exceptions import UnsupportedRomanRulesException

class K2a (object):

    _kanadict = None

    def __init__(self, method="Hepburn"):
        if method == "Hepburn":
            self._kanadict = jisyo('hepburndict2.pickle')
        elif method == "Passport":
            self._kanadict = jisyo('passportdict2.pickle')
        elif method == "Kunrei":
            self._kanadict = jisyo('kunreidict2.pickle')
        else:
            raise UnsupportedRomanRulesException("Unsupported roman rule") 

    def isRegion(self, char):
           return  (0x30a0 < ord(char[0]) and ord(char[0]) < 0x30fd)

    def convert(self, text):
        Hstr = ""
        max_len = -1
        r = min(self._kanadict.maxkeylen(), len(text))
        for x in range(1, r+1):
            if self._kanadict.haskey(text[:x]):
                if max_len < x:
                    max_len = x
                    Hstr = self._kanadict.lookup(text[:x])
        return (Hstr, max_len)

