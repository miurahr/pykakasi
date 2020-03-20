# -*- coding: utf-8 -*-
import pytest

import pykakasi


@pytest.mark.parametrize("case, expected",
                         [("", [{'orig': '', 'hira': '', 'kana': '', 'kunrei': '', 'hepburn': '', 'passport': ''}]),
                          ("構成",
                           [
                               {'orig': "構成", 'kana': "コウセイ", 'hira': "こうせい",
                                'hepburn': 'kousei', 'kunrei': "kousei", 'passport': "kosei"}
                           ]),
                          ("私がこの子を助けなきゃいけないってことだよね",
                           [
                               {'orig': "私", 'kana': "ワタシ", 'hira': "わたし", 'hepburn': "watashi", 'kunrei': "watasi", 'passport': "watashi"},
                               {'orig': "がこの", 'kana': "ガコノ", 'hira': "がこの", 'hepburn': "gakono", 'kunrei': "gakono", 'passport': "gakono"},
                               {'orig': "子", 'kana': "コ", 'hira': "こ", 'hepburn': "ko", 'kunrei': "ko", 'passport': "ko"},
                               {'orig': "を", 'kana': "ヲ", 'hira': "を", 'hepburn': "wo", 'kunrei': "wo", 'passport': "wo"},
                               {'orig': "助け", 'kana': "タスケ", 'hira': "たすけ", 'hepburn': "tasuke", 'kunrei': "tasuke", 'passport': "tasuke"},
                               {'orig': "なきゃいけないってことだよね", 'kana': "ナキャイケナイッテコトダヨネ", 'hira': "なきゃいけないってことだよね",
                                'hepburn': "nakyaikenaittekotodayone", 'kunrei': "nakyaikenaittekotodayone", 'passport': "nakyaikenaittekotodayone"}
                           ]),
                          ('やったー', [{'orig': 'やったー', 'kana': "ヤッター", 'hira': "やったー", 'hepburn': 'yattaa', 'kunrei': 'yattaa', 'passport': "yattaa"}]),
                          ('でっでー', [{'orig': 'でっでー', 'kana': "デッデー", 'hira': 'でっでー', 'hepburn': 'deddee', 'kunrei': 'deddee', 'passport': 'deddee'}]),
                          ('てんさーふろー', [{
                              'orig': 'てんさーふろー', 'kana': "テンサーフロー", 'hira': 'てんさーふろー',
                              'hepburn': 'tensaafuroo', 'kunrei': 'tensaafuroo', 'passport': 'tensaafuroo'}]),
                          ])
def test_kakasi_structured(case, expected):
    kakasi = pykakasi.kakasi()
    result = kakasi.convert(case)
    for i, r in enumerate(result):
        assert r['orig'] == expected[i]['orig']
        assert r['hira'] == expected[i]['hira']
        assert r['kana'] == expected[i]['kana']
        assert r['hepburn'] == expected[i]['hepburn']
        assert r['kunrei'] == expected[i]['kunrei']
        assert r['passport'] == expected[i]['passport']
