# -*- coding: utf-8 -*-
#  kakasi.py
#
# Copyright 2011-2021 Hiroshi Miura <miurahr@linux.com>
#
import enum
from typing import Dict, List, Tuple

import jaconv

from .kanji import JConv
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


class _ACTION(enum.Enum):
    NOBUFOUT_AND_OUTPUT_CURRENT_AND_NEXT = 1
    BUFOUT_AND_SKIP_CURRENT = 2
    BUFOUT_AND_OUTPUT_CURRENT_AND_NEXT = 3
    PUT_AND_NEXT = 4
    BUFOUT_AND_NEXT = 5
    DO_NOTHING = 6


class Kakasi:
    """Kakasi is a conversion class for Japanese text."""

    def __init__(self):
        self._jconv = JConv()
        self._iconv = IConv()

    @classmethod
    def normalize(cls, text):
        return jaconv.normalize(text)

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
        action_flag: _ACTION

        while i < len(text):
            if text[i] in Ch.endmark:
                prev_type = _TYPE.SYMBOL
                action_flag = _ACTION.BUFOUT_AND_NEXT
            elif text[i] in Ch.long_symbols:
                # Just follow previous character type
                # we don't change prev_type
                action_flag = _ACTION.PUT_AND_NEXT
            elif K2.isRegion(text[i]):
                if prev_type == _TYPE.KANA:
                    action_flag = _ACTION.PUT_AND_NEXT
                else:
                    action_flag = _ACTION.BUFOUT_AND_NEXT
                prev_type = _TYPE.KANA
            elif H2.isRegion(text[i]):
                if prev_type == _TYPE.HIRAGANA:
                    action_flag = _ACTION.PUT_AND_NEXT
                else:
                    action_flag = _ACTION.BUFOUT_AND_NEXT
                prev_type = _TYPE.HIRAGANA
            elif A2.isRegion(text[i]):
                if prev_type == _TYPE.ALPHA:
                    action_flag = _ACTION.PUT_AND_NEXT
                else:
                    action_flag = _ACTION.BUFOUT_AND_NEXT
                prev_type = _TYPE.ALPHA
            elif Sym2.isRegion(text[i]):
                if prev_type != _TYPE.SYMBOL:
                    action_flag = _ACTION.BUFOUT_AND_NEXT
                else:
                    action_flag = _ACTION.NOBUFOUT_AND_OUTPUT_CURRENT_AND_NEXT
                prev_type = _TYPE.SYMBOL
            elif self._jconv.isRegion(text[i]):
                # flush first
                if len(original_text) > 0:
                    _result.append(self._iconv.convert(original_text, kana_text))
                t, ln = self._jconv.convert(text[i:], original_text)
                prev_type = _TYPE.KANJI
                if ln > 0:
                    original_text = text[i : i + ln]
                    kana_text = t
                    i += ln
                    action_flag = _ACTION.DO_NOTHING
                else:  # unknown kanji
                    original_text = text[i]
                    kana_text = ""
                    i += 1
                    action_flag = _ACTION.BUFOUT_AND_SKIP_CURRENT
            elif 0xF000 <= ord(text[i]) <= 0xFFFD or 0x10000 <= ord(text[i]) <= 0x10FFFD:
                # PUA: ignore and drop
                prev_type = _TYPE.SYMBOL
                # flush first
                if len(original_text) > 0:
                    _result.append(self._iconv.convert(original_text, kana_text))
                i += 1
                action_flag = _ACTION.DO_NOTHING
            else:
                # flush first
                if len(original_text) > 0:
                    _result.append(self._iconv.convert(original_text, kana_text))
                _result.append(self._iconv.convert(text[i], ""))
                i += 1
                action_flag = _ACTION.DO_NOTHING

            # Convert to kana and Output based on flag
            if action_flag == _ACTION.BUFOUT_AND_OUTPUT_CURRENT_AND_NEXT:
                original_text += text[i]
                kana_text += text[i]
                _result.append(self._iconv.convert(original_text, kana_text))
                original_text = ""
                kana_text = ""
                i += 1
            elif action_flag == _ACTION.BUFOUT_AND_NEXT:
                if len(original_text) > 0:
                    _result.append(self._iconv.convert(original_text, kana_text))
                original_text = text[i]
                kana_text = text[i]
                i += 1
            elif action_flag == _ACTION.PUT_AND_NEXT:
                original_text += text[i]
                kana_text += text[i]
                i += 1
            elif  action_flag == _ACTION.NOBUFOUT_AND_OUTPUT_CURRENT_AND_NEXT:
                if len(original_text) > 0:
                    _result.append(self._iconv.convert(original_text, kana_text))
                _result.append(self._iconv.convert(text[i], text[i]))
                original_text = ""
                kana_text = ""
                i += 1
            elif action_flag == _ACTION.BUFOUT_AND_SKIP_CURRENT:
                if len(original_text) > 0:
                    _result.append(self._iconv.convert(original_text, kana_text))
                original_text = ""
                kana_text = ""
                i += 1
            elif action_flag == _ACTION.DO_NOTHING:
                pass
            else:
                pass

        # last word
        if len(original_text) > 0:
            _result.append(self._iconv.convert(original_text, kana_text))

        return _result
