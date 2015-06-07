# -*- coding: utf-8 -*-
#  j2h.py
#
# Copyright 2011 Hiroshi Miura <miurahr@linux.com>
#
#  Original Copyright:
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

from .kanwa import kanwa
from .itaiji import itaiji
import re

class J2H (object):

    _kanwa = None
    _itaiji = None

    _cl_table = [
	"","aiueow", "aiueow", "aiueow", "aiueow", "aiueow", "aiueow", "aiueow",
	"aiueow", "aiueow", "aiueow", "k", "g", "k", "g", "k", "g", "k", "g", "k",
	"g", "s", "zj", "s", "zj", "s", "zj", "s", "zj", "s", "zj", "t", "d", "tc",
	"d", "aiueokstchgzjfdbpw", "t", "d", "t", "d", "t", "d", "n", "n", "n", "n",
	"n", "h", "b", "p", "h", "b", "p", "hf", "b", "p", "h", "b", "p", "h", "b",
	"p", "m", "m", "m", "m", "m", "y", "y", "y", "y", "y", "y", "rl", "rl",
	"rl", "rl", "rl", "wiueo", "wiueo", "wiueo", "wiueo", "w", "n", "v", "k",
	"k", "", "", "", "", "", "", "", "", ""]

    def __init__(self):
        self._kanwa = kanwa()
        self._itaiji = itaiji()

    def isRegion(self, c):
        return ( 0x3400 <= ord(c[0]) and ord(c[0]) < 0xfa2e)

    def isCletter(self, l, c):
        if (0x3041 <= ord(c) and  ord(c) <= 0x309f) and (l in self._cl_table[ord(c) - 0x3040]): # ぁ:= u\3041
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

    def convert(self, text):
        max_len = 0
        match_more = False
        Hstr = ""
        text = self._itaiji.convert(text)
        table = self._kanwa.load(text[0])
        if table is None:
            return ("", 0)
        for (k,v) in table.items():
            length = len(k)
            if len(text) >= length:
                if text.startswith(k):
                    for  (yomi, tail) in v:
                        if tail is '':
                            if max_len < length:
                                Hstr = yomi
                                max_len = length
                        elif max_len < length+1 and len(text) > length and self.isCletter(tail, text[length]):
                            Hstr=''.join([yomi,text[length]])
                            max_len = length+1
        return (Hstr, max_len)
