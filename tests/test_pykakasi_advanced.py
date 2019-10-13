# -*- coding: utf-8 -*-

import pykakasi
import pytest


@pytest.mark.xfail(reason='Wrong result for comma seperation.')
def test_kakasi_structured_constitution():

    original_text = u"日本国民は、正当に選挙された国会における代表者を通じて行動し、われらとわれらの子孫のために、" \
                    u"諸国民との協和による成果と、わが国全土にわたつて自由のもたらす恵沢を確保し、" \
                    u"政府の行為によつて再び戦争の惨禍が起ることのないやうにすることを決意し、ここに主権が国民に存することを宣言し、" \
                    u"この憲法を確定する。そもそも国政は、国民の厳粛な信託によるものであつて、その権威は国民に由来し、" \
                    u"その権力は国民の代表者がこれを行使し、その福利は国民がこれを享受する。これは人類普遍の原理であり、" \
                    u"この憲法は、かかる原理に基くものである。われらは、これに反する一切の憲法、法令及び詔勅を排除する。"

    expected = [{'orig': '日本国民', 'hepburn': 'nihonkokumin'},
                {'orig': 'は、', 'hepburn': 'ha,'},
                {'orig': '正当', 'hepburn': 'seitou'},
                {'orig': 'に', 'hepburn': 'ni'},
                {'orig': '選挙', 'hepburn': 'senkyo'},
                {'orig': 'された', 'hepburn': 'sareta'},
                {'orig': '国会', 'hepburn': 'kokkai'},
                {'orig': 'における', 'hepburn': 'niokeru'},
                {'orig': '代表者', 'hepburn': 'daihyousha'},
                {'orig': 'を', 'hepburn': 'wo'},
                {'orig': '通じ', 'hepburn': 'tsuuji'},
                {'orig': 'て', 'hepburn': 'te'},
                {'orig': '行動', 'hepburn': 'koudou'},
                {'orig': 'し、', 'hepburn': 'shi,'},
                {'orig': 'われらとわれらの', 'hepburn': 'wareratowarerano'},
                # {'orig': 'し、われらとわれらの', 'hepburn': 'shi,wareratowarerano'},
                {'orig': '子孫', 'hepburn': 'shison'},
                {'orig': 'のために、', 'hepburn': 'notameni,'},
                {'orig': '諸国民', 'hepburn': 'shokokumin'},
                {'orig': 'との', 'hepburn': 'tono'},
                {'orig': '協和', 'hepburn': 'kyouwa'},
                {'orig': 'による', 'hepburn': 'niyoru'},
                {'orig': '成果', 'hepburn': 'seika'},
                {'orig': 'と、', 'hepburn': 'to,'},
                {'orig': 'わが', 'hepburn': 'waga'},
                # {'orig': 'と、わが', 'hepburn': 'to,waga'},
                {'orig': '国', 'hepburn': 'kuni'},
                {'orig': '全土', 'hepburn': 'zendo'},
                {'orig': 'にわたつて', 'hepburn': 'niwatatsute'},
                {'orig': '自由', 'hepburn': 'jiyuu'},
                {'orig': 'のもたらす', 'hepburn': 'nomotarasu'},
                {'orig': '恵沢', 'hepburn': 'keitaku'},
                ]

    kakasi = pykakasi.kakasi()
    result = kakasi.convert(original_text)
    for i, r in enumerate(expected):
        assert r['orig'] == result[i]['orig']
        assert r['hepburn'] == result[i]['hepburn']
