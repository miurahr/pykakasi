# -*- coding: utf-8 -*-
#  wakati.py
#
# Copyright 2014 Hiroshi Miura <miurahr@linux.com>
#
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

from pykakasi.exceptions import (InvalidFlagValueException,
                                 UnknownOptionsException)

from .kakasi import kakasi


class wakati(kakasi):

    _jconv = None
    _separator = " "
    _state = True

    def __init__(self):
        from .j2 import J2
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
