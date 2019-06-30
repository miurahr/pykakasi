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
__copyright__ = '2014-2019 Hiroshi Miura <miurahr@linux.com>'
__docformat__ = 'restructuredtext en'

import six

from .exceptions import (InvalidFlagValueException, InvalidModeValueException,
                         UnknownOptionsException,
                         UnsupportedRomanRulesException)
from .kana import H2, K2
from .kanji import J2
from .roman import a2, sym2


class kakasi():

    _keys = ["J", "H", "K", "E", "a"]
    _values = ["a", "E", "H", "K"]
    _roman_vals = ["Hepburn", "Kunrei", "Passport"]
    _endmark = [ord(a) for a in [")", "]", "!", ",", "."]] + [0x3001, 0x3002]
    _MAXLEN = 32

    def __init__(self):
        self._conv = {}
        self._mode = {"J": None, "H": None, "K": None, "E": None, "a": None}
        self._furi = {"J": False, "H": False, "K": False, "E": False, "a": False}
        self._flag = {"p": False, "s": False, "f": False, "c": False, "C": False, "U": False,
                      "u": False, "t": True}
        self._option = {"r": "Hepburn"}
        self._separator = ' '
        self._separator_string = ' '
        self._jconv = J2()
        self._haconv = H2("a")
        self._hkconv = H2("K")
        self._khconv = K2("H")
        self._kaconv = K2("a")
        self._aeconv = a2("E")
        self._saconv = sym2("a")

    def convert(self, text):
        _state = True

        if len(text) == 0:
            return ""

        otext = ''
        _result = []
        i = 0
        while True:
            if i >= len(text):
                break

            if self._jconv.isRegion(text[i]):
                t, ln = self._jconv.convert(text[i:])
                if ln <= 0:  # pragma: no cover
                    otext = otext + text[i]
                    i += 1
                    _state = False
                elif (i + ln) < len(text):
                    if _state:
                        _result.append(self._iconv(otext + text[i:i + ln], t))
                        otext = ''
                    else:
                        _result.append(self._iconv(otext, otext))
                        _result.append(self._iconv(text[i:i + ln], t))
                        otext = ''
                        _state = True
                    i = i + ln
                else:
                    if _state:
                        _result.append(self._iconv(otext + text[i:i + ln], t))
                    else:  # pragma: no cover
                        _result.append(self._iconv(otext, otext))
                        _result.append(self._iconv(text[i:i + ln], t))
                    break

            else:
                _state = False
                otext = otext + text[i]
                i += 1

        return _result

    def _iconv(self, otext, hira):
        tmp = {'orig': otext, 'hira': hira}
        tmp['kana'] = self._h2k(hira)
        tmp['hepburn'] = self._h2a(hira)
        return tmp

    def _h2k(self, text):
        result = ''
        i = 0
        while(i < len(text)):
            w = min(i + self._MAXLEN, len(text))
            (t, l1) = self._hkconv.convert(text[i:w])
            if l1 > 0:
                result += t
                i += l1
            else:
                result += text[i:i + 1]
                i += 1
        return result

    def _h2a(self, text):
        result = ''
        i = 0
        while(i < len(text)):
            w = min(i + self._MAXLEN, len(text))
            (t, l1) = self._haconv.convert(text[i:w])
            if l1 > 0:
                result += t
                i += l1
            else:
                result += text[i:i + 1]
                i += 1
        return result

    def setMode(self, fr, to):
        if fr in self._keys:
            if to is None:
                self._mode[fr] = to
            elif to[0] in self._values:
                self._mode[fr] = to[0]
                if len(to) == 2 and to[1] == "F":
                    self._furi[fr] = True
            else:
                raise InvalidModeValueException("Invalid value for mode")
        elif fr in self._flag.keys():
            if to in [True, False]:
                self._flag[fr] = to
            else:
                raise InvalidFlagValueException("Invalid flag value")
        elif fr == "r":
            if to in self._roman_vals:
                self._option["r"] = to
            else:
                raise UnsupportedRomanRulesException("Unknown roman table name")
        elif fr == "S":
            self._separator = to
        else:
            raise UnknownOptionsException("Unhandled options")  # pragma: no cover

    def getConverter(self):
        self._conv["J"] = J2(self._mode["J"], method=self._option["r"])
        self._conv["H"] = H2(self._mode["H"], method=self._option["r"])
        self._conv["K"] = K2(self._mode["K"], method=self._option["r"])
        self._conv["E"] = sym2(self._mode["E"])
        self._conv["a"] = a2(self._mode["a"])
        return self

    def do(self, itext):
        text = six.text_type(itext)

        otext = ""
        i = 0
        while True:
            if i >= len(text):
                break

            if self._conv["J"].isRegion(text[i]):
                mode = "J"
            elif self._conv["H"].isRegion(text[i]):
                mode = "H"
            elif self._conv["K"].isRegion(text[i]):
                mode = "K"
            elif self._conv["E"].isRegion(text[i]):
                mode = "E"
            elif self._conv["a"].isRegion(text[i]):
                mode = "a"
            else:
                mode = "o"

            if mode in ("J", "E"):
                w = min(i + self._MAXLEN, len(text))
                (t, l1) = self._conv[mode].convert(text[i:w])

                if l1 > 0:
                    orig = text[i:i + l1]
                    chunk = t
                    i = i + l1
                else:
                    orig = text[i:i + 1]
                    if self._flag["t"]:
                        chunk = orig
                    else:
                        chunk = "???"
                    i += 1

            elif mode in ("H", "K", "a"):
                orig = ''
                chunk = ''
                while True:  # eat mode
                    w = min(i + self._MAXLEN, len(text))
                    (t, l1) = self._conv[mode].convert(text[i:w])
                    if l1 > 0:  # fails to convert
                        orig += text[i:i + l1]
                        chunk += t
                        i = i + l1
                    elif orig != '':
                        break
                    else:
                        orig = text[i:i + 1]
                        if self._flag["t"]:
                            chunk = orig
                        else:
                            chunk = "???"
                        i += 1
                        break

                    if i >= len(text) or not self._conv[mode].isRegion(text[i]):
                        break

            else:
                otext += text[i]
                i += 1
                continue

            if mode in ("J", "E"):
                if self._flag["U"]:
                    chunk = chunk.upper()
                elif self._flag["C"]:
                    chunk = chunk.capitalize()

            if mode in self._keys and self._furi[mode]:
                otext += orig + "[" + chunk + "]"
            else:
                otext += chunk

            if self._flag["s"] and otext[-len(self._separator):] != self._separator \
                    and i < len(text) and not (ord(text[i]) in self._endmark):
                otext += self._separator

        return otext


