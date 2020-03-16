# -*- coding: utf-8 -*-

import pykakasi


def test_kakasi_structured_constitution():

    original_text = "日本国民は、正当に選挙された国会における代表者を通じて行動し、われらとわれらの子孫のために、" \
                    "諸国民との協和による成果と、わが国全土にわたつて自由のもたらす恵沢を確保し、" \
                    "政府の行為によつて再び戦争の惨禍が起ることのないやうにすることを決意し、ここに主権が国民に存することを宣言し、" \
                    "この憲法を確定する。そもそも国政は、国民の厳粛な信託によるものであつて、その権威は国民に由来し、" \
                    "その権力は国民の代表者がこれを行使し、その福利は国民がこれを享受する。これは人類普遍の原理であり、" \
                    "この憲法は、かかる原理に基くものである。われらは、これに反する一切の憲法、法令及び詔勅を排除する。"

    expected = [{'orig': "日本国民", 'kana': "ニホンコクミン", 'hira': "にほんこくみん", 'hepburn': "nihonkokumin"},
                {'orig': "は、", 'kana': "ハ、", 'hira': "は、", 'hepburn': "ha,"},
                {'orig': "正当", 'kana': "セイトウ", 'hira': "せいとう", 'hepburn': "seitou"},
                {'orig': "に", 'kana': "ニ", 'hira': "に", 'hepburn': "ni"},
                {'orig': "選挙", 'kana': "センキョ", 'hira': "せんきょ", 'hepburn': "senkyo"},
                {'orig': "された", 'kana': "サレタ", 'hira': "された", 'hepburn': "sareta"},
                {'orig': "国会", 'kana': "コッカイ", 'hira': "こっかい", 'hepburn': "kokkai"},
                {'orig': "における", 'kana': "ニオケル", 'hira': "における", 'hepburn': "niokeru"},
                {'orig': "代表者", 'kana': "ダイヒョウシャ", 'hira': "だいひょうしゃ", 'hepburn': "daihyousha"},
                {'orig': "を", 'kana': "ヲ", 'hira': "を", 'hepburn': "wo"},
                {'orig': "通じ", 'kana': "ツウジ", 'hira': "つうじ", 'hepburn': "tsuuji"},
                {'orig': "て", 'kana': "テ", 'hira': "て", 'hepburn': 'te'},
                {'orig': "行動", 'kana': "コウドウ", 'hira': "こうどう", 'hepburn': 'koudou'},
                {'orig': "し、", 'kana': "シ、", 'hira': "し、", 'hepburn': 'shi,'},
                {'orig': "われらとわれらの", 'kana': "ワレラトワレラノ", 'hira': "われらとわれらの", 'hepburn': "wareratowarerano"},
                {'orig': "子孫", 'kana': "シソン", 'hira': "しそん", 'hepburn': "shison"},
                {'orig': "のために、", 'kana': "ノタメニ、", 'hira': "のために、", 'hepburn': "notameni,"},
                {'orig': "諸国民", 'kana': "ショコクミン", 'hira': "しょこくみん", 'hepburn': "shokokumin"},
                {'orig': "との", 'kana': "トノ", 'hira': "との", 'hepburn': "tono"},
                {'orig': "協和", 'kana': "キョウワ", 'hira': "きょうわ", 'hepburn': "kyouwa"},
                {'orig': "による", 'kana': "ニヨル", 'hira': "による", 'hepburn': "niyoru"},
                {'orig': "成果", 'kana': "セイカ", 'hira': "せいか", 'hepburn': "seika"},
                {'orig': "と、", 'kana': "ト、", 'hira': "と、", 'hepburn': "to,"},
                {'orig': "わが", 'kana': "ワガ", 'hira': "わが", 'hepburn': "waga"},
                {'orig': "国", 'kana': "クニ", 'hira': "くに", 'hepburn': "kuni"},
                {'orig': "全土", 'kana': "ゼンド", 'hira': "ぜんど", 'hepburn': "zendo"},
                {'orig': "にわたつて", 'kana': "ニワタツテ", 'hira': "にわたつて", 'hepburn': "niwatatsute"},
                {'orig': "自由", 'kana': "ジユウ", 'hira': "じゆう", 'hepburn': "jiyuu"},
                {'orig': "のもたらす", 'kana': "ノモタラス", 'hira': 'のもたらす', 'hepburn': "nomotarasu"},
                {'orig': "恵沢", 'kana': "ケイタク", 'hira': "けいたく", 'hepburn': "keitaku"},
                {'orig': "を", 'kana': "ヲ", 'hira': "を", 'hepburn': 'wo'},
                {'orig': "確保", 'kana': "カクホ", 'hira': "かくほ", 'hepburn': "kakuho"},
                {'orig': "し、", 'kana': "シ、", 'hira': "し、", 'hepburn': "shi,"},
                {'orig': "政府", 'kana': "セイフ", 'hira': "せいふ", 'hepburn': "seifu"},
                {'orig': "の", 'kana': "ノ", 'hira': "の", 'hepburn': "no"},
                {'orig': "行為", 'kana': "コウイ", 'hira': "こうい", 'hepburn': "koui"},
                {'orig': "によつて", 'kana': "ニヨツテ", 'hira': "によつて", 'hepburn': "niyotsute"},
                {'orig': "再び", 'kana': "フタタビ", 'hira': "ふたたび", 'hepburn': "futatabi"},
                {'orig': "戦争", 'kana': "センソウ", 'hira': "せんそう", 'hepburn': "sensou"},
                {'orig': "の", 'kana': "ノ", 'hira': "の", 'hepburn': "no"},
                ]

    kakasi = pykakasi.kakasi()
    result = kakasi.convert(original_text)
    for i, e in enumerate(expected):
        assert result[i]['orig'] == e['orig']
        assert result[i]['hira'] == e['hira']
        assert result[i]['kana'] == e['kana']
        assert result[i]['hepburn'] == e['hepburn']
