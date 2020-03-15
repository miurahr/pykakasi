# -*- coding: utf-8 -*-

import pykakasi


def test_kakasi_structured():
    TESTS = [
        ("", [{'orig': '', 'hira': '', 'kana': '', 'kunrei': '', 'hepburn': '', 'passport': ''}]),
        ("構成", [{'orig': "構成", 'kana': "コウセイ", 'hira': "こうせい",
                 'hepburn': 'kousei', 'kunrei': "kousei", 'passport': "kosei"}])
    ]

    kakasi = pykakasi.kakasi()
    for case, expected in TESTS:
        result = kakasi.convert(case)
        for i, r in enumerate(result):
            assert r['orig'] == expected[i]['orig']
            assert r['hira'] == expected[i]['hira']
            assert r['kana'] == expected[i]['kana']
            assert r['hepburn'] == expected[i]['hepburn']
