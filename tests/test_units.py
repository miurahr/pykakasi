# -*- coding: utf-8 -*-

import pykakasi


def test_itaiji():
    I_TEST = [
        (u"菟", u"兎"),
        (u"菟集", u"兎集"),
        (u"熙", u"煕"),
        (u"壱弍", u"一二"),
        (u"森鷗外", u"森鴎外"),
    ]
    j = pykakasi.J2("H")
    for case, result in I_TEST:
        assert j.itaiji_conv(case) == result


def test_J2H():

    TESTS = [
        (u"構成", (u"こうせい", 2)),
        (u"好き", (u"すき", 2)),
        (u"大きい", (u"おおきい", 3)),
        (u"日本国民は、", (u"にほんこくみん", 4))
    ]
    j = pykakasi.J2("H")
    for case, result in TESTS:
        assert j.convert(case) == result


def test_H2a():
    TESTS = [
        (u"かんたん", ("ka", 1)),
        (u"にゃ", ("nya", 2)),
        (u"っき", ("kki", 2)),
        (u"っふぁ", ("ffa", 3)),
        (u"しつもん", ("shi", 1)),
        (u"ちがい", ("chi", 1)),
    ]
    h = pykakasi.H2("a")
    for case, result in TESTS:
        assert h.convert(case) == result


def test_H2K():
    TESTS = [
        (u"かんたん", (u"カンタン", 4)),
        (u"にゃ", (u"ニャ", 2)),
        (u"っき", (u"ッキ", 2)),
        (u"っふぁ", (u"ッファ", 3)),
        (u"しつもん", (u"シツモン", 4)),
        (u"ちがい", (u"チガイ", 3)),
    ]
    h = pykakasi.H2("K")
    for case, result in TESTS:
        assert h.convert(case) == result


def test_K2H():
    TESTS = [
        (u"カンタン", (u"かんたん", 4)),
        (u"ニャ", (u"にゃ", 2)),
        (u"ッキ", (u"っき", 2)),
        (u"ッファ", (u"っふぁ", 3)),
        (u"シツモン", (u"しつもん", 4)),
        (u"チガイ", (u"ちがい", 3)),
    ]
    h = pykakasi.K2("H")
    for case, result in TESTS:
        assert h.convert(case) == result


def test_K2a():
    TESTS = [
        (u"カンタン", ("ka", 1)),
        (u"ニャ", ("nya", 2)),
        (u"ッキ", ("kki", 2)),
        (u"ッファ", ("ffa", 3)),
        (u"シツモン", ("shi", 1)),
        (u"チガイ", ("chi", 1)),
        (u"ジ", ("ji", 1)),
    ]
    h = pykakasi.K2("a")
    for case, result in TESTS:
        assert h.convert(case) == result


def test_H2a_kunrei():
    TESTS = [
        (u"しつもん", ("si", 1)),
        (u"ちがい", ("ti", 1)),
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
    h = pykakasi.H2("a", method="Kunrei")
    for case, result in TESTS:
        assert h.convert(case) == result


def test_K2a_kunrei():
    TESTS = [
        (u"シツモン", ("si", 1)),
        (U"チガイ", ("ti", 1)),
        (u"ジ", ("zi", 1)),
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
    h = pykakasi.K2("a", method="Kunrei")
    for case, result in TESTS:
        assert h.convert(case) == result


def test_H2a_passport():
    TESTS = [
        (u"しつもん", ("shi", 1)),
        (u"ちがい", ("chi", 1)),
        (u"おおの", ("o", 2)),
        (u"さいとう", ("sa", 1)),
        (u"とう", ("to", 2)),
        (u"なんば", ("na", 1)),
        (u"んば", ("mba", 2))
    ]
    h = pykakasi.H2("a", method="Passport")
    for case, result in TESTS:
        assert h.convert(case) == result


def test_J2K():
    TESTS = [
        (u"構成", (u"コウセイ", 2)),
        (u"好き", (u"スキ", 2)),
        (u"大きい", (u"オオキイ", 3)),
        (u"日本国民は、", (u"ニホンコクミン", 4))
    ]
    j = pykakasi.J2("K")
    for case, result in TESTS:
        assert j.convert(case) == result


def test_J2a():
    TESTS = [
        (u"構成", ("kousei", 2)),
        (u"好き", ("suki", 2)),
        (u"大きい", ("ookii", 3)),
        (u"日本国民は、", ("nihonkokumin", 4)),
        (u"\u31a0", ("", 0))  # non japanese character
    ]
    j = pykakasi.J2("a")
    for case, result in TESTS:
        assert j.convert(case) == result


def test_a2E():
    TESTS = [
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", u"ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"),
        ("abcdefghijklmnopqrstuvwxyz", u"ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"),
        ("!\"#$%&'()*+,-./_ {|}~", u"！＂＃＄％＆＇（）＊＋，－．／＿　｛｜｝～")
    ]
    a = pykakasi.a2("E")
    for case, result in TESTS:
        for i in range(len(case)):
            assert a.convert(case[i]) == (result[i], 1)


def test_sym2a():
    TESTS = [
        ([u"\u3000", u"\u3001", u"\u3002", u"\u3003", u"\u3004", u"\u3006", u"\u3008",
          u"\u3009", u"\u300a", u"\u300b", u"\u300c", u"\u300d", u"\u300e", u"\u300f",
          u"\u3010", u"\u3011", u"\u3012", u"\u3013", u"\u3014", u"\u3015", u"\u3016",
          u"\u3017", u"\u3018", u"\u3019", u"\u301a", u"\u301b", u"\u301c", u"\u301d",
          u"\u301e", u"\u301f", u"\u3020",
          u"\u3030", u"\u3031", u"\u3032", u"\u3033", u"\u3034", u"\u3035", u"\u3036",
          u"\u3037",
          u"\u303c", u"\u303d", u"\u303e", u"\u303f",
          u"\u03b1", u"\u03b2", u"\u03b6", u"\u03c9", u"\u0391", u"\u0392", u"\u0396",
          u"\u03a9", u"\u03c2", u"\uff10",
          u"\u0430", u"\u044f", u"\u0451", u"\u0401"],
         [" ", ",", ".", '"', "(kigou)", "(sime)", "<", ">", "<<", ">>", "(", ")", "(", ")",
          "(", ")", "(kigou)", "(geta)", "(", ")", "(", ")", "(", ")", "(",
          ")", "~", "(kigou)", "\"", "(kigou)", "(kigou)", "-", "(kurikaesi)",
          "(kurikaesi)", "(kurikaesi)", "(kurikaesi)", "(kurikaesi)",
          "(kigou)", "XX", "(masu)", "(kurikaesi)", " ", " ", "alpha", "beta", "zeta", "omega",
          "Alpha", "Beta", "Zeta", "Omega", "final sigma",
          "0",
          "a", "ya", "e", "E"])
    ]
    s = pykakasi.sym2("a")
    for case, result in TESTS:
        for i in range(len(case)):
            assert tuple([case[i] == s.convert(case[i])]), tuple([case[i], (result[i], 1)])
