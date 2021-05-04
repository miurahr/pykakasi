# -*- coding: utf-8 -*-
import pytest

import pykakasi


def test_kakasi_unknown_rule():
    with pytest.raises(pykakasi.UnsupportedRomanRulesException):
        kakasi = pykakasi.kakasi()
        kakasi.setMode("H", "a")
        kakasi.setMode("K", "a")
        kakasi.setMode("J", "a")
        kakasi.setMode("r", "hogefuga")


def test_kakasi_unknown_mode():
    with pytest.raises(pykakasi.InvalidModeValueException):
        kakasi = pykakasi.kakasi()
        kakasi.setMode("H", "a")
        kakasi.setMode("K", "a")
        kakasi.setMode("J", "X")


def test_kakasi_invalid_flag_value():
    with pytest.raises(pykakasi.InvalidFlagValueException):
        kakasi = pykakasi.kakasi()
        kakasi.setMode("H", "a")
        kakasi.setMode("K", "a")
        kakasi.setMode("s", "yes")
