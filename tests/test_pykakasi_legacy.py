# -*- coding: utf-8 -*-
import pytest

import pykakasi


@pytest.mark.parametrize("case, expected", [
    ("", ""),
    ("構成", "Kousei"),
    ("好き", "Suki"),
    ("大きい", "Ookii"),
    ("かんたん", "kantan"),
    ("にゃ", "nya"),
    ("っき", "kki"),
    ("っふぁ", "ffa"),
    ("キャ", "kya"),
    ("キュ", "kyu"),
    ("キョ", "kyo"),
    ("漢字とひらがな交じり文", "Kanji tohiragana Majiri Bun"),
    ("Alphabet 123 and 漢字", "Alphabet 123 and Kanji"),
    ("日経新聞", "Nikkeishinbun"),
    ("日本国民は、", "Nihonkokumin ha,")
])
def test_kakasi_hepburn(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("r", "Hepburn")
    kakasi.setMode("s", True)
    kakasi.setMode("E", "a")
    kakasi.setMode("a", None)
    kakasi.setMode("C", True)
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ("", ""),
    ("構成", "Kousei"),
    ("好き", "Suki"),
    ("大きい", "Ookii"),
    ("かんたん", "kantan"),
    ("にゃ", "nya"),
    ("っき", "kki"),
    ("っふぁ", "ffa"),
    ("漢字とひらがな交じり文", "Kanzi tohiragana Maziri Bun"),
    ("Alphabet 123 and 漢字", "Alphabet 123 and Kanzi"),
    ("日経新聞", "Nikkeisinbun"),
    ("日本国民は、", "Nihonkokumin ha,")
])
def test_kakasi_kunrei(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("r", "Kunrei")
    kakasi.setMode("E", "a")
    kakasi.setMode("s", True)
    kakasi.setMode("a", None)
    kakasi.setMode("C", True)
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ("", ""),
    ("構成", "こうせい"),
    ("好き", "すき"),
    ("大きい", "おおきい"),
    ("かんたん", "かんたん"),
    ("にゃ", "にゃ"),
    ("っき", "っき"),
    ("っふぁ", "っふぁ"),
    ("漢字とひらがな交じり文", "かんじとひらがなまじりぶん"),
    ("Alphabet 123 and 漢字", "Alphabet 123 and かんじ"),
    ("日経新聞", "にっけいしんぶん"),
    ("日本国民は、", "にほんこくみんは、"),
    ("苦々しい", "にがにがしい")
])
def test_kakasi_J2H(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", None)
    kakasi.setMode("K", None)
    kakasi.setMode("J", "H")
    kakasi.setMode("s", False)
    kakasi.setMode("C", True)
    kakasi.setMode("E", None)
    kakasi.setMode("a", None)
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ("", ""),
    ("構成", "コウセイ"),
    ("好き", "スキ"),
    ("大きい", "オオキイ"),
    ("かんたん", "かんたん"),
    ("漢字とひらがな交じり文", "カンジとひらがなマジリブン"),
    ("Alphabet 123 and 漢字", "Alphabet 123 and カンジ")
])
def test_kakasi_J2K(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", None)
    kakasi.setMode("K", None)
    kakasi.setMode("J", "K")
    kakasi.setMode("s", False)
    kakasi.setMode("C", True)
    kakasi.setMode("E", None)
    kakasi.setMode("a", None)
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ("", ""),
    ("かんたん", "カンタン"),
    ("にゃ", "ニャ")
])
def test_kakasi_H2K(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "K")
    kakasi.setMode("S", " ")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ("", ""),
    ("カンタン", "かんたん"),
    ("ニャ", "にゃ")
])
def test_kakasi_K2H(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("K", "H")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ("", ""),
    ("交じり文", "交じり 文"),
    ("ひらがな交じり文", "ひらがな 交じり 文"),
    ("漢字とひらがな交じり文", "漢字 とひらがな 交じり 文")
])
def test_wakati(case, expected):
    wakati = pykakasi.wakati()
    converter = wakati.getConverter()
    assert converter.do(case) == expected


