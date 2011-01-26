# -*- coding: utf-8 -*-
#  h2a.py
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

from jisyo import jisyo

class H2a (object):

    H2a_table = {
        u"\u3041":"a", u"\u3042":"a",
        u"\u3043":"i", u"\u3044":"i",
        u"\u3045":"u", u"\u3046":"u",
        u"\u3046\u309b":"vu", u"\u3046\u309b\u3041":"va",
        u"\u3046\u309b\u3043":"vi", u"\u3046\u309b\u3047":"ve",
        u"\u3046\u309b\u3049":"vo",
        u"\u3047":"e", u"\u3048":"e",
        u"\u3049":"o", u"\u304a":"o",

        u"\u304b":"ka", u"\u304c":"ga",
        u"\u304d":"ki", u"\u304d\u3083":"kya",
        u"\u304d\u3045":"kyu",
    }

    def convert(self, text):
        for x in xrange(4):
            if text[:x] in self.H2a_table:
                return (self.H2a_table[text[:x]], x) 
        return ("", 1)

