# -*- coding: utf-8 -*-
import pytest

import pykakasi


@pytest.mark.parametrize(
    "case, expected",
    [
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
        ("日本国民は、", "Nihonkokumin ha,"),
    ],
)
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


@pytest.mark.parametrize(
    "case, expected",
    [
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
        ("日本国民は、", "Nihonkokumin ha,"),
    ],
)
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


@pytest.mark.parametrize(
    "case, expected",
    [
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
        ("苦々しい", "にがにがしい"),
    ],
)
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


@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("構成", "コウセイ"),
        ("好き", "スキ"),
        ("大きい", "オオキイ"),
        ("かんたん", "かんたん"),
        ("漢字とひらがな交じり文", "カンジとひらがなマジリブン"),
        ("Alphabet 123 and 漢字", "Alphabet 123 and カンジ"),
    ],
)
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


@pytest.mark.parametrize("case, expected", [("", ""), ("かんたん", "カンタン"), ("にゃ", "ニャ")])
def test_kakasi_H2K(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "K")
    kakasi.setMode("S", " ")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize("case, expected", [("", ""), ("カンタン", "かんたん"), ("ニャ", "にゃ")])
def test_kakasi_K2H(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("K", "H")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("交じり文", "交じり 文"),
        ("ひらがな交じり文", "ひらがな 交じり 文"),
        ("漢字とひらがな交じり文", "漢字 とひらがな 交じり 文"),
    ],
)
def test_wakati(case, expected):
    wakati = pykakasi.wakati()
    converter = wakati.getConverter()
    assert converter.do(case) == expected


def test_katakana_furiagana():
    TESTS = [(u"変換前の漢字の脇に", u"変換前[ヘンカンマエ]の漢字[カンジ]の脇[ワキ]に")]
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
    TESTS = [(u"変換前の漢字の脇に", u"変換前[へんかんまえ]の漢字[かんじ]の脇[わき]に")]
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
    TESTS = [(u"変換前の漢字の脇に", u"変換前[へんかんまえ] の 漢字[かんじ] の 脇[わき] に")]
    kakasi = pykakasi.wakati()
    kakasi.setMode("f", True)
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


@pytest.mark.parametrize(
    "case, expected",
    [
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", u"ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"),
        ("abcdefghijklmnopqrstuvwxyz", u"ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"),
        ("!\"#$%&'()*+,-./_ {|}~", u"！＂＃＄％＆＇（）＊＋，－．／＿　｛｜｝～"),
    ],
)
def test_kakasi_a2E(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("a", "E")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        ("ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ", "abcdefghijklmnopqrstuvwxyz"),
        ("！＂＃＄％＆＇（）＊＋，－．／＿　｛｜｝～\uFF1A", "!\"#$%&'()*+,-./_ {|}~:"),
    ],
)
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
        (u"一 二 三 四 五 六 七 八 九 〇", "ichi ni san shi go roku shichi hachi kyuu (maru)"),
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("E", "a")
    kakasi.setMode("J", "a")
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


@pytest.mark.parametrize(
    "case, expected",
    [
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
        ("ふぉ", "fuo"),
    ],
)
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


@pytest.mark.parametrize(
    "case, expected",
    [("えっちゅう", "etchu"), ("はっちょう", "hatcho"), ("エッチュウ", "etchu"), ("ハッチョウ", "hatcho")],
)
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


@pytest.mark.parametrize(
    "case, expected",
    [
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
        ("日本国民は、", "nihonkokumin ha,"),
    ],
)
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


@pytest.mark.parametrize("case, expected", [("\U0001b150", "wi"), ("\U0001b151", "we")])
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
    TESTS = [(u"您好", u"您 kou")]
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
    TESTS = [(u"您好", u"??? kou")]
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


@pytest.mark.parametrize(
    "case, expected",
    [
        ("やったー", "yattaa"),
        ("でっでー", "deddee"),
        ("てんさーふろー", "tensaafuroo"),
        ("がっがーん", "gaggaan"),
        ("どーん", "doon"),
    ],
)
def test_kakasi_long_symbol_H(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        (u"ヤッター", u"yattaa"),
        (u"デッデー", u"deddee"),
        (u"テンサーフロー", u"tensaafuroo"),
        (u"ガッガーン", u"gaggaan"),
        (u"ドーン", u"doon"),
    ],
)
def test_kakasi_long_symbol_K(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("K", "a")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("じゃーんデデーン", "jaandedeen"),
        ("デッデーンじゃーん", "deddeenjaan"),
        ("テンサーふろー", "tensaafuroo"),
        ("ガッガーン", "gaggaan"),
        ("ドーン", "doon"),
    ],
)
def test_kakasi_long_symbol_mixed_HK(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("K", "a")
    kakasi.setMode("H", "a")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("順じゃーんデデーン", "junjaandedeen"),
        ("デッデーン順じゃーん", "deddeenjunjaan"),
        ("テンサーふろー風呂", "tensaafuroofuro"),
        ("ガッガーン癌", "gaggaangan"),
        ("ドーン", "doon"),
    ],
)
def test_kakasi_long_symbol_mixed_JHK(case, expected):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("K", "a")
    kakasi.setMode("H", "a")
    kakasi.setMode("J", "a")
    converter = kakasi.getConverter()
    assert converter.do(case) == expected


