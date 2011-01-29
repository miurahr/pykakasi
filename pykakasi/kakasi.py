# -*- coding: utf-8 -*-
#  kakasi.py
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

import re
import sys, os

class kakasi(object):

#instances
    _jconv = None
    _hconv = None
    _kconv = None

#mode flags
    _flag = {"W":False}
    _mode = {"J":"a", "H":"a", "K":"a"}
    _values = ["a", "h", "k"]

    def __init__(self):
        pass

    def setMode(self, fr, to):
        if fr in self._mode:
            if to in self._values:
                self._mode[fr] = to
        if fr in self._flag:
            if to in [True,False]:
                self._flag[fr] = to

    def getConverter(self):
        from j2h import J2H
        from h2a import H2a
        from k2a import K2a
        self._jconv = J2H()
        self._hconv = H2a() 
        self._kconv = K2a()
        return self

    def do(self, text):
        otext =  ''
        i = 0
        while True:
            if i >= len(text):
                break

            if self._jconv.isKanji(text[i]):
                (t, l) = self._jconv.convert(text[i:])
                if l <= 0:
                    break
                i = i + l
                m = 0
                tmptext = ""
                while True: 
                    if m >= len(t):
                        break
                    (s, n) = self._hconv.convert(t[m:])
                    if n <= 0:
                        break
                    m = m + n
                    tmptext = tmptext+s
                if i >= len(text):
                    otext = otext + tmptext.capitalize()
                else:
                    otext = otext + tmptext.capitalize() +' ' 
            elif self._hconv.isHiragana(text[i]):
                tmptext = ''
                while True:
                    (t, l) = self._hconv.convert(text[i:])
                    tmptext = tmptext+t
                    i = i + l
                    if i >= len(text):
                        otext = otext + tmptext                    
                        break
                    elif not self._hconv.isHiragana(text[i]):
                        otext = otext + tmptext + ' '
                        break
            elif self._kconv.isKatakana(text[i]):
                tmptext = ''
                while True:
                    (t, l) = self._kconv.convert(text[i:])
                    tmptext = tmptext+t
                    i = i + l
                    if i >= len(text):
                        otext = otext + tmptext                    
                        break
                    elif not self._kconv.isKatakana(text[i]):
                        otext = otext + tmptext + ' '
                        break
            else:
                otext  = otext + text[i]
                i += 1

        return otext

