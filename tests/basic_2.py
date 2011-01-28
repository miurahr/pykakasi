# -*- coding: utf-8 -*-
import unittest
import pykakasi

class TestPyKakasi(unittest.TestCase):

    def test_J2H(self):

        TESTS = [
            (u"構成",         (u"こうせい",2)),
            (u"好き",          (u"すき",2)),
            (u"大きい",       (u"おおき",2)),
      ]

        I_TEST = [
            (u"菟", u"兎"),
            (u"菟集", u"兎集"),
            (u"熙", u"煕"),
        ]

        j = pykakasi.J2H()
        for case, result in TESTS:
            self.failUnlessEqual(j.convert(case), result)
        for case, result in I_TEST:
            self.failUnlessEqual(j.itaiji_conv(case), result)

    def test_H2a(self):

        TESTS = [
            (u"かんたん",   ("ka", 1)),
            (u"にゃ", ("nya",2)),
            (u"っき", ("kki",2)),
            (u"っふぁ", ("ffa", 3)),
        ]

        h = pykakasi.H2a()
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)

    def test_H2a(self):

        TESTS = [
            (u"カンタン",   ("ka", 1)),
            (u"ニャ", ("nya",2)),
            (u"ッキ", ("kki",2)),
            (u"ッファ", ("ffa", 3)),
        ]

        h = pykakasi.K2a()
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)

    def test_kakasi(self):

        TESTS = [
            (u"構成",         "Kousei"),
            (u"好き",          "Suki"),
            (u"大きい",       "Ooki i"),
            (u"かんたん",  "kantan"),
            (u"にゃ",          "nya"),
            (u"っき",           "kki"),
            (u"っふぁ",        "ffa"),
            (u"漢字とひらがな交じり文", "Kanji tohiragana Majiri Bun"),
            (u"Alphabet 123 and 漢字", "Alphabet 123 and Kanji"),
            (u"日経新聞", "Nikkeishinbun"),
        ]

        k = pykakasi.kakasi()
        for case, result in TESTS:
            self.failUnlessEqual(k.do(case), result)


