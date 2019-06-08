# -*- coding: utf-8 -*-
#  a2.py
#
# Copyright 2014-2019 Hiroshi Miura <miurahr@linux.com>
#

from __future__ import unicode_literals

from six import unichr


class a2 (object):
    _table_1 = ["\u3000", "\uff01", "\uff02", "\uff03", "\uff04", "\uff05", "\uff06",
                "\uff07", "\uff08", "\uff09", "\uff0a", "\uff0b", "\uff0c", "\uff0d",
                "\uff0e", "\uff0f",  # ！＂＃＄％＆＇（）＊＋，－．／
                "\uff10", "\uff11", "\uff12", "\uff13", "\uff14", "\uff15", "\uff16",
                "\uff17", "\uff18", "\uff19"  # ０...９
                "\uff1a", "\uff1b", "\uff1c", "\uff1d",
                "\uff1e", "\uff1f", "\uff20"]  # ：；＜＝＞？＠
    _table_2 = ["\uff3b", "\uff3c", "\uff3d", "\uff3e", "\uff3f", "\uff40"]  # ［＼］＾＿｀
    _table_3 = ["\uff5b", "\uff5c", "\uff5d", "\uff5e"]  # ｛｜｝～

    def __init__(self, mode):
        if mode == "E":
            self.convert = self.convert_E
        else:
            self.convert = self.convert_noop

    def isRegion(self, char):
        return 0x20 <= ord(char[0]) < 0x7f

    def _convert(self, text):
        c = ord(text[0])
        if 0x20 <= c < 0x41:
            return self._table_1[(c - 0x20)]
        elif 0x41 <= c < 0x5b:
            return unichr(0xff21 + c - 0x0041)  # u\0041A => u\ff21Ａ
        elif 0x5b <= c < 0x61:
            return self._table_2[(c - 0x5b)]
        elif 0x61 <= c < 0x7b:
            return unichr(0xff41 + c - 0x0061)  # u\0061a => u\ff41ａ
        elif 0x7b <= c < 0x7f:
            return self._table_3[(c - 0x7b)]
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
