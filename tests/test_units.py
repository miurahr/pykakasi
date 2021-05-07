# -*- coding: utf-8 -*-

import pytest

import pykakasi
import pykakasi.scripts


@pytest.mark.parametrize(
    "case, expected",
    [
        ("かんたん", ("ka", 1)),
        ("にゃ", ("nya", 2)),
        ("っき", ("kki", 2)),
        ("っふぁ", ("ffa", 3)),
        ("しつもん", ("shi", 1)),
        ("ちがい", ("chi", 1)),
    ],
)
def test_H2a(case, expected):
    h = pykakasi.scripts.H2("a")
    assert h.convert(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("かんたん", ("カンタン", 4)),
        ("にゃ", ("ニャ", 2)),
        ("っき", ("ッキ", 2)),
        ("っふぁ", ("ッファ", 3)),
        ("しつもん", ("シツモン", 4)),
        ("ちがい", ("チガイ", 3)),
    ],
)
def test_H2K(case, expected):
    h = pykakasi.scripts.H2("K")
    assert h.convert(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("カンタン", ("かんたん", 4)),
        ("ニャ", ("にゃ", 2)),
        ("ッキ", ("っき", 2)),
        ("ッファ", ("っふぁ", 3)),
        ("シツモン", ("しつもん", 4)),
        ("チガイ", ("ちがい", 3)),
    ],
)
def test_K2H(case, expected):
    h = pykakasi.scripts.K2("H")
    assert h.convert(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("カンタン", ("ka", 1)),
        ("ニャ", ("nya", 2)),
        ("ッキ", ("kki", 2)),
        ("ッファ", ("ffa", 3)),
        ("シツモン", ("shi", 1)),
        ("チガイ", ("chi", 1)),
        ("ジ", ("ji", 1)),
    ],
)
def test_K2a(case, expected):
    h = pykakasi.scripts.K2("a")
    assert h.convert(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("しつもん", ("si", 1)),
        ("ちがい", ("ti", 1)),
        ("きゃ", ("kya", 2)),
        ("きゅ", ("kyu", 2)),
        ("きょ", ("kyo", 2)),
        ("しゃ", ("sya", 2)),
        ("しゅ", ("syu", 2)),
        ("しょ", ("syo", 2)),
        ("ちゃ", ("tya", 2)),
        ("ちゅ", ("tyu", 2)),
        ("ちょ", ("tyo", 2)),
        ("にゃ", ("nya", 2)),
        ("にゅ", ("nyu", 2)),
        ("にょ", ("nyo", 2)),
        ("りゃ", ("rya", 2)),
        ("りゅ", ("ryu", 2)),
        ("りょ", ("ryo", 2)),
        ("ざ", ("za", 1)),
        ("じ", ("zi", 1)),
        ("ず", ("zu", 1)),
        ("ぜ", ("ze", 1)),
        ("ぞ", ("zo", 1)),
        ("だ", ("da", 1)),
        ("ぢ", ("zi", 1)),
        ("づ", ("zu", 1)),
        ("で", ("de", 1)),
        ("ど", ("do", 1)),
        ("た", ("ta", 1)),
        ("ち", ("ti", 1)),
        ("つ", ("tu", 1)),
        ("て", ("te", 1)),
        ("と", ("to", 1)),
    ],
)
def test_H2a_kunrei(case, expected):
    h = pykakasi.scripts.H2("a", method="Kunrei")
    assert h.convert(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("シツモン", ("si", 1)),
        ("チガイ", ("ti", 1)),
        ("ジ", ("zi", 1)),
        ("ファジー", ("fa", 2)),
        ("ジー", ("zi", 1)),
        ("ウォークマン", ("u", 1)),
        ("キャ", ("kya", 2)),
        ("キュ", ("kyu", 2)),
        ("キョ", ("kyo", 2)),
        ("シャ", ("sya", 2)),
        ("シュ", ("syu", 2)),
        ("ショ", ("syo", 2)),
        ("チャ", ("tya", 2)),
        ("チュ", ("tyu", 2)),
        ("チョ", ("tyo", 2)),
        ("ニャ", ("nya", 2)),
        ("ニュ", ("nyu", 2)),
        ("ニョ", ("nyo", 2)),
        ("リャ", ("rya", 2)),
        ("リュ", ("ryu", 2)),
        ("リョ", ("ryo", 2)),
        ("ザ", ("za", 1)),
        ("ジ", ("zi", 1)),
        ("ズ", ("zu", 1)),
        ("ゼ", ("ze", 1)),
        ("ゾ", ("zo", 1)),
        ("ダ", ("da", 1)),
        ("ヂ", ("zi", 1)),
        ("ヅ", ("zu", 1)),
        ("デ", ("de", 1)),
        ("ド", ("do", 1)),
        ("タ", ("ta", 1)),
        ("チ", ("ti", 1)),
        ("ツ", ("tu", 1)),
        ("テ", ("te", 1)),
        ("ト", ("to", 1)),
    ],
)
def test_K2a_kunrei(case, expected):
    h = pykakasi.scripts.K2("a", method="Kunrei")
    assert h.convert(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("しつもん", ("shi", 1)),
        ("ちがい", ("chi", 1)),
        ("おおの", ("o", 2)),
        ("さいとう", ("sa", 1)),
        ("とう", ("to", 2)),
        ("なんば", ("na", 1)),
        ("んば", ("mba", 2)),
    ],
)
def test_H2a_passport(case, expected):
    h = pykakasi.scripts.H2("a", method="Passport")
    assert h.convert(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", u"ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"),
        ("abcdefghijklmnopqrstuvwxyz", u"ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"),
        ("!\"#$%&'()*+,-./_ {|}~", u"！＂＃＄％＆＇（）＊＋，－．／＿　｛｜｝～"),
    ],
)
def test_a2E(case, expected):
    a = pykakasi.scripts.A2("E")
    for i in range(len(case)):
        assert a.convert(case[i]) == (expected[i], 1)


