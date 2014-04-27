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

import re
import sys, os
from .kakasi import kakasi

class wakati(kakasi):

    _jconv = None
    _separator = " "
    _state = True

    def __init__(self):
        from .j2h import J2H
        self._jconv = J2H()

    def getConverter(self):
        return self

    def do(self, text):

        if len(text) == 0:
            return ""

        otext =  ''
        i = 0
        while True:
            if i >= len(text):
                break

            if self._jconv.isRegion(text[i]):
                _, l = self._jconv.convert(text[i:])
                if l <= 0:
                    otext = otext + text[i]
                    i += 1
                    self._state = False
                elif (i+l) < len(text):
                    if self._state:
                        otext = otext + text[i:i+l] + self._separator
                    else:
                        otext = otext + self._separator + text[i:i+l] + self._separator
                        self._state = True
                    i = i + l
                else:
                    if self._state:
                        otext = otext + text[i:i+l]
                    else:
                        otext = otext + self._separator + text[i:i+l]
                    break

            else:
                self._state = False
                otext  = otext + text[i]
                i += 1

        return otext

