# -*- coding: utf-8 -*-
import pytest

import pykakasi


@pytest.mark.parametrize("case, expected", [
    ("", [{'orig': '', 'hira': '', 'kana': '', 'kunrei': '', 'hepburn': '', 'passport': ''}]),
    ("構成",
     [
         {'orig': "構成", 'kana': "コウセイ", 'hira': "こうせい",
          'hepburn': 'kousei', 'kunrei': "kousei", 'passport': "kosei"}
     ]),
    ('好き',
     [{'orig': '好き', 'hira': 'すき', 'kana': 'スキ', 'hepburn': 'suki', 'kunrei': 'suki', 'passport': 'suki'}]),
    ('大きい',
     [{'orig': '大きい', 'hira': 'おおきい', 'kana': 'オオキイ', 'hepburn': 'ookii', 'kunrei': 'ookii', 'passport': 'okii'}]),
    ('かんたん',
     [{'orig': 'かんたん', 'hira': 'かんたん', 'kana': 'カンタン', 'hepburn': 'kantan', 'kunrei': 'kantan', 'passport': 'kantan'}]),
    ('にゃ',
     [{'orig': 'にゃ', 'hira': 'にゃ', 'kana': 'ニャ', 'hepburn': 'nya', 'kunrei': 'nya', 'passport': 'nya'}]),
    ('っき',
     [{'orig': 'っき', 'hira': 'っき', 'kana': 'ッキ', 'hepburn': 'kki', 'kunrei': 'kki', 'passport': 'kki'}]),
    ('っふぁ',
     [{'orig': 'っふぁ', 'hira': 'っふぁ', 'kana': 'ッファ', 'hepburn': 'ffa', 'kunrei': 'ffa', 'passport': 'ffa'}]),
    ('キャ',
     [{'orig': 'キャ', 'hira': 'きゃ', 'kana': 'キャ', 'hepburn': 'kya', 'kunrei': 'kya', 'passport': 'kya'}]),
    ('キュ',
     [{'orig': 'キュ', 'hira': 'きゅ', 'kana': 'キュ', 'hepburn': 'kyu', 'kunrei': 'kyu', 'passport': 'kyu'}]),
    ('キョ',
     [{'orig': 'キョ', 'hira': 'きょ', 'kana': 'キョ', 'hepburn': 'kyo', 'kunrei': 'kyo', 'passport': 'kyo'}]),
    ('漢字とひらがな交じり文',
     [
         {'orig': '漢字', 'hira': 'かんじ', 'kana': 'カンジ', 'hepburn': 'kanji', 'kunrei': 'kanzi', 'passport': 'kanji'},
         {'orig': 'とひらがな', 'hira': 'とひらがな', 'kana': 'トヒラガナ', 'hepburn': 'tohiragana', 'kunrei': 'tohiragana', 'passport': 'tohiragana'},
         {'orig': '交じり', 'hira': 'まじり', 'kana': 'マジリ', 'hepburn': 'majiri', 'kunrei': 'maziri', 'passport': 'majiri'},
         {'orig': '文', 'hira': 'ぶん', 'kana': 'ブン', 'hepburn': 'bun', 'kunrei': 'bun', 'passport': 'bun'}
     ]),
    ('Alphabet 123 and 漢字',
     [
         {'orig': 'Alphabet 123 and ', 'hira': 'Alphabet 123 and ', 'kana': 'Alphabet 123 and ',
             'hepburn': 'Alphabet 123 and ', 'kunrei': 'Alphabet 123 and ', 'passport': 'Alphabet 123 and '},
         {'orig': '漢字', 'hira': 'かんじ', 'kana': 'カンジ', 'hepburn': 'kanji', 'kunrei': 'kanzi', 'passport': 'kanji'}
     ]),
    ('日経新聞',
     [{'orig': '日経新聞', 'hira': 'にっけいしんぶん', 'kana': 'ニッケイシンブン', 'hepburn': 'nikkeishinbun', 'kunrei': 'nikkeisinbun', 'passport': 'nikkeishimbun'}]),
    ('日本国民は、',
     [
         {'orig': '日本国民', 'hira': 'にほんこくみん', 'kana': 'ニホンコクミン', 'hepburn': 'nihonkokumin', 'kunrei': 'nihonkokumin', 'passport': 'nihonkokumin'},
         {'orig': 'は、', 'hira': 'は、', 'kana': 'ハ、', 'hepburn': 'ha,', 'kunrei': 'ha,', 'passport': 'ha,'}
     ]),
    ("私がこの子を助けなきゃいけないってことだよね",
     [
         {'orig': "私", 'kana': "ワタシ", 'hira': "わたし", 'hepburn': "watashi", 'kunrei': "watasi", 'passport': "watashi"},
         {'orig': "がこの", 'kana': "ガコノ", 'hira': "がこの", 'hepburn': "gakono", 'kunrei': "gakono", 'passport': "gakono"},
         {'orig': "子", 'kana': "コ", 'hira': "こ", 'hepburn': "ko", 'kunrei': "ko", 'passport': "ko"},
         {'orig': "を", 'kana': "ヲ", 'hira': "を", 'hepburn': "wo", 'kunrei': "wo", 'passport': "wo"},
         {'orig': "助け", 'kana': "タスケ", 'hira': "たすけ", 'hepburn': "tasuke", 'kunrei': "tasuke", 'passport': "tasuke"},
         {'orig': "なきゃいけないってことだよね", 'kana': "ナキャイケナイッテコトダヨネ", 'hira': "なきゃいけないってことだよね",
          'hepburn': "nakyaikenaittekotodayone", 'kunrei': "nakyaikenaittekotodayone",
          'passport': "nakyaikenaittekotodayone"}
     ]),
    ('やったー',
     [{'orig': 'やったー', 'kana': "ヤッター", 'hira': "やったー", 'hepburn': 'yattaa', 'kunrei': 'yattaa', 'passport': "yattaa"}]),
    ('でっでー',
     [{'orig': 'でっでー', 'kana': "デッデー", 'hira': 'でっでー', 'hepburn': 'deddee', 'kunrei': 'deddee', 'passport': 'deddee'}]),
    ('てんさーふろー', [{
        'orig': 'てんさーふろー', 'kana': "テンサーフロー", 'hira': 'てんさーふろー',
        'hepburn': 'tensaafuroo', 'kunrei': 'tensaafuroo', 'passport': 'tensaafuroo'}]),
])
def test_kakasi_structured(case, expected):
    kakasi = pykakasi.kakasi()
    result = kakasi.convert(case)
    assert len(result) == len(expected)
    for i, r in enumerate(result):
        assert r['orig'] == expected[i]['orig']
        assert r['hira'] == expected[i]['hira']
        assert r['kana'] == expected[i]['kana']
        assert r['hepburn'] == expected[i]['hepburn']
        assert r['kunrei'] == expected[i]['kunrei']
        assert r['passport'] == expected[i]['passport']
