# -*- coding: utf-8 -*-
#  h2k.py
#
# Copyright 2011,2014 Hiroshi Miura <miurahr@linux.com>
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

from six import unichr
from six.moves import xrange

class H2K (object):

    _diff = 0x30a1 - 0x3041 # KATAKANA LETTER A - HIRAGANA A

    def __init__(self):
        pass

    def isRegion(self, char):
        return (0x3040 < ord(char[0]) and ord(char[0]) < 0x3097)

    def convert(self, text):
        Hstr = ""
        max_len = 0
        r = len(text)
        for x in xrange(r):
            if self.isRegion(text[x]):
                Hstr = Hstr + unichr(ord(text[x]) + self._diff)
                max_len = max_len + 1
            else:
                break
        return (Hstr, max_len)

