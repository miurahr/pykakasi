# -*- coding: utf-8 -*-
#  kakasi.py
#
# Copyright 2011,2014 Hiroshi Miura <miurahr@linux.com>
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
    _aconv = None

#mode flags
    _flag = {"W":False, "C":True, "c":True}
    _mode = {"J":"a", "H":"a", "K":"a", "a":None, "r":"Hepburn"}
    _values = ["a", "h", "k"]
    _option = {"r":"Hepburn"}
    _optvals = {"r":["Hepburn", "Kunrei"]}

#variables
    _separator = ''

    def __init__(self):
        pass

#fixme: value chck
    def setMode(self, fr, to):
        if fr in self._mode:
            if to in self._values:
                self._mode[fr] = to
        if fr in self._flag:
            if to in [True,False]:
                self._flag[fr] = to
        if fr in self._option:
            if to in self._optvals[fr]:
                self._option[fr] = to

    def getConverter(self):

        if self._mode["H"] == "a":
            from h2a import H2a
            self._hconv = H2a(method = self._option["r"]) 
        else:
            from nop import NOP
            self._hconv = NOP()

        if self._mode["K"] == "a":
            from k2a import K2a
            self._kconv = K2a(method = self._option["r"])
        else:
            from nop import NOP
            self._kconv = NOP()

        if self._mode["J"] == "a":
            from j2a import J2a
            self._jconv = J2a(method = self._option["r"])
            if self._flag["C"]:
                self._separator = ' '
            else:
                self._separator = ''

        from nop import NOP
        if self._mode["a"] == None:
            self._aconv = NOP()
        else:
            self._aconv = NOP()

        return self

    def do(self, text):

        otext =  ''
        i = 0
        while True:
            if i >= len(text):
                break

            if self._jconv.isRegion(text[i]):
                (t, l) = self._jconv.convert(text[i:])
                if l <= 0:
                    i = i + 1
                    break
                i = i + l
                if self._flag["c"]:
                    t = t.capitalize()
                if i >= len(text):
                    otext = otext + t
                else:
                    otext = otext + t + self._separator

            elif self._hconv.isRegion(text[i]):
                tmptext = ''
                while True: # eat mode
                    (t, l) = self._hconv.convert(text[i:])
                    tmptext = tmptext+t
                    i = i + l
                    if i >= len(text):
                        otext = otext + tmptext
                        break
                    elif not self._hconv.isRegion(text[i]):
                        otext = otext + tmptext + self._separator
                        break

            elif self._kconv.isRegion(text[i]):
                tmptext = ''
                while True: # eat mode
                    (t, l) = self._kconv.convert(text[i:])
                    tmptext = tmptext+t
                    i = i + l
                    if i >= len(text):
                        otext = otext + tmptext
                        break
                    elif not self._kconv.isRigion(text[i]):
                        otext = otext + tmptext + self._separator
                        break

            else:
                otext  = otext + text[i]
                i += 1

        return otext