class wakati(kakasi):

    _jconv = None
    _separator = " "
    _state = True

    def __init__(self):
        self._jconv = J2("H")
        self._flag = {"f": False}

    def getConverter(self):
        return self

    def setMode(self, fr, to):
        if fr in self._flag.keys():
            if to in [True, False]:
                self._flag[fr] = to
            else:
                raise InvalidFlagValueException("Invalid flag value")
            raise UnknownOptionsException("Unhandled options")

    def do(self, text):

        if len(text) == 0:
            return ""

        otext = ''
        i = 0
        while True:
            if i >= len(text):
                break

            if self._jconv.isRegion(text[i]):
                _, ln = self._jconv.convert(text[i:])
                if ln <= 0:  # pragma: no cover
                    otext = otext + text[i]
                    i += 1
                    self._state = False
                elif (i + ln) < len(text):
                    if self._state:
                        otext = otext + text[i:i + ln] + self._separator
                    else:
                        otext = otext + self._separator + text[i:i + ln] + self._separator
                        self._state = True
                    i = i + ln
                else:
                    if self._state:
                        otext = otext + text[i:i + ln]
                    else:  # pragma: no cover
                        otext = otext + self._separator + text[i:i + ln]
                    break

            else:
                self._state = False
                otext = otext + text[i]
                i += 1

        return otext
