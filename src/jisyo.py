# -*- coding: utf-8 -*-
#  j2h.py
#
# Copyright 2011 Hiroshi Miura <miurahr@linux.com>
#

#
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

import anydbm,marshal
from zlib import uncompress

class jisyo (object):
    kanwadict = None
    jisyo_table = []

    def __init__(self):
        if self.kanwadict is None:
            self.kanwadict = anydbm.open('kanwadict2.db','r')

    def load_jisyo(self, key):
        try:
            table = self.jisyo_table[key]
        except:
            try:
                self.jisyo_table[key]  = marshal.loads(uncompress(self.kanwadict[key]))
            except:
                self.jisyo_table[key] = None
        return self.jisyo_table[key]

