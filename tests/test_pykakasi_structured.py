# -*- coding: utf-8 -*-
import pytest

import pykakasi


@pytest.mark.parametrize(
    "case, expected",
    [
        (
            "",
            [
                {
                    "orig": "",
                    "hira": "",
                    "kana": "",
                    "kunrei": "",
                    "hepburn": "",
                    "passport": "",
                }
            ],
        ),
        (
            "構成",
            [
                {
                    "orig": "構成",
                    "kana": "コウセイ",
                    "hira": "こうせい",
                    "hepburn": "kousei",
                    "kunrei": "kousei",
                    "passport": "kosei",
                }
            ],
        ),
        (
            "好き",
            [
                {
                    "orig": "好き",
                    "hira": "すき",
                    "kana": "スキ",
                    "hepburn": "suki",
                    "kunrei": "suki",
                    "passport": "suki",
                }
            ],
        ),
        (
            "大きい",
            [
                {
                    "orig": "大きい",
                    "hira": "おおきい",
                    "kana": "オオキイ",
                    "hepburn": "ookii",
                    "kunrei": "ookii",
                    "passport": "okii",
                }
            ],
        ),
        (
            "かんたん",
            [
                {
                    "orig": "かんたん",
                    "hira": "かんたん",
                    "kana": "カンタン",
                    "hepburn": "kantan",
                    "kunrei": "kantan",
                    "passport": "kantan",
                }
            ],
        ),
        (
            "にゃ",
            [
                {
                    "orig": "にゃ",
                    "hira": "にゃ",
                    "kana": "ニャ",
                    "hepburn": "nya",
                    "kunrei": "nya",
                    "passport": "nya",
                }
            ],
        ),
        (
            "っき",
            [
                {
                    "orig": "っき",
                    "hira": "っき",
                    "kana": "ッキ",
                    "hepburn": "kki",
                    "kunrei": "kki",
                    "passport": "kki",
                }
            ],
        ),
        (
            "っふぁ",
            [
                {
                    "orig": "っふぁ",
                    "hira": "っふぁ",
                    "kana": "ッファ",
                    "hepburn": "ffa",
                    "kunrei": "ffa",
                    "passport": "ffa",
                }
            ],
        ),
        (
            "キャ",
            [
                {
                    "orig": "キャ",
                    "hira": "きゃ",
                    "kana": "キャ",
                    "hepburn": "kya",
                    "kunrei": "kya",
                    "passport": "kya",
                }
            ],
        ),
        (
            "キュ",
            [
                {
                    "orig": "キュ",
                    "hira": "きゅ",
                    "kana": "キュ",
                    "hepburn": "kyu",
                    "kunrei": "kyu",
                    "passport": "kyu",
                }
            ],
        ),
        (
            "キョ",
            [
                {
                    "orig": "キョ",
                    "hira": "きょ",
                    "kana": "キョ",
                    "hepburn": "kyo",
                    "kunrei": "kyo",
                    "passport": "kyo",
                }
            ],
        ),
        (
            "漢字とひらがな交じり文",
            [
                {
                    "orig": "漢字",
                    "hira": "かんじ",
                    "kana": "カンジ",
                    "hepburn": "kanji",
                    "kunrei": "kanzi",
                    "passport": "kanji",
                },
                {
                    "orig": "とひらがな",
                    "hira": "とひらがな",
                    "kana": "トヒラガナ",
                    "hepburn": "tohiragana",
                    "kunrei": "tohiragana",
                    "passport": "tohiragana",
                },
                {
                    "orig": "交じり",
                    "hira": "まじり",
                    "kana": "マジリ",
                    "hepburn": "majiri",
                    "kunrei": "maziri",
                    "passport": "majiri",
                },
                {
                    "orig": "文",
                    "hira": "ぶん",
                    "kana": "ブン",
                    "hepburn": "bun",
                    "kunrei": "bun",
                    "passport": "bun",
                },
            ],
        ),
        (
            "Alphabet 123 and 漢字",
            [
                {
                    "orig": "Alphabet 123 and ",
                    "hira": "Alphabet 123 and ",
                    "kana": "Alphabet 123 and ",
                    "hepburn": "Alphabet 123 and ",
                    "kunrei": "Alphabet 123 and ",
                    "passport": "Alphabet 123 and ",
                },
                {
                    "orig": "漢字",
                    "hira": "かんじ",
                    "kana": "カンジ",
                    "hepburn": "kanji",
                    "kunrei": "kanzi",
                    "passport": "kanji",
                },
            ],
        ),
        (
            "日経新聞",
            [
                {
                    "orig": "日経新聞",
                    "hira": "にっけいしんぶん",
                    "kana": "ニッケイシンブン",
                    "hepburn": "nikkeishinbun",
                    "kunrei": "nikkeisinbun",
                    "passport": "nikkeishimbun",
                }
            ],
        ),
        (
            "日本国民は、",
            [
                {
                    "orig": "日本国民",
                    "hira": "にほんこくみん",
                    "kana": "ニホンコクミン",
                    "hepburn": "nihonkokumin",
                    "kunrei": "nihonkokumin",
                    "passport": "nihonkokumin",
                },
                {
                    "orig": "は",
                    "hira": "は",
                    "kana": "ハ",
                    "hepburn": "ha",
                    "kunrei": "ha",
                    "passport": "ha",
                },
                {
                    "orig": "、",
                    "kana": "、",
                    "hira": "、",
                    "hepburn": ",",
                    "kunrei": ",",
                    "passport": ",",
                },

            ],
        ),
        (
            "私がこの子を助けなきゃいけないってことだよね",
            [
                {
                    "orig": "私",
                    "kana": "ワタシ",
                    "hira": "わたし",
                    "hepburn": "watashi",
                    "kunrei": "watasi",
                    "passport": "watashi",
                },
                {
                    "orig": "がこの",
                    "kana": "ガコノ",
                    "hira": "がこの",
                    "hepburn": "gakono",
                    "kunrei": "gakono",
                    "passport": "gakono",
                },
                {
                    "orig": "子",
                    "kana": "コ",
                    "hira": "こ",
                    "hepburn": "ko",
                    "kunrei": "ko",
                    "passport": "ko",
                },
                {
                    "orig": "を",
                    "kana": "ヲ",
                    "hira": "を",
                    "hepburn": "wo",
                    "kunrei": "wo",
                    "passport": "wo",
                },
                {
                    "orig": "助け",
                    "kana": "タスケ",
                    "hira": "たすけ",
                    "hepburn": "tasuke",
                    "kunrei": "tasuke",
                    "passport": "tasuke",
                },
                {
                    "orig": "なきゃいけないってことだよね",
                    "kana": "ナキャイケナイッテコトダヨネ",
                    "hira": "なきゃいけないってことだよね",
                    "hepburn": "nakyaikenaittekotodayone",
                    "kunrei": "nakyaikenaittekotodayone",
                    "passport": "nakyaikenaittekotodayone",
                },
            ],
        ),
        (
            "やったー",
            [
                {
                    "orig": "やったー",
                    "kana": "ヤッター",
                    "hira": "やったー",
                    "hepburn": "yattaa",
                    "kunrei": "yattaa",
                    "passport": "yattaa",
                }
            ],
        ),
        (
            "でっでー",
            [
                {
                    "orig": "でっでー",
                    "kana": "デッデー",
                    "hira": "でっでー",
                    "hepburn": "deddee",
                    "kunrei": "deddee",
                    "passport": "deddee",
                }
            ],
        ),
        (
            "てんさーふろー",
            [
                {
                    "orig": "てんさーふろー",
                    "kana": "テンサーフロー",
                    "hira": "てんさーふろー",
                    "hepburn": "tensaafuroo",
                    "kunrei": "tensaafuroo",
                    "passport": "tensaafuroo",
                }
            ],
        ),
        (
            "オレンジ色",
            [
                {
                    "orig": "オレンジ",
                    "kana": "オレンジ",
                    "hira": "おれんじ",
                    "hepburn": "orenji",
                    "kunrei": "orenzi",
                    "passport": "orenji",
                },
                {
                    "orig": "色",
                    "kana": "イロ",
                    "hira": "いろ",
                    "hepburn": "iro",
                    "kunrei": "iro",
                    "passport": "iro",
                },
            ],
        ),
        (
            "檸檬は、レモン色",
            [
                {
                    "orig": "檸檬",
                    "hira": "れもん",
                    "kana": "レモン",
                    "hepburn": "remon",
                    "kunrei": "remon",
                    "passport": "remon",
                },
                {
                    "orig": "は",
                    "hira": "は",
                    "kana": "ハ",
                    "hepburn": "ha",
                    "kunrei": "ha",
                    "passport": "ha",
                },
                {
                    "orig": "、",
                    "kana": "、",
                    "hira": "、",
                    "hepburn": ",",
                    "kunrei": ",",
                    "passport": ",",
                },
                {
                    "orig": "レモン",
                    "kana": "レモン",
                    "hira": "れもん",
                    "hepburn": "remon",
                    "kunrei": "remon",
                    "passport": "remon",
                },
                {
                    "orig": "色",
                    "kana": "イロ",
                    "hira": "いろ",
                    "hepburn": "iro",
                    "kunrei": "iro",
                    "passport": "iro",
                },
            ],
        ),
    ],
)
def test_kakasi_structured(case, expected):
    kakasi = pykakasi.kakasi()
    result = kakasi.convert(case)
    if len(result) >= len(expected):
        for i, r in enumerate(result):
            assert r["orig"] == expected[i]["orig"]
            assert r["hira"] == expected[i]["hira"]
            assert r["kana"] == expected[i]["kana"]
            assert r["hepburn"] == expected[i]["hepburn"]
            assert r["kunrei"] == expected[i]["kunrei"]
            assert r["passport"] == expected[i]["passport"]
    else:
        for i, e in enumerate(expected):
            assert result[i]["orig"] == e["orig"]
            assert result[i]["hira"] == e["hira"]
            assert result[i]["kana"] == e["kana"]
            assert result[i]["hepburn"] == e["hepburn"]
            assert result[i]["kunrei"] == e["kunrei"]
            assert result[i]["passport"] == e["passport"]


