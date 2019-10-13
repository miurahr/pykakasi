# -*- coding: utf-8 -*-

import pykakasi


def test_kakasi_structured():
    TESTS = [
        (u"", [{'orig': '', 'hira': '', 'kana': '', 'kunrei': '', 'hepburn': '', 'passport': ''}]),
        (u"構成", [{'orig': u"構成", 'kana': u"コウセイ", 'hira': u"こうせい", 'hepburn': 'kousei',
                  'kunrei': "kousei", 'passport': "kosei"}]),
    ]

    kakasi = pykakasi.kakasi()
    for case, expected in TESTS:
        result = kakasi.convert(case)
        for i, r in enumerate(result):
            assert r['orig'] == expected[i]['orig']
            assert r['hira'] == expected[i]['hira']
            assert r['kana'] == expected[i]['kana']
            assert r['hepburn'] == expected[i]['hepburn']
