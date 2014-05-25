# -*- coding: utf-8 -*-
import unittest
import pykakasi

class TestPyKakasi(unittest.TestCase):

    def test_J2H(self):

        TESTS = [
            ("構成",         ("こうせい",2)),
            ("好き",         ("すき",2)),
            ("大きい",       ("おおきい",3)),
            ("日本国民は、", ("にほんこくみん", 4))
      ]

        I_TEST = [
            ("菟", "兎"),
            ("菟集", "兎集"),
            ("熙", "煕"),
        ]

        j = pykakasi.J2H()
        for case, result in TESTS:
            self.assertEqual(j.convert(case), result)
        for case, result in I_TEST:
            self.assertEqual(j.itaiji_conv(case), result)

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
            self.assertEqual(h.convert(case), result)


    def test_H2K(self):

        TESTS = [
            ("かんたん",   ("カンタン", 4)),
            ("にゃ",       ("ニャ",2)),
            ("っき",       ("ッキ",2)),
            ("っふぁ",     ("ッファ", 3)),
            ("しつもん",   ("シツモン",4)),
            ("ちがい",     ("チガイ",3)),
        ]

        h = pykakasi.H2K()
        for case, result in TESTS:
            self.assertEqual(h.convert(case), result)

    def test_K2H(self):

        TESTS = [
            ("カンタン",   ("かんたん", 4)),
            ("ニャ",       ("にゃ",2)),
            ("ッキ",       ("っき",2)),
            ("ッファ",     ("っふぁ", 3)),
            ("シツモン",   ("しつもん",4)),
            ("チガイ",     ("ちがい",3)),
        ]

        h = pykakasi.K2H()
        for case, result in TESTS:
            self.assertEqual(h.convert(case), result)

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
            self.assertEqual(h.convert(case), result)

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
            self.assertEqual(h.convert(case), result)

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
            self.assertEqual(h.convert(case), result)

    def test_H2a_passport(self):

        TESTS = [
            ("しつもん",("shi",1)),
            ("ちがい", ("chi",1)),
            ("おおの",("o",2)),
            ("さいとう",("sa",1)),
            ("とう",("to",2)),
            ("なんば", ("na", 1)),
            ("んば", ("mba", 2))
        ]

        h = pykakasi.H2a(method="Passport")
        for case, result in TESTS:
            self.assertEqual(h.convert(case), result)

    def test_J2K(self):

        TESTS = [
            ("構成",         ("コウセイ",2)),
            ("好き",         ("スキ",2)),
            ("大きい",       ("オオキイ",3)),
            ("日本国民は、", ("ニホンコクミン", 4))
      ]

        I_TEST = [
            ("菟", "兎"),
            ("菟集", "兎集"),
            ("熙", "煕"),
        ]

        j = pykakasi.J2K()
        for case, result in TESTS:
            self.assertEqual(j.convert(case), result)
        for case, result in I_TEST:
            self.assertEqual(j.itaiji_conv(case), result)

    def test_J2a(self):

        TESTS = [
            ("構成",         ("kousei",2)),
            ("好き",         ("suki",2)),
            ("大きい",       ("ookii",3)),
            ("日本国民は、", ("nihonkokumin", 4))
      ]

        j = pykakasi.J2a()
        for case, result in TESTS:
            self.assertEqual(j.convert(case), result)

    def test_J2a_kunrei(self):

        TESTS = [
            ("構成",         ("kousei",2)),
            ("好き",         ("suki",2)),
            ("大きい",       ("ookii",3)),
            ("日本国民は、", ("nihonkokumin", 4)),
            ("漢字",         ("kanzi",2))
      ]

        j = pykakasi.J2a(method="Kunrei")
        for case, result in TESTS:
            self.assertEqual(j.convert(case), result)

    def test_J2a_passport(self):

        TESTS = [
            ("構成",         ("kosei",2)),
            ("好き",         ("suki",2)),
            ("大きい",       ("okii",3)),
            ("日本国民は、", ("nihonkokumin", 4)),
            ("漢字",         ("kanji", 2)),
            ("佐藤",         ("sato", 2)),
            ("難波",         ("namba",2))
      ]

        j = pykakasi.J2a(method="Passport")
        for case, result in TESTS:
            self.assertEqual(j.convert(case), result)

    def test_a2(self):

        TESTS = [
            ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
             "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"),
            ("abcdefghijklmnopqrstuvwxyz",
             "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ")
      ]

        a = pykakasi.a2()
        for case, result in TESTS:
            for i in range(26):
                self.assertEqual(a.convert(case[i]), result[i])

    def test_sym2(self):

        TESTS = [
            (["　","、","。","〃","〄","〆","〈","〉","《","》","「","」","『",
            "』","【","】","〒","〓","〔","〕","〖","〗","〘","〙","〚","〛",
            "〜","〝","〞","〟","〠","〰","〱","〲","〳","〴","〵","〶","〷",
            "〼","〽","〾","〿"],
             [" ",",",".",'"',"(kigou)","(sime)","<",">","<<",">>","(",")","(",")",
            "(",")","(kigou)","(geta)","(",")","(",")","(",")","(",
            ")","~","(kigou)","\"","(kigou)","(kigou)","-","(kurikaesi)",
            "(kurikaesi)","(kurikaesi)","(kurikaesi)","(kurikaesi)",
            "(kigou)","XX","(masu)","(kurikaesi)"," "," "])
      ]

        s = pykakasi.sym2()
        for case, result in TESTS:
            for i in range(len(case)):
                self.assertEqual(tuple([case[i],s.convert(case[i])]), tuple([case[i],result[i]]))

    def test_kakasi(self):

        TESTS = [
            ("構成",         "Kousei"),
            ("好き",         "Suki"),
            ("大きい",       "Ookii"),
            ("かんたん",     "kantan"),
            ("にゃ",         "nya"),
            ("っき",         "kki"),
            ("っふぁ",       "ffa"),
            ("漢字とひらがな交じり文", "Kanji tohiragana Majiri Bun"),
            ("Alphabet 123 and 漢字", "Alphabet 123 and Kanji"),
            ("日経新聞", "Nikkeishinbun"),
            ("日本国民は、","Nihonkokumin ha,")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","a")
        kakasi.setMode("K","a")
        kakasi.setMode("J","a")
        kakasi.setMode("r","Hepburn")
        kakasi.setMode("C",True)
        kakasi.setMode("s",True)
        kakasi.setMode("E","a")
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)

    def test_kakasi_kunrei(self):

        TESTS = [
            ("構成",         "Kousei"),
            ("好き",         "Suki"),
            ("大きい",       "Ookii"),
            ("かんたん",     "kantan"),
            ("にゃ",         "nya"),
            ("っき",         "kki"),
            ("っふぁ",       "ffa"),
            ("漢字とひらがな交じり文", "Kanzi tohiragana Maziri Bun"),
            ("Alphabet 123 and 漢字", "Alphabet 123 and Kanzi"),
            ("日経新聞", "Nikkeisinbun"),
            ("日本国民は、","Nihonkokumin ha,")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","a")
        kakasi.setMode("K","a")
        kakasi.setMode("J","a")
        kakasi.setMode("r","Kunrei")
        kakasi.setMode("C",True)
        kakasi.setMode("s",True)
        kakasi.setMode("E","a")
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)

    def test_kakasi_J2H(self):

        TESTS = [
            ("構成",         "こうせい"),
            ("好き",          "すき"),
            ("大きい",       "おおきい"),
            ("かんたん",  "かんたん"),
            ("にゃ",          "にゃ"),
            ("っき",           "っき"),
            ("っふぁ",        "っふぁ"),
            ("漢字とひらがな交じり文", "かんじ とひらがなまじり ぶん"),
            ("Alphabet 123 and 漢字", "Alphabet 123 and かんじ"),
            ("日経新聞", "にっけいしんぶん"),
            ("日本国民は、","にほんこくみん は、")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H",None)
        kakasi.setMode("K",None)
        kakasi.setMode("J","H")
        kakasi.setMode("s",True)
        kakasi.setMode("C",True)
        kakasi.setMode("E",None)
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)

    def test_wakati(self):
        TESTS = [
        ("交じり文", "交じり 文"),
        ("ひらがな交じり文", "ひらがな 交じり 文"),
        ("漢字とひらがな交じり文", "漢字 とひらがな 交じり 文")
        ]
        wakati = pykakasi.wakati()
        converter = wakati.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)
