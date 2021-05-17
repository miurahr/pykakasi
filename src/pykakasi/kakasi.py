# -*- coding: utf-8 -*-
#  kakasi.py
#
# Copyright 2011-2021 Hiroshi Miura <miurahr@linux.com>
#
import enum
from typing import Dict, List

import jaconv

from .kanji import Itaiji, JConv
from .properties import Ch
from .scripts import A2, H2, IConv, K2


class PyKakasiException(Exception):
    pass


class UnknownCharacterException(PyKakasiException):
    pass


class _TYPE(enum.Enum):
    KANJI = 1
    KANA = 2
    HIRAGANA = 3
    SYMBOL = 4
    ALPHA = 5


class Kakasi:
    """Kakasi is a conversion class for Japanese text."""

    def __init__(self):
        self._jconv = JConv()
        self._iconv = IConv()
        self._itaiji = Itaiji()

    @classmethod
    def normalize(cls, text):
        return jaconv.normalize(text)

    def _type(self, c: str):
        if K2.isRegion(c):
            return _TYPE.KANA
        elif A2.isRegion(c):
            return _TYPE.ALPHA
        elif H2.isRegion(c):
            return _TYPE.HIRAGANA
        # always not Kanji
        # elif self._isKanji(c):
        #    return _TYPE.KANJI
        else:
            return _TYPE.SYMBOL

    def _isKanji(self, c: str):
        return 0x3400 <= ord(c[0]) < 0xE000 or self._itaiji.haskey(ord(c[0]))

    def convert(self, text: str) -> List[Dict[str, str]]:
        """Convert input text to dictionary contains KANA, HIRA and romaji results."""
        _state = True

        if len(text) == 0:
            return [
                {
                    "orig": "",
                    "kana": "",
                    "hira": "",
                    "hepburn": "",
                    "passport": "",
                    "kunrei": "",
                }
            ]

        otext = ""
        _result = []
        i = 0
        prev_type = _TYPE.KANJI

        while i < len(text):
            if self._isKanji(text[i]):
                t, ln = self._jconv.convert(text[i:])
                if ln <= 0:
                    # When JConv does not convert text
                    # FIXME: maybe a bug
                    _state = False
                    otext = otext + text[i]  # pass through
                    i += 1
                else:
                    if _state:
                        _result.append(self._iconv.convert(otext + text[i : i + ln], t))
                    else:
                        _result.append(self._iconv.convert(otext, otext))
                        _result.append(self._iconv.convert(text[i : i + ln], t))
                        _state = True
                    otext = ""
                    i += ln
            elif self._type(text[i]) != prev_type:
                if text[i] in Ch.endmark:
                    otext += text[i]
                    _result.append(self._iconv.convert(otext, otext))
                    otext = ""
                    i += 1
                    _state = True
                elif text[i] in self._iconv.LONG_SYMBOLS:
                    otext += text[i]
                    i += 1
                    _state = False
                else:
                    prev_type = self._type(text[i])
                    if len(otext) > 0:
                        _result.append(self._iconv.convert(otext, otext))
                        otext = text[i]
                        _state = False
                        i += 1
                    else:
                        _state = False
                        otext = otext + text[i]
                        i += 1
            else:
                _state = False
                otext = otext + text[i]
                i += 1

                if otext[-1] in Ch.endmark:
                    _result.append(self._iconv.convert(otext, otext))
                    otext = ""
                    _state = True

        if otext:
            # last word
            _result.append(self._iconv.convert(otext, otext))

        return _result
