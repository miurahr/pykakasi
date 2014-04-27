# -*- coding: utf-8 -*-
#  j2k.py
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

class J2K (object):

    _jconv = None
    _hconv = None

    def __init__(self):
        from .j2h import J2H
        from .h2k import H2K
        self._jconv = J2H()
        self._hconv = H2K()

    def isRegion(self, char):
        return self._jconv.isRegion(char)

    def itaiji_conv(self, text):
        return self._jconv.itaiji_conv(text)

    def convert(self, text):
        if not self._jconv.isRegion(text[0]):
            return ("", 0)
            
        (t, l) = self._jconv.convert(text)
        if l <= 0:
            return ("", 0)

        m = 0
        otext = ""

        while True: 
            if m >= len(t):
                break
            (s, n) = self._hconv.convert(t[m:])
            if n <= 0:
                m = m + 1
            else:
                m = m + n
                otext = otext+s

        return (otext, l) 

