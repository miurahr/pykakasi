# -*- coding: utf-8 -*-
#  kakasi.py
#
# Copyright 2011-2018 Hiroshi Miura <miurahr@linux.com>
#

__license__ = 'GPL 3'
__copyright__ = '2014-2020 Hiroshi Miura <miurahr@linux.com>'
__docformat__ = 'restructuredtext en'

from typing import Dict, List, Optional, Union

from .exceptions import (InvalidFlagValueException, InvalidModeValueException,
                         UnknownOptionsException,
                         UnsupportedRomanRulesException)
from .kanji import J2
from .properties import Ch
from .scripts import A2, H2, K2, Sym2


class kakasi:

    _keys = ["J", "H", "K", "E", "a"]  # type: List[str]
    _values = ["a", "E", "H", "K"]  # type: List[str]
    _roman_vals = ["Hepburn", "Kunrei", "Passport"]  # type: List[str]
    _MAXLEN = 32  # type: int
    _LONG_SYMBOL = [
        # 0x002D,  # -
        0x30FC,  # ー
        # 0x2010,  # ‐
        # 0x2011,  # ‑
        # 0x2013,  # –
        # 0x2014,  # —
        0x2015,  # ―
        0x2212,  # −
        0xFF70  # ｰ
    ]  # type: List[int]

    def __init__(self):
        self._conv = {}  # type: Dict[str, Union[J2, H2, K2, A2, Sym2]]
        self._mode = {"J": None, "H": None, "K": None, "E": None, "a": None}  # type: Dict[str, Optional[str]]
        self._furi = {"J": False, "H": False, "K": False, "E": False, "a": False}  # type: Dict[str, bool]
        self._flag = {"p": False, "s": False, "f": False, "c": False, "C": False, "U": False,
                      "u": False, "t": True}  # type: Dict[str, bool]
        self._option = {"r": "Hepburn"}  # type: Dict[str, str]
        self._separator = ' '  # type: str
        self._separator_string = ' '  # type: str
        self._jconv = J2("H")
        self._hahconv = H2("a", method='Hepburn')
        self._hakconv = H2("a", method='Kunrei')
        self._hapconv = H2("a", method='Passport')
        self._hkconv = H2("K")
        self._khconv = K2("H")
        self._kaconv = K2("a")
        self._aeconv = A2("E")
        self._saconv = Sym2("a")

    def convert(self, text: str) -> List[Dict[str, str]]:
        _state = True

        if len(text) == 0:
            return [{'orig': "", 'kana': "", 'hira': "", 'hepburn': "", 'passport': "", 'kunrei': ""}]

        otext = ''
        _result = []
        i = 0
        while True:
            if i >= len(text):
                break

            if self._jconv.isRegion(text[i]):
                t, ln = self._jconv.convert(text[i:])
                if ln <= 0:  # pragma: no cover
                    otext = otext + text[i]
                    i += 1
                    _state = False
                elif (i + ln) < len(text):
                    if _state:
                        _result.append(self._iconv(otext + text[i:i + ln], t))
                        otext = ''
                    else:
                        _result.append(self._iconv(otext, otext))
                        _result.append(self._iconv(text[i:i + ln], t))
                        otext = ''
                        _state = True
                    i = i + ln
                else:
                    if _state:
                        _result.append(self._iconv(otext + text[i:i + ln], t))
                    else:  # pragma: no cover
                        _result.append(self._iconv(otext, otext))
                        _result.append(self._iconv(text[i:i + ln], t))
                    break

            else:
                _state = False
                otext = otext + text[i]
                i += 1

                if ord(otext[-1]) in Ch.endmark:
                    _result.append(self._iconv(otext, otext))
                    otext = ''
                    _state = True

        return _result

    def _iconv(self, otext: str, hira: str) -> Dict[str, str]:
        tmp = {'orig': otext, 'hira': hira}
        tmp['kana'] = self._h2k(hira)
        tmp['hepburn'] = self._s2a(self._h2ah(hira))
        tmp['kunrei'] = self._s2a(self._h2ak(hira))
        tmp['passport'] = self._s2a(self._h2ap(hira))
        return tmp

    def _s2a(self, text: str) -> str:
        result = ''  # type: str
        i = 0
        while(i < len(text)):
            w = min(i + self._MAXLEN, len(text))  # type: int
            (t, l1) = self._saconv.convert(text[i:w])
            if l1 > 0:
                result += t
                i += l1
            else:
                result += text[i:i + 1]
                i += 1
        return result

    def _h2k(self, text: str) -> str:
        result = ''
        i = 0
        while(i < len(text)):
            w = min(i + self._MAXLEN, len(text))
            (t, l1) = self._hkconv.convert(text[i:w])
            if l1 > 0:
                result += t
                i += l1
            else:
                result += text[i:i + 1]
                i += 1
        return result

    def _h2ak(self, text: str) -> str:
        result = ''
        i = 0
        while(i < len(text)):
            w = min(i + self._MAXLEN, len(text))
            (t, l1) = self._hakconv.convert(text[i:w])
            if l1 > 0:
                result += t
                i += l1
            else:
                result += text[i:i + 1]
                i += 1
        return result

    def _h2ah(self, text: str) -> str:
        result = ''
        i = 0
        while(i < len(text)):
            w = min(i + self._MAXLEN, len(text))
            (t, l1) = self._hahconv.convert(text[i:w])
            if l1 > 0:
                result += t
                i += l1
            else:
                result += text[i:i + 1]
                i += 1
        return result

    def _h2ap(self, text: str) -> str:
        result = ''
        i = 0
        while(i < len(text)):
            w = min(i + self._MAXLEN, len(text))
            (t, l1) = self._hapconv.convert(text[i:w])
            if l1 > 0:
                result += t
                i += l1
            else:
                result += text[i:i + 1]
                i += 1
        return result

    def setMode(self, fr: str, to: Optional[Union[bool, str]]) -> None:
        if fr in self._keys:
            if to is None:
                self._mode[fr] = None
            elif isinstance(to, str) and to[0] in self._values:
                self._mode[fr] = to[0]
                if len(to) == 2 and to[1] == "F":
                    self._furi[fr] = True
            else:
                raise InvalidModeValueException("Invalid value for mode")
        elif fr in self._flag.keys():
            if isinstance(to, bool):
                self._flag[fr] = to
            else:
                raise InvalidFlagValueException("Invalid flag value")
        elif fr == "r":
            if isinstance(to, str) and to in self._roman_vals:
                self._option["r"] = to
            else:
                raise UnsupportedRomanRulesException("Unknown roman table name")
        elif fr == "S":
            if isinstance(to, str):
                self._separator = to
            else:
                raise InvalidFlagValueException("Incompatible separator value")
        else:
            raise UnknownOptionsException("Unhandled options")  # pragma: no cover

    def getConverter(self):
        self._conv["J"] = J2(self._mode["J"], method=self._option["r"])
        self._conv["H"] = H2(self._mode["H"], method=self._option["r"])
        self._conv["K"] = K2(self._mode["K"], method=self._option["r"])
        self._conv["E"] = Sym2(self._mode["E"])
        self._conv["a"] = A2(self._mode["a"])
        return self

    def do(self, text: str) -> str:
        otext = ""
        i = 0
        while True:
            if i >= len(text):
                break

            if self._conv["J"].isRegion(text[i]):
                mode = "J"
            elif self._conv["H"].isRegion(text[i]):
                mode = "H"
            elif self._conv["K"].isRegion(text[i]):
                mode = "K"
            elif self._conv["E"].isRegion(text[i]):
                mode = "E"
            elif self._conv["a"].isRegion(text[i]):
                mode = "a"
            else:
                mode = "o"

            if mode in ("J", "E"):
                w = min(i + self._MAXLEN, len(text))
                (t, l1) = self._conv[mode].convert(text[i:w])

                if l1 > 0:
                    orig = text[i:i + l1]
                    chunk = t
                    i += l1
                else:
                    orig = text[i:i + 1]
                    if self._flag["t"]:
                        chunk = orig
                    else:
                        chunk = "???"
                    i += 1

            elif mode in ("H", "K", "a"):
                orig = ''
                chunk = ''

                while i < len(text):

                    if ord(text[i]) in self._LONG_SYMBOL:

                        # FIXME: q&d workaround when hiragana/katanaka dash is first char.
                        if self._mode[mode] is not None and len(chunk) > 0:
                            # use previous char as a transliteration for kana-dash
                            orig += text[i]
                            chunk = chunk + chunk[-1]
                            i += 1
                        elif len(chunk) == 0:
                            orig += text[i]
                            chunk += '-'
                            i += 1
                            break
                        else:
                            orig += text[i]
                            chunk += text[i]
                            i += 1
                            break

                    elif self._conv[mode].isRegion(text[i]):
                        w = min(i + self._MAXLEN, len(text))
                        (t, l1) = self._conv[mode].convert(text[i:w])
                        if l1 > 0:
                            orig += text[i:i + l1]
                            chunk += t
                            i += l1
                        else:
                            orig = text[i:i + 1]
                            if self._flag["t"]:
                                chunk = orig
                            else:
                                chunk = "???"
                            i += 1
                            break

                    else:
                        # i += 1
                        break

            else:
                otext += text[i]
                i += 1
                continue

            if mode in ("J", "E"):
                if self._flag["U"]:
                    chunk = chunk.upper()
                elif self._flag["C"]:
                    chunk = chunk.capitalize()

            if mode in self._keys and self._furi[mode]:
                otext += orig + "[" + chunk + "]"
            else:
                otext += chunk

            # insert separator when option specified and it is not a last character and not an end mark
            if self._flag["s"] and otext[-len(self._separator):] != self._separator \
                    and i < len(text) and not (ord(text[i]) in Ch.endmark):
                otext += self._separator

        return otext


