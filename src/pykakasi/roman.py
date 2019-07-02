# -*- coding: utf-8 -*-
#  roman.py
#
# Copyright 2014-2019 Hiroshi Miura <miurahr@linux.com>

from __future__ import unicode_literals

import six
from six import unichr

from .properties import Ch, Convert_Tables

__license__ = 'GPL 3'
__copyright__ = '2014-2019, Hiroshi Miura <miurahr@linux.com>'
__docformat__ = 'restructuredtext en'


class Sym2:

    def __init__(self, mode):
        if mode == "a":
            self.convert = self.convert_a
        else:
            self.convert = self.convert_noop

    def isRegion(self, char):
        c = ord(char[0])
        return (Ch.ideographic_space <= c <= Ch.postal_mark_face) or \
               (Ch.wavy_dash <= c <= Ch.ideographic_half_fill_space) or \
               (Ch.greece_Alpha <= c <= Ch.greece_Rho) or (Ch.greece_Sigma <= c <= Ch.greece_Omega) or \
               (Ch.greece_alpha <= c <= Ch.greece_omega) or \
               (Ch.cyrillic_A <= c <= Ch.cyrillic_ya) or \
               (Ch.zenkaku_exc_mark <= c <= Ch.zenkaku_number_nine) or \
               (0xff20 <= c <= 0xff5e) or c == 0x0451 or c == 0x0401

    def _convert(self, text):
        c = ord(text[0])
        if Ch.ideographic_space <= c <= Ch.postal_mark_face:
            return Convert_Tables.symbol_table_1[c - Ch.ideographic_space]
        elif Ch.wavy_dash <= c <= Ch.ideographic_half_fill_space:
            return Convert_Tables.symbol_table_2[c - Ch.wavy_dash]
        elif Ch.greece_Alpha <= c <= Ch.greece_Omega:
            return Convert_Tables.symbol_table_3[c - Ch.greece_Alpha]
        elif Ch.greece_alpha <= c <= Ch.greece_omega:
            return Convert_Tables.symbol_table_4[c - Ch.greece_alpha]
        elif Ch.cyrillic_A <= c <= Ch.cyrillic_ya:
            return Convert_Tables.cyrillic_table[text[0]]
        elif c == Ch.cyrillic_E or c == Ch.cyrillic_e:
            return Convert_Tables.cyrillic_table[text[0]]
        elif Ch.zenkaku_exc_mark <= c <= Ch.zenkaku_slash_mark:
            return Convert_Tables.symbol_table_5[c - Ch.zenkaku_exc_mark]
        elif Ch.zenkaku_number_zero <= c <= Ch.zenkaku_number_nine:
            return six.unichr(c - Ch.zenkaku_number_zero + ord('0'))
        elif 0xff20 <= c <= 0xff40:
            return six.unichr(0x0041 + c - 0xff21)  # u\ff21Ａ => u\0041:@A..Z[\]^_`
        elif 0xff41 <= c < 0xff5f:
            return six.unichr(0x0061 + c - 0xff41)  # u\ff41ａ => u\0061:a..z{|}
        else:
            return ""  # pragma: no cover

    def convert_a(self, text):
        t = self._convert(text)
        if len(t):
            return t, 1
        else:
            return "", 0

    def convert_noop(self, text):
        return text[0], 1


class A2:

    def __init__(self, mode):
        if mode == "E":
            self.convert = self.convert_E
        else:
            self.convert = self.convert_noop

    def isRegion(self, char):
        return Ch.space <= ord(char[0]) < Ch.delete

    def _convert(self, text):
        c = ord(text[0])
        if Ch.space <= c <= Ch.at_mark:
            return Convert_Tables.alpha_table_1[(c - Ch.space)]
        elif Ch.alphabet_A <= c <= Ch.alphabet_Z:
            return unichr(Ch.zenkaku_A + c - Ch.alphabet_A)  # u\0041A => u\ff21Ａ
        elif Ch.square_bra <= c <= Ch.back_quote:
            return Convert_Tables.alpha_table_2[(c - Ch.square_bra)]
        elif Ch.alphabet_a <= c <= Ch.alphabet_z:
            return unichr(Ch.zenkaku_a + c - Ch.alphabet_a)  # u\0061a => u\ff41ａ
        elif Ch.bracket_bra <= c <= Ch.tilda:
            return Convert_Tables.alpha_table_3[(c - Ch.bracket_bra)]
        else:
            return ""  # pragma: no cover

    def convert_E(self, text):
        t = self._convert(text)
        if len(t):
            return t, 1
        else:
            return "", 0

    def convert_noop(self, text):
        return text[0], 1