def test_kakasi_long_symbol_with_no_HK():
    TESTS = [(u"順ーデデーン", u"jun-dedeen"), (u"デッデーン順ー", u"deddeenjun-")]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("K", "a")
    kakasi.setMode("H", "a")
    kakasi.setMode("J", "a")
    converter = kakasi.getConverter()
    for case, result in TESTS:
        assert converter.do(case) == result


def test_kakasi_legacy_constitution():

    original_text = (
        u"日本国民は、正当に選挙された国会における代表者を通じて行動し、われらとわれらの子孫のために、"
        u"諸国民との協和による成果と、わが国全土にわたつて自由のもたらす恵沢を確保し、"
        u"政府の行為によつて再び戦争の惨禍が起ることのないやうにすることを決意し、ここに主権が国民に存することを宣言し、"
        u"この憲法を確定する。そもそも国政は、国民の厳粛な信託によるものであつて、その権威は国民に由来し、"
        u"その権力は国民の代表者がこれを行使し、その福利は国民がこれを享受する。これは人類普遍の原理であり、"
        u"この憲法は、かかる原理に基くものである。われらは、これに反する一切の憲法、法令及び詔勅を排除する。"
    )
    result = (
        "Nihonkokumin ha, Seitou ni Senkyo sareta Kokkai niokeru Daihyousha wo Tsuuji te Koudou shi, "
        "wareratowarerano Shison notameni, Shokokumin tono Kyouwa niyoru Seika to, waga Kuni Zendo "
        "niwatatsute Jiyuu nomotarasu Keitaku wo Kakuho shi,"
        " Seifu no Koui niyotsute Futatabi Sensou no Sanka ga Okoru kotononaiyaunisurukotowo Ketsui shi, "
        "kokoni Shuken ga Kokumin ni Sonsu rukotowo Sengen shi, kono Kenpou wo Kakuteisu ru. "
        "somosomo Kokusei ha, Kokumin no Genshuku na Shintaku niyorumonodeatsute, sono Ken'i ha Kokumin ni "
        "Yurai shi, sono Kenryoku ha Kokumin no Daihyousha gakorewo Koushi shi, sono Fukuri ha Kokumin "
        "gakorewo Kyouju suru. koreha Jinruifuhen no Genri deari, kono Kenpou ha, kakaru Genri ni Motozuku "
        "monodearu. wareraha, koreni Hansu ru Issai no Kenpou, Hourei Oyobi Shouchoku wo Haijo suru."
    )

    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("E", "a")
    kakasi.setMode("r", "Hepburn")
    kakasi.setMode("C", True)
    kakasi.setMode("s", True)
    converter = kakasi.getConverter()
    assert converter.do(original_text) == result


def test_wakati_constitution():

    original_text = (
        u"日本国民は、正当に選挙された国会における代表者を通じて行動し、われらとわれらの子孫のために、"
        u"諸国民との協和による成果と、わが国全土にわたつて自由のもたらす恵沢を確保し、"
        u"政府の行為によつて再び戦争の惨禍が起ることのないやうにすることを決意し、ここに主権が国民に存することを宣言し、"
        u"この憲法を確定する。そもそも国政は、国民の厳粛な信託によるものであつて、その権威は国民に由来し、"
        u"その権力は国民の代表者がこれを行使し、その福利は国民がこれを享受する。これは人類普遍の原理であり、"
        u"この憲法は、かかる原理に基くものである。われらは、これに反する一切の憲法、法令及び詔勅を排除する。"
    )
    result = (
        u"日本国民 は、 正当 に 選挙 された 国会 における 代表者 を 通じ て 行動 し、われらとわれらの 子孫 のために、 "
        u"諸国民 との 協和 による 成果 と、わが 国 全土 にわたつて 自由 のもたらす 恵沢 を 確保 し、 政府 の 行為 によつて 再び 戦争 "
        u"の 惨禍 が 起る ことのないやうにすることを 決意 し、ここに 主権 が 国民 に 存す ることを "
        u"宣言 し、この 憲法 を 確定す る。そもそも 国政 は、 国民 の 厳粛 な 信託 によるものであつて、"
        u"その 権威 は 国民 に 由来 し、その 権力 は 国民 の 代表者 がこれを 行使 し、その 福利 は 国民 "
        u"がこれを 享受 する。これは 人類普遍 の 原理 であり、この 憲法 は、かかる 原理 に 基く ものである。われらは、"
        u"これに 反す る 一切 の 憲法 、 法令 及び 詔勅 を 排除 する。"
    )

    wakati = pykakasi.wakati()
    converter = wakati.getConverter()
    assert converter.do(original_text) == result


