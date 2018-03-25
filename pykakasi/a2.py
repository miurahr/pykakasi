# -*- coding: utf-8 -*-
#  a2.py
#
# Copyright 2014 Hiroshi Miura <miurahr@linux.com>
#

from six import unichr

class a2 (object):
    _table_1 = [ u"\u3000",u"\uff01",u"\uff02",u"\uff03",u"\uff04",u"\uff05",u"\uff06",
               u"\uff07",u"\uff08",u"\uff09",u"\uff0a",u"\uff0b",u"\uff0c",u"\uff0d",
               u"\uff0e",u"\uff0f",#！＂＃＄％＆＇（）＊＋，－．／
               u"\uff10",u"\uff11",u"\uff12",u"\uff13",u"\uff14",u"\uff15",u"\uff16",
               u"\uff17",u"\uff18",u"\uff19"# ０...９
               u"\uff1a",u"\uff1b",u"\uff1c",u"\uff1d",
               u"\uff1e",u"\uff1f",u"\uff20"]#：；＜＝＞？＠
    _table_2 = [u"\uff3b",u"\uff3c",u"\uff3d",u"\uff3e",u"\uff3f",u"\uff40"]#［＼］＾＿｀
    _table_3 = [u"\uff5b",u"\uff5c",u"\uff5d",u"\uff5e"]#｛｜｝～

    def __init__(self):
        pass

    def isRegion(self, char): 
        return (0x20 <= ord(char[0]) and ord(char[0]) < 0x7f)

    def convert(self, text):
        c = ord(text[0])
        if   (0x20 <= c and c < 0x41):
            return self._table_1[(c-0x20)]
        elif (0x41 <= c and c < 0x5b):
            return unichr(0xff21+c-0x0041)# u\0041A => u\ff21Ａ
        elif (0x5b <= c and c < 0x61):
            return self._table_2[(c-0x5b)]
        elif (0x61 <= c and c < 0x7b):
            return unichr(0xff41+c-0x0061)# u\0061a => u\ff41ａ
        elif (0x7b <= c and c < 0x7f):
            return self._table_3[(c-0x7b)]
        else:
            return None # pragma: no cover
