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
    _conv = {}

#mode flags
    _flag = {"C":True, "c":True}
    _mode = {"J":"a", "H":"a", "K":"a", "a":None, "r":"Hepburn"}
    _values = ["a", "H", "K"]
    _option = {"r":"Hepburn"}
    _optvals = {"r":["Hepburn", "Kunrei"]}

#variables
    _separator = ' '
    _endmark = [0x002c, 0x002e, 0x3001, 0x3002]

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
        from .nop import NOP

        if self._mode["H"] == "a":
            from .h2a import H2a
            self._conv["H"] = H2a(method = self._option["r"])
        elif self._mode["H"] == "k":
            from .h2k import H2K
            self._conv["H"] = H2K()
        else:
            self._conv["H"] = NOP()

        if self._mode["K"] == "a":
            from .k2a import K2a
            self._conv["K"] = K2a(method = self._option["r"])
        elif self._mode["K"] == "h":
            from .k2h import K2H
            self._conv["K"] = K2H()
        else:
            self._conv["K"] = NOP()

        if self._mode["J"] == "a":
            from .j2a import J2a
            self._conv["J"] = J2a(method = self._option["r"])
        elif self._mode["J"] == "h":
            from .j2h import J2H
            self._conv["J"] = J2H()
        elif self._mode["J"] == "k":
            from .j2k import J2k
            self._conv["J"] = J2k(method = self._option["r"])
        else:
            self._conv["J"] = NOP()

        if self._mode["a"] == None:
            self._conv["a"] = NOP()
        else:
            self._conv["a"] = NOP()

        if self._flag["C"]:
            self._separator = ' '
        else:
            self._separator = ''

        return self

    def do(self, text):

        otext =  ''
        i = 0
        while True:
            if i >= len(text):
                break

            if self._conv["J"].isRegion(text[i]):
                (t, l) = self._conv["J"].convert(text[i:])
                if l <= 0:
                    i += 1
                    continue
                i = i + l
                if self._flag["c"]:
                    t = t.capitalize()
                otext = otext + t
                # Not insert space BEFORE end marks and text end.
                if (i < len(text)) and not (ord(text[i]) in self._endmark):
                    otext = otext + self._separator

            elif self._conv["H"].isRegion(text[i]):
                tmptext = ''
                while True: # eat mode
                    (t, l) = self._conv["H"].convert(text[i:])
                    if l <= 0:
                        # XXX: problem happens.
                        i += 1
                        continue
                    tmptext = tmptext + t
                    i = i + l
                    if i >= len(text):
                        if self._flag["c"]:
                            otext = otext + tmptext.capitalize()
                        else:
                            otext = otext + tmptext
                        break
                    elif not self._conv["H"].isRegion(text[i]):
                        # Found a place _conv["H"] cannot convert.
                        # this means we found word boundary.
                        if self._flag["c"]:
                            otext = otext + tmptext.capitalize()
                        else:
                            otext = otext + tmptext
                        # Inserting word separator(space) to indicate word boundary.
                        # Not inserting space BEFORE comma and full stop
                        if not ord(text[i]) in self._endmark:
                            otext = otext + self._separator
                        break
                    else:
                        pass

            elif self._conv["K"].isRegion(text[i]):
                tmptext = ''
                while True: # eat mode
                    (t, l) = self._conv["K"].convert(text[i:])
                    if l <= 0:
                        # XXX: problem happens.
                        i += 1
                        continue
                    if self._flag["c"]:
                        t = t.capitalize()
                    tmptext = tmptext + t
                    i = i + l
                    if i >= len(text):
                        # finished all text
                        if self._flag["c"]:
                            otext = otext + tmptext.capitalize()
                        else:
                            otext = otext + tmptext
                        break
                    elif not self._conv["K"].isRegion(text[i]):
                        # this means we found word boundary.
                        # Inserting ' ' to indicate word boundary.
                        # except for end marks
                        if self._flag["c"]:
                            otext = otext + tmptext.capitalize()
                        else:
                            otext = otext + tmptext
                        # Inserting word separator(space) to indicate word boundary.
                        # Not inserting space BEFORE comma and full stop
                        if not ord(text[i]) in self._endmark:
                            otext = otext + self._separator
                        break
                    else:
                        pass

            else:
                otext  = otext + text[i]
                i += 1

        return otext

