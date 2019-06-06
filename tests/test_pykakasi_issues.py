# -*- coding: utf-8 -*-

import pykakasi


def test_issues60():
    TESTS = [
        (u"市立", u"しりつ")
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", None)
    kakasi.setMode("K", None)
    kakasi.setMode("J", "H")
    kakasi.setMode("s", False)
    kakasi.setMode("C", True)
    kakasi.setMode("E", None)
    kakasi.setMode("a", None)
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


def test_issues59():
    TESTS = [
        (u"じゃーん", u"じゃーん"),
        (u"ヷヸヹヺ", u"ヷヸヹヺ")
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", None)
    kakasi.setMode("K", "H")
    kakasi.setMode("J", None)
    kakasi.setMode("s", False)
    kakasi.setMode("C", True)
    kakasi.setMode("E", None)
    kakasi.setMode("a", None)
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


def test_kakasi_issues68():
    TESTS = [
        (u"", u""),
        (u"埇", u"よう")
    ]
    kks = pykakasi.kakasi()
    kks.setMode("J", "H")
    convert = kks.getConverter()
    for case, result in TESTS:
        assert convert.do(case) == result
