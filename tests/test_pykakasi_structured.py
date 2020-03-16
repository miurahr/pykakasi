# -*- coding: utf-8 -*-
import pykakasi
import pytest


@pytest.mark.parametrize("case, expected",
                         [("", [{'orig': '', 'hira': '', 'kana': '', 'kunrei': '', 'hepburn': '', 'passport': ''}]),
                          ("構成", [{'orig': "構成", 'kana': "コウセイ", 'hira': "こうせい",
                                   'hepburn': 'kousei', 'kunrei': "kousei", 'passport': "kosei"}]),
                          ("私がこの子を助けなきゃいけないってことだよね",
                           [
                               {'orig': "私", 'kana': "ワタシ", 'hira': "わたし", 'hepburn': "watashi"},
                               {'orig': "がこの", 'kana': "ガコノ", 'hira': "がこの", 'hepburn': "gakono"},
                               {'orig': "子", 'kana': "コ", 'hira': "こ", 'hepburn': "ko"},
                               {'orig': "を", 'kana': "ヲ", 'hira': "を", 'hepburn': "wo"},
                               {'orig': "助け", 'kana': "タスケ", 'hira': "たすけ", 'hepburn': "tasuke"},
                               {'orig': "なきゃいけないってことだよね", 'kana': "ナキャイケナイッテコトダヨネ",
                                'hira': "なきゃいけないってことだよね", 'hepburn': "nakyaikenaittekotodayone"}
                           ])
                          ])
def test_kakasi_structured(case, expected):
    kakasi = pykakasi.kakasi()
    result = kakasi.convert(case)
    for i, r in enumerate(result):
        assert r['orig'] == expected[i]['orig']
        assert r['hira'] == expected[i]['hira']
        assert r['kana'] == expected[i]['kana']
        assert r['hepburn'] == expected[i]['hepburn']