def test_katakana_furiagana():
    TESTS = [
        (u"変換前の漢字の脇に", u"変換前[ヘンカンマエ]の漢字[カンジ]の脇[ワキ]に")
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", None)
    kakasi.setMode("K", None)
    kakasi.setMode("J", "KF")
    kakasi.setMode("f", True)
    kakasi.setMode("s", False)
    kakasi.setMode("E", None)
    kakasi.setMode("a", None)
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


def test_hiragana_furiagana():
    TESTS = [
        (u"変換前の漢字の脇に", u"変換前[へんかんまえ]の漢字[かんじ]の脇[わき]に")
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", None)
    kakasi.setMode("K", None)
    kakasi.setMode("J", "HF")
    kakasi.setMode("f", True)
    kakasi.setMode("s", False)
    kakasi.setMode("E", None)
    kakasi.setMode("a", None)
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


@pytest.mark.xfail(reason="Not implemented yet furigana mode for wakati")
def test_wakati_furiagana():
    TESTS = [
        (u"変換前の漢字の脇に", u"変換前[へんかんまえ] の 漢字[かんじ] の 脇[わき] に")
    ]
    kakasi = pykakasi.wakati()
    kakasi.setMode("f", True)
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


@pytest.mark.parametrize("case, expected", [
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", u"ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"),
    ("abcdefghijklmnopqrstuvwxyz", u"ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"),
    ("!\"#$%&'()*+,-./_ {|}~", u"！＂＃＄％＆＇（）＊＋，－．／＿　｛｜｝～")
])
def test_kakasi_a2E(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("a", "E")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ("ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    ("ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ", "abcdefghijklmnopqrstuvwxyz"),
    ("！＂＃＄％＆＇（）＊＋，－．／＿　｛｜｝～\uFF1A", "!\"#$%&'()*+,-./_ {|}~:")
])
def test_kakasi_E2a(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("E", "a")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


def test_kakasi_E2a_upper():
    TESTS = [
        (u"ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("E", "a")
    kakasi.setMode("U", True)
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


def test_kakasi_J2a_upper():
    TESTS = [
        (u"かな漢字", "kana KANJI"),
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("J", "a")
    kakasi.setMode("H", "a")
    kakasi.setMode("s", True)
    kakasi.setMode("U", True)
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


def test_kakasi_numbers():

    TESTS = [
        (u"１２３４５６７８９０", "1234567890"),
        (u"一 二 三 四 五 六 七 八 九 〇", "ichi ni san shi go roku shichi hachi kyuu (maru)")
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("E", "a")
    kakasi.setMode("J", "a")
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


@pytest.mark.parametrize("case, expected", [
    ("", ""),
    ("構成", "Kosei"),
    ("大野", "Ono"),
    ("斎藤", "Saito"),
    ("菅野", "Kanno"),
    ("本田", "Honda"),
    ("一式", "Isshiki"),
    ("別府", "Beppu"),
    ("ジェ", "jie"),
    ("チェ", "chie"),
    ("ティ", "tei"),
    ("ディ", "dei"),
    ("デュ", "deyu"),
    ("ファ", "fua"),
    ("フィ", "fui"),
    ("フェ", "fue"),
    ("フォ", "fuo"),
    ("ヴァ", "bua"),
    ("ヴィ", "bui"),
    ("ヴ", "bu"),
    ("ヴェ", "bue"),
    ("ヴォ", "buo"),
    ("キャ", "kya"),
    ("キュ", "kyu"),
    ("キョ", "kyo"),
    ("じぇ", "jie"),
    ("ちぇ", "chie"),
    ("てぃ", "tei"),
    ("でぃ", "dei"),
    ("でゅ", "deyu"),
    ("ふぁ", "fua"),
    ("ふぃ", "fui"),
    ("ふぇ", "fue"),
    ("ふぉ", "fuo")
])
def test_kakasi_passport(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("r", "Passport")
    kakasi.setMode("E", "a")
    kakasi.setMode("C", True)
    kakasi.setMode("a", None)
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ("えっちゅう", "etchu"),
    ("はっちょう", "hatcho"),
    ("エッチュウ", "etchu"),
    ("ハッチョウ", "hatcho")
])
def test_kakasi_passport_specialcase(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("r", "Passport")
    kakasi.setMode("E", "a")
    kakasi.setMode("a", None)
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ("", ""),
    ("構成", "kousei"),
    ("好き", "suki"),
    ("大きい", "ookii"),
    ("かんたん", "kantan"),
    ("にゃ", "nya"),
    ("っき", "kki"),
    ("っふぁ", "ffa"),
    ("漢字とひらがな交じり文", "kanji tohiragana majiri bun"),
    ("Alphabet 123 and 漢字", "Alphabet 123 and kanji"),
    ("日経新聞", "nikkeishinbun"),
    ("日本国民は、", "nihonkokumin ha,")
])
def test_kakasi_hepburn_nocapital(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("r", "Hepburn")
    kakasi.setMode("s", True)
    kakasi.setMode("E", "a")
    kakasi.setMode("a", None)
    kakasi.setMode("C", False)
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ("\U0001b150", "wi"),
    ("\U0001b151", "we")
])
def test_kakasi_extended_kana(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("r", "Hepburn")
    kakasi.setMode("s", True)
    kakasi.setMode("E", "a")
    kakasi.setMode("a", None)
    kakasi.setMode("C", False)
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


def test_kakasi_chinese_kanji():
    TESTS = [
        (u"您好", u'您 kou')
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("s", True)
    kakasi.setMode("E", "a")
    kakasi.setMode("a", None)
    kakasi.setMode("C", False)
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


def test_kakasi_chinese_kanji_replace():
    TESTS = [
        (u"您好", u'??? kou')
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("s", True)
    kakasi.setMode("E", "a")
    kakasi.setMode("a", None)
    kakasi.setMode("C", False)
    kakasi.setMode("t", False)
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


@pytest.mark.parametrize("case, expected", [
    ('やったー', 'yattaa'),
    ('でっでー', 'deddee'),
    ('てんさーふろー', 'tensaafuroo'),
    ('がっがーん', 'gaggaan'),
    ('どーん', 'doon')
])
def test_kakasi_long_symbol_H(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode('H', 'a')
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    (u'ヤッター', u'yattaa'),
    (u'デッデー', u'deddee'),
    (u'テンサーフロー', u'tensaafuroo'),
    (u'ガッガーン', u'gaggaan'),
    (u'ドーン', u'doon')
])
def test_kakasi_long_symbol_K(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode('K', 'a')
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ('じゃーんデデーン', 'jaandedeen'),
    ('デッデーンじゃーん', 'deddeenjaan'),
    ('テンサーふろー', 'tensaafuroo'),
    ('ガッガーン', 'gaggaan'),
    ('ドーン', 'doon')
])
def test_kakasi_long_symbol_mixed_HK(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode('K', 'a')
    kakasi.setMode('H', 'a')
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [
    ('順じゃーんデデーン', 'junjaandedeen'),
    ('デッデーン順じゃーん', 'deddeenjunjaan'),
    ('テンサーふろー風呂', 'tensaafuroofuro'),
    ('ガッガーン癌', 'gaggaangan'),
    ('ドーン', 'doon')
])
def test_kakasi_long_symbol_mixed_JHK(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode('K', 'a')
    kakasi.setMode('H', 'a')
    kakasi.setMode('J', 'a')
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


def test_kakasi_long_symbol_with_no_HK():
    TESTS = [
        (u'順ーデデーン', u'jun-dedeen'),
        (u'デッデーン順ー', u'deddeenjun-')
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode('K', 'a')
    kakasi.setMode('H', 'a')
    kakasi.setMode('J', 'a')
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result