@pytest.mark.parametrize(
    "case, expected",
    [
        ("\u3000", " "),
        ("\u3001", ","),
        ("\u3002", "."),
        ("\u3003", '"'),
        ("\u3004", "(kigou)"),
        ("\u3006", "(sime)"),
        ("\u3008", "<"),
        ("\u3009", ">"),
        ("\u300a", "<<"),
        ("\u300b", ">>"),
        ("\u300c", "("),
        ("\u300d", ")"),
        ("\u300e", "("),
        ("\u300f", ")"),
        ("\u3010", "("),
        ("\u3011", ")"),
        ("\u3012", "(kigou)"),
        ("\u3013", "(geta)"),
        ("\u3014", "("),
        ("\u3015", ")"),
        ("\u3016", "("),
        ("\u3017", ")"),
        ("\u3018", "("),
        ("\u3019", ")"),
        ("\u301a", "("),
        ("\u301b", ")"),
        ("\u301c", "~"),
        ("\u301d", "(kigou)"),
        ("\u301e", '"'),
        ("\u301f", "(kigou)"),
        ("\u3020", "(kigou)"),
        ("\u3030", "-"),
        ("\u3031", "(kurikaesi)"),
        ("\u3032", "(kurikaesi)"),
        ("\u3033", "(kurikaesi)"),
        ("\u3034", "(kurikaesi)"),
        ("\u3035", "(kurikaesi)"),
        ("\u3036", "(kigou)"),
        ("\u3037", "XX"),
        ("\u303c", "(masu)"),
        ("\u303d", "(kurikaesi)"),
        ("\u303e", " "),
        ("\u303f", " "),
        ("\u03b1", "alpha"),
        ("\u03b2", "beta"),
        ("\u03b6", "zeta"),
        ("\u03c9", "omega"),
        ("\u0391", "Alpha"),
        ("\u0392", "Beta"),
        ("\u0396", "Zeta"),
        ("\u03a9", "Omega"),
        ("\u03c2", "final sigma"),
        ("\uff10", "0"),
        ("\u0430", "a"),
        ("\u044f", "ya"),
        ("\u0451", "e"),
        ("\u0401", "E"),
    ],
)
def test_sym2a(case, expected):
    s = pykakasi.scripts.Sym2("a")
    assert s.convert(case) == (expected, 1)


def test_extended_kana_unit():
    s = pykakasi.scripts.K2("a")
    assert s.convert("\U0001b164") == ("wi", 1)


def test_extended_kana_hira():
    s = pykakasi.scripts.K2("H")
    assert s.convert("\U0001b167") == ("ん", 1)
