# -*- coding: utf-8 -*-
import unittest
import pykakasi

class TestPyKakasi(unittest.TestCase):

    def test_J2H(self):

        TESTS = [
            ("構成",         ("こうせい",2)),
            ("好き",         ("すき",2)),
            ("大きい",       ("おおき",2)),
      ]

        I_TEST = [
            ("菟", "兎"),
            ("菟集", "兎集"),
            ("熙", "煕"),
        ]

        j = pykakasi.J2H()
        for case, result in TESTS:
            self.failUnlessEqual(j.convert(case), result)
        for case, result in I_TEST:
            self.failUnlessEqual(j.itaiji_conv(case), result)

    def test_H2a(self):

        TESTS = [
            ("かんたん",   ("ka", 1)),
            ("にゃ", ("nya",2)),
            ("っき", ("kki",2)),
            ("っふぁ", ("ffa", 3)),
            ("しつもん",   ("shi",1)),
            ("ちがい", ("chi",1)),
        ]

        h = pykakasi.H2a()
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)

    def test_K2a(self):

        TESTS = [
            ("カンタン",   ("ka", 1)),
            ("ニャ", ("nya",2)),
            ("ッキ", ("kki",2)),
            ("ッファ", ("ffa", 3)),
            ("シツモン",   ("shi", 1)),
            ("チガイ",  ("chi", 1)),
            ("ジ", ("ji",1)),
        ]

        h = pykakasi.K2a()
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)

    def test_H2a_kunrei(self):

        TESTS = [
            ("しつもん",   ("si",1)),
            ("ちがい", ("ti",1)),
            ("きゃ", ("kya", 2)), ("きゅ", ("kyu", 2)), ("きょ", ("kyo", 2)),
            ("しゃ", ("sya", 2)), ("しゅ", ("syu", 2)), ("しょ", ("syo", 2)),
            ("ちゃ", ("tya", 2)), ("ちゅ", ("tyu", 2)), ("ちょ", ("tyo", 2)),
            ("にゃ", ("nya", 2)), ("にゅ", ("nyu", 2)), ("にょ", ("nyo", 2)),
            ("りゃ", ("rya", 2)), ("りゅ", ("ryu", 2)), ("りょ", ("ryo", 2)),
            ("ざ", ("za", 1)), ("じ", ("zi", 1)), ("ず", ("zu", 1)),
            ("ぜ", ("ze", 1)), ("ぞ", ("zo", 1)),
            ("だ", ("da", 1)), ("ぢ", ("zi", 1)), ("づ", ("zu", 1)),
            ("で", ("de", 1)), ("ど", ("do", 1)),
            ("た", ("ta", 1)), ("ち", ("ti", 1)), ("つ", ("tu", 1)),
            ("て", ("te", 1)), ("と", ("to", 1))
        ]

        h = pykakasi.H2a(method="Kunrei")
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)

    def test_K2a_kunrei(self):

        TESTS = [
            ("シツモン",   ("si", 1)),
            ("チガイ", ("ti", 1)),
            ("ジ", ("zi",1)),
            ("ファジー", ("fa", 2)),
            ("ジー", ("zi", 1)),
            ("ウォークマン", ("u", 1)),
            ("キャ", ("kya", 2)), ("キュ", ("kyu", 2)), ("キョ", ("kyo", 2)),
            ("シャ", ("sya", 2)), ("シュ", ("syu", 2)), ("ショ", ("syo", 2)),
            ("チャ", ("tya", 2)), ("チュ", ("tyu", 2)), ("チョ", ("tyo", 2)),
            ("ニャ", ("nya", 2)), ("ニュ", ("nyu", 2)), ("ニョ", ("nyo", 2)),
            ("リャ", ("rya", 2)), ("リュ", ("ryu", 2)), ("リョ", ("ryo", 2)),
            ("ザ", ("za", 1)), ("ジ", ("zi", 1)), ("ズ", ("zu", 1)),
            ("ゼ", ("ze", 1)), ("ゾ", ("zo", 1)),
            ("ダ", ("da", 1)), ("ヂ", ("zi", 1)), ("ヅ", ("zu", 1)),
            ("デ", ("de", 1)), ("ド", ("do", 1)),
            ("タ", ("ta", 1)), ("チ", ("ti", 1)), ("ツ", ("tu", 1)),
            ("テ", ("te", 1)), ("ト", ("to", 1))
        ]

        h = pykakasi.K2a(method="Kunrei")
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)

    def test_kakasi(self):

        TESTS = [
            ("構成",         "Kousei"),
            ("好き",          "Suki"),
            ("大きい",       "Ooki i"),
            ("かんたん",  "kantan"),
            ("にゃ",          "nya"),
            ("っき",           "kki"),
            ("っふぁ",        "ffa"),
            ("漢字とひらがな交じり文", "Kanji tohiragana Majiri Bun"),
            ("Alphabet 123 and 漢字", "Alphabet 123 and Kanji"),
            ("日経新聞", "Nikkeishinbun"),
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","a")
        kakasi.setMode("K","a")
        kakasi.setMode("J","a")
        kakasi.setMode("r","Hepburn")
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.failUnlessEqual(converter.do(case), result)


