# -*- coding: utf-8 -*-
#  kakasi.py
#
# Copyright 2011-2021 Hiroshi Miura <miurahr@linux.com>
#
import enum
from typing import Dict, List, Tuple

import jaconv

from .kanji import Itaiji, JConv
from .properties import Ch
from .scripts import A2, H2, IConv, K2, Sym2


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

    def _isAlpha(self, c: str):
        return A2.isRegion(c)

    def _isSymbol(self, c: str):
        return Sym2.isRegion(c)

    def _isKana(self, c: str):
        return K2.isRegion(c)

    def _isHira(self, c: str):
        return H2.isRegion(c)

    def _isKanji(self, c: str):
        return 0x3400 <= ord(c[0]) < 0xE000 or self._itaiji.haskey(ord(c[0]))

    def convert(self, text: str) -> List[Dict[str, str]]:
        """Convert input text to dictionary contains KANA, HIRA and romaji results."""

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

        original_text = ""
        kana_text = ""
        _result = []
        i = 0
        prev_type = _TYPE.KANJI
        output_flag: Tuple[bool, bool, bool] = (False, False, False)

        while i < len(text):
            # output_flag
            # means (output buffer?, output text[i]?, copy and increment i?)
            # possible (False, True, True), (True, False, False), (True, True, True)
            #          (False, False, True)
            if text[i] in Ch.endmark:
                prev_type = _TYPE.SYMBOL
                output_flag = (True, True, True)
            elif text[i] in Ch.long_symbols:
                # FIXME: special case
                output_flag = (False, False, True)
            elif self._isSymbol(text[i]):
                if prev_type != _TYPE.SYMBOL:
                    output_flag = (True, False, True)
                else:
                    output_flag = (False, True, True)
                prev_type = _TYPE.SYMBOL
            elif self._isKana(text[i]):
                output_flag = (prev_type != _TYPE.KANA, False, True)
                prev_type = _TYPE.KANA
            elif self._isHira(text[i]):
                output_flag = (prev_type != _TYPE.HIRAGANA, False, True)
                prev_type = _TYPE.HIRAGANA
            elif self._isAlpha(text[i]):
                output_flag = (prev_type != _TYPE.ALPHA, False, True)
                prev_type = _TYPE.ALPHA
            elif self._isKanji(text[i]):
                if len(original_text) > 0:
                    _result.append(self._iconv.convert(original_text, kana_text))
                t, ln = self._jconv.convert(text[i:])
                prev_type = _TYPE.KANJI
                if ln > 0:
                    original_text = text[i : i + ln]
                    kana_text = t
                    i += ln
                    output_flag = (False, False, False)
                else:  # unknown kanji
                    original_text = text[i]
                    kana_text = ""
                    i += 1
                    output_flag = (True, False, False)
            else:
                if len(original_text) > 0:
                    _result.append(self._iconv.convert(original_text, kana_text))
                _result.append(self._iconv.convert(text[i], ""))
                i += 1
                output_flag = (False, False, False)

            # Convert to kana and Output based on flag
            if output_flag[0] and output_flag[1]:
                original_text += text[i]
                kana_text += text[i]
                _result.append(self._iconv.convert(original_text, kana_text))
                original_text = ""
                kana_text = ""
                i += 1
            elif output_flag[0] and output_flag[2]:
                if len(original_text) > 0:
                    _result.append(self._iconv.convert(original_text, kana_text))
                original_text = text[i]
                kana_text = text[i]
                i += 1
            elif output_flag[2]:
                original_text += text[i]
                kana_text += text[i]
                i += 1
            else:
                pass

        # last word
        if len(original_text) > 0:
            _result.append(self._iconv.convert(original_text, kana_text))

        return _result