def test_issue90():
    text = "私がこの子を助けなきゃいけないってことだよね"
    expected = ["ワタシ", "ガコノ", "コ", "ヲ", "タスケ", "ナキャイケナイッテコトダヨネ"]
    kks = pykakasi.kakasi()
    result = kks.convert(text)
    for i in range(len(expected)):
        assert result[i]["kana"] == expected[i]


def test_issue105():
    text = "ｿｳｿﾞｸﾆﾝ"
    kks = pykakasi.kakasi()
    result = kks.convert(text)
    assert result[0]["kana"] == "ｿｳｿﾞｸﾆﾝ"
    assert result[0]["hepburn"] == "souzokunin"
    assert result[0]["hira"] == "そうぞくにん"


def test_issue114():
    text = "思った 言った 行った"
    kks = pykakasi.kakasi()
    result = kks.convert(text)
    assert result[0]["hepburn"] == "omotta"
    assert result[2]["hepburn"] == "itta"
    assert result[4]["hepburn"] == "itta"


def test_issue115():
    kks = pykakasi.kakasi()
    result = kks.convert("ﾞっ、")  # \uFF9E
    expected = [
        {"hira": "\u309B", "kana": "\uFF9E", "hepburn": '"'},
        {"hira": "っ", "kana": "ッ", "hepburn": "tsu"},
        {"hira": "、", "kana": "、", "hepburn": ","},
    ]
    for i in range(len(expected)):
        assert result[i]["hira"] == expected[i]["hira"]
        assert result[i]["kana"] == expected[i]["kana"]
        assert result[i]["hepburn"] == expected[i]["hepburn"]