def test_issues60():
    TESTS = [(u"市立", u"しりつ")]
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
    TESTS = [(u"じゃーん", u"じゃーん"), (u"ヷヸヹヺ", u"ヷヸヹヺ")]
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


def test_issue66():
    TESTS = [
        (u"月々", "tukizuki"),
        (u"毎月々", "maitukizuki"),
        (u"佐々木", "sasaki"),
        (u"中佐々木", "nakasasaki"),
        (u"代々木", "yoyogi"),
        (u"次代々木", "tugiyoyogi"),
    ]
    kakasi = pykakasi.kakasi()
    kakasi.setMode("J", "a")
    kakasi.setMode("r", "Kunrei")
    conv = kakasi.getConverter()
    for case, result in TESTS:
        assert conv.do(case) == result


def test_issues68():
    TESTS = [(u"", u""), (u"埇", u"よう")]
    kks = pykakasi.kakasi()
    kks.setMode("J", "H")
    convert = kks.getConverter()
    for case, result in TESTS:
        assert convert.do(case) == result


def test_issue68_2():
    kks = pykakasi.kakasi()
    kks.setMode("J", "H")
    convert = kks.getConverter()
    for case in range(0x3400, 0xDFFF):
        assert convert.do(chr(case)) is not None
    for case in range(0xF900, 0xFA2E):
        assert convert.do(chr(case)) is not None


def test_issue72():
    TESTS = [(u"㐂", u"き")]
    kks = pykakasi.kakasi()
    kks.setMode("J", "H")
    convert = kks.getConverter()
    for case, result in TESTS:
        assert convert.do(case) == result


def test_issue78():
    TESTS = [
        (u"由来し、この", u"ゆらい し、 この"),
        (u"これは人類普遍であり、かかる原理に", u"これは じんるいふへん であり、 かかる げんり に"),
    ]
    kks = pykakasi.kakasi()
    kks.setMode("J", "H")
    kks.setMode("s", True)
    convert = kks.getConverter()
    for case, result in TESTS:
        assert convert.do(case) == result


def test_issue90_legacy():
    TESTS = [(u"私がこの子を助けなきゃいけないってことだよね", u"ワタシガコノコヲタスケナキャイケナイッテコトダヨネ")]
    kks = pykakasi.kakasi()
    kks.setMode("J", "K")
    kks.setMode("H", "K")
    convert = kks.getConverter()
    for case, result in TESTS:
        assert convert.do(case) == result


def test_issue105_legacy():
    text = "ｿｳｿﾞｸﾆﾝ"
    kks = pykakasi.kakasi()
    kks.setMode("K", "H")
    converter = kks.getConverter()
    result = converter.do(text)
    assert result == "そうぞくにん"


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


@pytest.mark.parametrize(
    "case, expected",
    [
        ("構成", ("kousei", 2)),
        ("好き", ("suki", 2)),
        ("大きい", ("ookii", 3)),
        ("日本国民は、", ("nihonkokumin", 4)),
        ("\u31a0", ("", 0)),  # non japanese character
    ],
)
def test_J2a(case, expected):
    j = pykakasi.legacy.J2("a")
    assert j.convert(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("構成", (u"コウセイ", 2)),
        ("好き", (u"スキ", 2)),
        ("大きい", (u"オオキイ", 3)),
        ("日本国民は、", (u"ニホンコクミン", 4)),
    ],
)
def test_J2K(case, expected):
    j = pykakasi.legacy.J2("K")
    assert j.convert(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("菟", "兎"),
        ("菟集", "兎集"),
        ("熙", "煕"),
        ("壱弍", "一二"),
        ("森鷗外", "森鴎外"),
        ("神", "神"),
        ("\U0000FA30", "\U00004FAE"),
        ("\U0000845B\U000E0101城市", "葛城市"),
        ("\U0000845B\U000E0100飾区", "葛飾区"),
        ("高橋祥", "高橋祥"),
    ],
)
def test_itaiji(case, expected):
    j = pykakasi.legacy.J2("H")
    assert j._itaiji.convert(case) == expected


@pytest.mark.parametrize(
    "case, expected",
    [
        ("構成", ("こうせい", 2)),
        ("好き", ("すき", 2)),
        ("大きい", ("おおきい", 3)),
        ("日本国民は、", ("にほんこくみん", 4)),
        ("\U0000845B\U000E0101城市", ("かつらぎ", 3)),
        ("\U0000845B\U000E0100飾区", ("かつしかく", 4)),
    ],
)
def test_J2H(case, expected):
    j = pykakasi.legacy.J2("H")
    assert j.convert(case) == expected
