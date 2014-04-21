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
            (u"しつもん",   ("shi",1)),
            (u"ちがい", ("chi",1)),
        ]

        h = pykakasi.H2a()
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)

    def test_K2a(self):

        TESTS = [
            (u"カンタン",   ("ka", 1)),
            (u"ニャ", ("nya",2)),
            (u"ッキ", ("kki",2)),
            (u"ッファ", ("ffa", 3)),
            (u"シツモン",   ("shi", 1)),
            (u"チガイ",  ("chi", 1)),
            (u"ジ", ("ji",1)),
        ]

        h = pykakasi.K2a()
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)

    def test_H2a_kunrei(self):

        TESTS = [
            (u"しつもん",   ("si",1)),
            (u"ちがい", ("ti",1)),
            (u"きゃ", ("kya", 2)), (u"きゅ", ("kyu", 2)), (u"きょ", ("kyo", 2)),
            (u"しゃ", ("sya", 2)), (u"しゅ", ("syu", 2)), (u"しょ", ("syo", 2)),
            (u"ちゃ", ("tya", 2)), (u"ちゅ", ("tyu", 2)), (u"ちょ", ("tyo", 2)),
            (u"にゃ", ("nya", 2)), (u"にゅ", ("nyu", 2)), (u"にょ", ("nyo", 2)),
            (u"りゃ", ("rya", 2)), (u"りゅ", ("ryu", 2)), (u"りょ", ("ryo", 2)),
            (u"ざ", ("za", 1)), (u"じ", ("zi", 1)), (u"ず", ("zu", 1)),
            (u"ぜ", ("ze", 1)), (u"ぞ", ("zo", 1)),
            (u"だ", ("da", 1)), (u"ぢ", ("zi", 1)), (u"づ", ("zu", 1)),
            (u"で", ("de", 1)), (u"ど", ("do", 1)),
            (u"た", ("ta", 1)), (u"ち", ("ti", 1)), (u"つ", ("tu", 1)),
            (u"て", ("te", 1)), (u"と", ("to", 1))
        ]

        h = pykakasi.H2a(method="Kunrei")
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)

    def test_K2a_kunrei(self):

        TESTS = [
            (u"シツモン",   ("si", 1)),
            (U"チガイ", ("ti", 1)),
            (u"ジ", ("zi",1)),
            (u"ファジー", ("fa", 2)),
            (u"ジー", ("zi", 1)),
            (u"ウォークマン", ("u", 1)),
            (u"キャ", ("kya", 2)), (u"キュ", ("kyu", 2)), (u"キョ", ("kyo", 2)),
            (u"シャ", ("sya", 2)), (u"シュ", ("syu", 2)), (u"ショ", ("syo", 2)),
            (u"チャ", ("tya", 2)), (u"チュ", ("tyu", 2)), (u"チョ", ("tyo", 2)),
            (u"ニャ", ("nya", 2)), (u"ニュ", ("nyu", 2)), (u"ニョ", ("nyo", 2)),
            (u"リャ", ("rya", 2)), (u"リュ", ("ryu", 2)), (u"リョ", ("ryo", 2)),
            (u"ザ", ("za", 1)), (u"ジ", ("zi", 1)), (u"ズ", ("zu", 1)),
            (u"ゼ", ("ze", 1)), (u"ゾ", ("zo", 1)),
            (u"ダ", ("da", 1)), (u"ヂ", ("zi", 1)), (u"ヅ", ("zu", 1)),
            (u"デ", ("de", 1)), (u"ド", ("do", 1)),
            (u"タ", ("ta", 1)), (u"チ", ("ti", 1)), (u"ツ", ("tu", 1)),
            (u"テ", ("te", 1)), (u"ト", ("to", 1))
        ]

        h = pykakasi.K2a(method="Kunrei")
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

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","a")
        kakasi.setMode("K","a")
        kakasi.setMode("J","a")
        kakasi.setMode("r","Hepburn")
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.failUnlessEqual(converter.do(case), result)