@pytest.mark.parametrize("case, expected", [("藍之介", "あいのすけ"), ("藍水", "らんすい")])
def test_kakasi_unidic_noun(case, expected):
    kakasi = pykakasi.Kakasi()
    result = kakasi.convert(case)
    key = kakasi._jconv._kanwa._jisyo_table.get("85cd", None)
    assert result[0]["orig"] == case
    assert result[0]["hira"] == expected


def test_issue_145():
    case = "見えますか？"
    expected = {
        "orig": "ますか",
        "hira": "ますか",
        "kana": "マスカ",
        "hepburn": "masuka",
        "kunrei": "masuka",
        "passport": "masuka",
    }
    kakasi = pykakasi.Kakasi()
    result = kakasi.convert(case)
    assert result[1]["orig"] == expected["orig"]
    assert result[1]["hira"] == expected["hira"]


@pytest.mark.parametrize(
    "case, expected",
    [
        (
            "バニーちゃんちのシャワーノズルの先端",
            [
                {
                    "orig": "バニー",
                    "hira": "ばにー",
                    "kana": "バニー",
                    "hepburn": "banii",
                    "kunrei": "banii",
                    "passport": "banii",
                },
                {
                    "orig": "ちゃんちの",
                    "hira": "ちゃんちの",
                    "kana": "チャンチノ",
                    "hepburn": "chanchino",
                    "kunrei": "tyantino",
                    "passport": "chanchino",
                },
                {
                    "orig": "シャワーノズル",
                    "hira": "しゃわーのずる",
                    "kana": "シャワーノズル",
                    "hepburn": "shawaanozuru",
                    "kunrei": "syawaanozuru",
                    "passport": "shawaanozuru",
                },
                {
                    "orig": "の",
                    "hira": "の",
                    "kana": "ノ",
                    "hepburn": "no",
                    "kunrei": "no",
                    "passport": "no",
                },
                {
                    "orig": "先端",
                    "hira": "せんたん",
                    "kana": "センタン",
                    "hepburn": "sentan",
                    "kunrei": "sentan",
                    "passport": "sentan",
                },
            ],
        ),
        (
            "明日は明日の風が吹く",
            [
                {
                    "orig": "明日",
                    "hira": "あした",
                    "kana": "アシタ",
                    "hepburn": "ashita",
                    "kunrei": "asita",
                    "passport": "ashita",
                },
                {
                    "orig": "は",
                    "hira": "は",
                    "kana": "ハ",
                    "hepburn": "ha",
                    "kunrei": "ha",
                    "passport": "ha",
                },
                {
                    "orig": "明日",
                    "hira": "あした",
                    "kana": "アシタ",
                    "hepburn": "ashita",
                    "kunrei": "asita",
                    "passport": "ashita",
                },
                {
                    "orig": "の",
                    "hira": "の",
                    "kana": "ノ",
                    "hepburn": "no",
                    "kunrei": "no",
                    "passport": "no",
                },
                {
                    "orig": "風",
                    "hira": "かぜ",
                    "kana": "カゼ",
                    "hepburn": "kaze",
                    "kunrei": "kaze",
                    "passport": "kaze",
                },
                {
                    "orig": "が",
                    "hira": "が",
                    "kana": "ガ",
                    "hepburn": "ga",
                    "kunrei": "ga",
                    "passport": "ga",
                },
                {
                    "orig": "吹く",
                    "hira": "ふく",
                    "kana": "フク",
                    "hepburn": "fuku",
                    "kunrei": "fuku",
                    "passport": "fuku",
                },
            ],
        ),
        (
            "\uF862\u6709\u9650\u4F1A\u793E",  # Adobe CID 8321
            [
                {
                    "orig": "\u6709\u9650\u4F1A\u793E",
                    "hira": "ゆうげんがいしゃ",
                    "kana": "ユウゲンガイシャ",
                    "hepburn": "yuugengaisha",
                    "kunrei": "yuugengaisya",
                    "passport": "yuugengaisha",
                }
            ],
        ),
    ],
)
def test_kakasi_unihandecode(case, expected):
    kakasi = pykakasi.Kakasi()
    result = kakasi.convert(case)
    if len(result) < len(expected):
        for i, r in enumerate(result):
            assert r["orig"] == expected[i]["orig"]
            assert r["hira"] == expected[i]["hira"]
            assert r["kana"] == expected[i]["kana"]
            assert r["hepburn"] == expected[i]["hepburn"]
            assert r["kunrei"] == expected[i]["kunrei"]
            assert r["passport"] == expected[i]["passport"]
    else:
        for i, e in enumerate(expected):
            assert result[i]["orig"] == e["orig"]
            assert result[i]["hira"] == e["hira"]
            assert result[i]["kana"] == e["kana"]
            assert result[i]["hepburn"] == e["hepburn"]
            assert result[i]["kunrei"] == e["kunrei"]
            assert result[i]["passport"] == e["passport"]


def test_issue_150():
    kakasi = pykakasi.kakasi()
    result = kakasi.convert("三\u00D7五")
    assert result[0]["hira"] == "さん"
    assert result[1]["orig"] == "\u00D7"
    assert result[1]["hira"] == "×"
    assert result[2]["hira"] == "ご"
    assert len(result) == 3


def test_aozora():
    kakasi = pykakasi.Kakasi()
    result = kakasi.convert("私は品行方正な人間として周囲から待遇されて居る。")
    assert result[0]['kana'] == 'ワタシ'
    assert result[1]['kana'] == 'ハ'
    assert result[2]['kana'] == 'ヒンコウホウセイ'
    assert result[3]['kana'] == 'ナ'
    assert result[4]['kana'] == 'ニンゲン'
    assert result[5]['kana'] == 'トシテ'
    assert result[6]['kana'] == 'シュウイ'
    assert result[7]['kana'] == 'カラ'
    assert result[8]['kana'] == 'タイグウ'
    assert result[9]['kana'] == 'サレテ'
    assert result[10]['kana'] == 'イル。'
