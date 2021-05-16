# -*- coding: utf-8 -*-
#  kakasi.py
#
# Copyright 2011-2021 Hiroshi Miura <miurahr@linux.com>
#
from typing import Dict, List

import jaconv

from .kanji import Itaiji, JConv
from .properties import Ch
from .scripts import IConv


class PyKakasiException(Exception):
    pass


class UnknownCharacterException(PyKakasiException):
    pass


class Kakasi:
    """Kakasi is a conversion class for Japanese text."""

    def __init__(self):
        self._jconv = JConv()
        self._iconv = IConv()
        self._itaiji = Itaiji()

    @classmethod
    def normalize(cls, text):
        return jaconv.normalize(text)

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

        while i < len(text):
            if self._isKanji(text[i]):
                t, ln = self._jconv.convert(text[i:])
                if ln <= 0:  # When JConv successfully convert text
                    _state = False
                    otext = otext + text[i]
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
            else:
                _state = False
                otext = otext + text[i]
                i += 1

                if ord(otext[-1]) in Ch.endmark:
                    _result.append(self._iconv.convert(otext, otext))
                    otext = ""
                    _state = True

        if otext:
            # last word
            _result.append(self._iconv.convert(otext, otext))

        return _result
