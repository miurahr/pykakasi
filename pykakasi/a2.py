# -*- coding: utf-8 -*-
#  a2.py
#
# Copyright 2014 Hiroshi Miura <miurahr@linux.com>
#

try:
    unicode
except: #Python3
    unichr = chr

class a2 (object):
    _table_1 = [ "\u3000","u\ff01","u\ff02","u\ff03","u\ff04","u\ff05","u\ff06",
               "u\ff07","u\ff08","u\ff09","u\ff0a","u\ff0b","u\ff0c","u\ff0d",
               "u\ff0e","u\ff0f",#！＂＃＄％＆＇（）＊＋，－．／
               "u\ff10","u\ff11","u\ff12","u\ff13","u\ff14","u\ff15","u\ff16",
               "u\ff17","u\ff18","u\ff19"# ０...９
               "u\ff1a","u\ff1b","u\ff1c","u\ff1d",
               "u\ff1e","u\ff1f","u\ff20"]#：；＜＝＞？＠
    _table_2 = ["u\ff3b","u\ff3c","u\ff3d","u\ff3e","u\ff3f","u\ff40"]#［＼］＾＿｀
    _table_3 = ["u\ff5b","u\ff5c","u\ff5d","u\ff5e"]#｛｜｝～

    def __init__(self):
        pass

    def isRegion(self, char): 
        return (0x20 <= ord(char[0]) and ord(char[0]) < 0x7f)

    def convert(self, text):
        c = ord(text[0])
        if   (0x20 <= c and c < 0x41):
            return _table_1[(c-0x20)]
        elif (0x41 <= c and c < 0x5b):
            return unichr(0xff21+c-0x0041)# u\0041A => u\ff21Ａ
        elif (0x5b <= c and c < 0x61):
            return _table_2[(c-0x5b)]
        elif (0x61 <= c and c < 0x7b):
            return unichr(0xff41+c-0x0061)# u\0061a => u\ff41ａ
        elif (0x7b <= c and c < 0x7f):
            return _table_3[(c-0x7b)]
        else:
            return None


