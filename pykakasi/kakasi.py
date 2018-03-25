# -*- coding: utf-8 -*-
#  kakasi.py
#
# Copyright 2011-2018 Hiroshi Miura <miurahr@linux.com>
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
__license__ = 'GPL 3'
__copyright__ = '2014-2018 Hiroshi Miura <miurahr@linux.com>'
__docformat__ = 'restructuredtext en'

'''
Flags: 
  These flags are as same as KAKASI.

  p: List all possible readings. If there exist two or more
     possible readings, KAKASI shows them in braces {aaa,bbb}.(not implemented yet)
  s: Insert a separate character between words.
  f: Furigana mode. Shows the original kanji word with reading.
  c: Skip characters within word. ( default TAB CR LF BLANK )(not implemented yet)
  C: Capitalize Romaji word (with -Ja or -Jj option)
  U: Upcase romaji word (with -Ja or -Jj option)
  u: Unbufferd mode.(not implemented yet)
  w: wakatigaki mode. 'wakatigaki' is word segmentation for
     Japanese sentences.(implemented as wakati class)

'''

import re
import sys, os
from pykakasi.exceptions import InvalidFlagValueException,InvalidModeValueException,UnsupportedRomanRulesException,UnknownOptionsException

class kakasi(object):

    _keys = ["J","H","K","a","E"]
    _values = ["a","E","H","K",None]
    _roman_vals = ["Hepburn", "Kunrei", "Passport"]
    _endmark = [0x002c, 0x002e, 0x3001, 0x3002]
    _MAXLEN  = 32

    def __init__(self):
        self._conv = {}
        self._mode = {"J":None, "H":None, "K":None, "E":None, "a":None}
        self._flag = {"p":False, "s":False, "f":False, "c":False, "C":False, "U":False,
                      "u":False}
        self._option = {"r":"Hepburn"}
        self._separator = ' '
        self._separator_string = ' '
        pass

#fixme: value chck
    def setMode(self, fr, to):
        if fr in self._keys:
            if to in self._values:
                self._mode[fr] = to
            else:
                raise InvalidModeValueException("Invalid value for mode")
        elif fr in self._flag.keys():
            if to in [True,False]:
                self._flag[fr] = to
            else:
                raise InvalidFlagValueException("Invalid flag value")
        elif fr == "r":
            if to in ["Hepburn","Kunrei","Passport"]:
                self._option["r"] = to
            else:
                raise UnsupportedRomanRulesException("Unknown roman table name")
        elif fr == "S":
            self._separator = to
        else:
            raise UnknownOptionsException("Unhandled options")

    def getConverter(self):
        from .nop import NOP

        if self._mode["H"] == "a":
            from .h2a import H2a
            self._conv["H"] = H2a(method = self._option["r"])
        elif self._mode["H"] == "K":
            from .h2k import H2K
            self._conv["H"] = H2K()
        else:
            self._conv["H"] = NOP()

        if self._mode["K"] == "a":
            from .k2a import K2a
            self._conv["K"] = K2a(method = self._option["r"])
        elif self._mode["K"] == "H":
            from .k2h import K2H
            self._conv["K"] = K2H()
        else:
            self._conv["K"] = NOP()

        if self._mode["J"] == "a":
            from .j2a import J2a
            self._conv["J"] = J2a(method = self._option["r"])
        elif self._mode["J"] == "H":
            from .j2h import J2H
            self._conv["J"] = J2H()
        elif self._mode["J"] == "K":
            from .j2k import J2K
            self._conv["J"] = J2K()
        else:
            self._conv["J"] = NOP()

        if self._mode["a"] == "E":
            from .a2 import a2
            self._conv["a"] = a2()
        else:
            self._conv["a"] = NOP()

        if self._mode["E"] == "a":
            from .symbols import sym2
            self._conv["E"] = sym2()
        else:
            self._conv["E"] = NOP()

        if not self._flag["s"]:
            self._separator = ''

        return self

    def do(self, text):

        otext =  ''
        i = 0
        while True:
            if i >= len(text):
                break

            if self._conv["J"].isRegion(text[i]):
                w = min(i+self._MAXLEN, len(text))
                (t, l) = self._conv["J"].convert(text[i:w])

                if l <= 0: # fails to convert
                    i += 1 # pragma: no cover
                    continue

                i = i + l
                # now i have been incremented..Clarify it by using var j
                j = i
                if self._flag["U"]:
                    otext = otext + t.upcase()
                elif self._flag["C"]:
                    otext = otext + t.capitalize()
                else:
                    otext = otext + t

                # Not insert space BEFORE end marks and text end.
                if (j < len(text)) and not (ord(text[j]) in self._endmark):
                    otext = otext + self._separator

            elif self._conv["H"].isRegion(text[i]):
                tmptext = ''
                while True: # eat mode
                    w = min(i+self._MAXLEN, len(text))
                    (t, l) = self._conv["H"].convert(text[i:w])
                    if l <= 0:
                        # XXX: problem happens.
                        i += 1 # pragma: no cover
                        continue # pragma: no cover
                    tmptext = tmptext + t
                    i = i + l
                    # now i have been incremented..Clarify it by using var j
                    j = i
                    if j >= len(text):
                        otext = otext + tmptext
                        break
                    elif not self._conv["H"].isRegion(text[j]):
                        # Found a place _conv["H"] cannot convert.
                        # this means we found word boundary.
                        otext = otext + tmptext
                        # Inserting word separator(space) to indicate word boundary.
                        # Not inserting space BEFORE comma and full stop
                        if not ord(text[j]) in self._endmark:
                            otext = otext + self._separator
                        break
                    else:
                        pass # pragma: no cover

            elif self._conv["K"].isRegion(text[i]):
                tmptext = ''
                while True: # eat mode
                    w = min(i+self._MAXLEN, len(text))
                    (t, l) = self._conv["K"].convert(text[i:w])
                    if l <= 0:
                        # XXX: problem happens.
                        i += 1 # pragma: no cover
                        continue
                    tmptext = tmptext + t
                    i = i + l
                    # now i have been incremented..Clarify it by using var j
                    j = i
                    if j >= len(text):
                        # finished all text
                        otext = otext + tmptext
                        break
                    elif not self._conv["K"].isRegion(text[j]):
                        # this means we found word boundary.
                        # Inserting ' ' to indicate word boundary.
                        # except for end marks
                        otext = otext + tmptext
                        # Inserting word separator(space) to indicate word boundary.
                        # Not inserting space BEFORE comma and full stop
                        if not ord(text[j]) in self._endmark:
                            otext = otext + self._separator
                        break
                    else:
                        pass

            elif self._conv["a"].isRegion(text[i]):
                otext = otext + self._conv["a"].convert(text[i])
                i += 1

            elif self._conv["E"].isRegion(text[i]):
                otext = otext + self._conv["E"].convert(text[i])
                i += 1
                if i >= len(text): # it is last char of text
                    break
                if text[i] == "\n": # it is last char of line
                    break
                if ord(text[i-1]) in self._endmark:
                    otext = otext + self._separator

            else:
                otext  = otext + text[i]
                i += 1

        return otext