class wakati(kakasi):

    def __init__(self):
        super(wakati, self).__init__()
        self._state = True  # type: bool

    def getConverter(self):
        return self

    def setMode(self, fr: str, to: Optional[Union[bool, str]]) -> None:
        if fr in self._flag.keys():
            if isinstance(to, bool):
                self._flag[fr] = to
            else:
                raise InvalidFlagValueException("Invalid flag value")
            raise UnknownOptionsException("Unhandled options")

    def do(self, text: str) -> str:

        if len(text) == 0:
            return ""

        otext = ''
        i = 0
        while True:
            if i >= len(text):
                break

            if self._jconv.isRegion(text[i]):
                _, ln = self._jconv.convert(text[i:])
                if ln <= 0:  # pragma: no cover
                    otext = otext + text[i]
                    i += 1
                    self._state = False
                elif (i + ln) < len(text):
                    if self._state:
                        otext = otext + text[i:i + ln] + self._separator
                    else:
                        otext = otext + self._separator + text[i:i + ln] + self._separator
                        self._state = True
                    i = i + ln
                else:
                    if self._state:
                        otext = otext + text[i:i + ln]
                    else:  # pragma: no cover
                        otext = otext + self._separator + text[i:i + ln]
                    break

            else:
                self._state = False
                otext = otext + text[i]
                i += 1

        return otext
