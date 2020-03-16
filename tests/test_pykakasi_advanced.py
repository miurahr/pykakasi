# -*- coding: utf-8 -*-

import pykakasi


def test_kakasi_structured_constitution():

    original_text = "日本国民は、正当に選挙された国会における代表者を通じて行動し、われらとわれらの子孫のために、" \
                    "諸国民との協和による成果と、わが国全土にわたつて自由のもたらす恵沢を確保し、" \
                    "政府の行為によつて再び戦争の惨禍が起ることのないやうにすることを決意し、ここに主権が国民に存することを宣言し、" \
                    "この憲法を確定する。そもそも国政は、国民の厳粛な信託によるものであつて、その権威は国民に由来し、" \
                    "その権力は国民の代表者がこれを行使し、その福利は国民がこれを享受する。これは人類普遍の原理であり、" \
                    "この憲法は、かかる原理に基くものである。われらは、これに反する一切の憲法、法令及び詔勅を排除する。"

    expected = [{'orig': "日本国民", 'kana': "ニホンコクミン", 'hira': "にほんこくみん", 'hepburn': "nihonkokumin", 'kunrei': "nihonkokumin", 'passport': "nihonkokumin"},
                {'orig': "は、", 'kana': "ハ、", 'hira': "は、", 'hepburn': "ha,", 'kunrei': "ha,", 'passport': "ha,"},
                {'orig': "正当", 'kana': "セイトウ", 'hira': "せいとう", 'hepburn': "seitou", 'kunrei': "seitou", 'passport': "seito"},
                {'orig': "に", 'kana': "ニ", 'hira': "に", 'hepburn': "ni", 'kunrei': "ni", 'passport': "ni"},
                {'orig': "選挙", 'kana': "センキョ", 'hira': "せんきょ", 'hepburn': "senkyo", 'kunrei': "senkyo", 'passport': "senkyo"},
                {'orig': "された", 'kana': "サレタ", 'hira': "された", 'hepburn': "sareta", 'kunrei': "sareta", 'passport': "sareta"},
                {'orig': "国会", 'kana': "コッカイ", 'hira': "こっかい", 'hepburn': "kokkai", 'kunrei': "kokkai", 'passport': "kokkai"},
                {'orig': "における", 'kana': "ニオケル", 'hira': "における", 'hepburn': "niokeru", 'kunrei': "niokeru", 'passport': "niokeru"},
                {'orig': "代表者", 'kana': "ダイヒョウシャ", 'hira': "だいひょうしゃ", 'hepburn': "daihyousha", 'kunrei': "daihyousya", 'passport': "daihyousha"},
                {'orig': "を", 'kana': "ヲ", 'hira': "を", 'hepburn': "wo", 'kunrei': "wo", 'passport': "wo"},
                {'orig': "通じ", 'kana': "ツウジ", 'hira': "つうじ", 'hepburn': "tsuuji", 'kunrei': "tuuzi", 'passport': "tsuuji"},
                {'orig': "て", 'kana': "テ", 'hira': "て", 'hepburn': "te", 'kunrei': "te", 'passport': "te"},
                {'orig': "行動", 'kana': "コウドウ", 'hira': "こうどう", 'hepburn': "koudou", 'kunrei': "koudou", 'passport': "kodou"},
                {'orig': "し、", 'kana': "シ、", 'hira': "し、", 'hepburn': 'shi,', 'kunrei': "si,", 'passport': "shi,"},
                {'orig': "われらとわれらの", 'kana': "ワレラトワレラノ", 'hira': "われらとわれらの",
                 'hepburn': "wareratowarerano", 'kunrei': "wareratowarerano", 'passport': "wareratowarerano"},
                {'orig': "子孫", 'kana': "シソン", 'hira': "しそん", 'hepburn': "shison", 'kunrei': "sison", 'passport': "shison"},
                {'orig': "のために、", 'kana': "ノタメニ、", 'hira': "のために、", 'hepburn': "notameni,", 'kunrei': "notameni,", 'passport': "notameni,"},
                {'orig': "諸国民", 'kana': "ショコクミン", 'hira': "しょこくみん", 'hepburn': "shokokumin", 'kunrei': "syokokumin", 'passport': "shokokumin"},
                {'orig': "との", 'kana': "トノ", 'hira': "との", 'hepburn': "tono", 'kunrei': "tono", 'passport': "tono"},
                {'orig': "協和", 'kana': "キョウワ", 'hira': "きょうわ", 'hepburn': "kyouwa", 'kunrei': "kyouwa", 'passport': "kyouwa"},
                {'orig': "による", 'kana': "ニヨル", 'hira': "による", 'hepburn': "niyoru", 'kunrei': "niyoru", 'passport': "niyoru"},
                {'orig': "成果", 'kana': "セイカ", 'hira': "せいか", 'hepburn': "seika", 'kunrei': "seika", 'passport': "seika"},
                {'orig': "と、", 'kana': "ト、", 'hira': "と、", 'hepburn': "to,", 'kunrei': "to,", 'passport': "to,"},
                {'orig': "わが", 'kana': "ワガ", 'hira': "わが", 'hepburn': "waga", 'kunrei': "waga", 'passport': "waga"},
                {'orig': "国", 'kana': "クニ", 'hira': "くに", 'hepburn': "kuni", 'kunrei': "kuni", 'passport': "kuni"},
                {'orig': "全土", 'kana': "ゼンド", 'hira': "ぜんど", 'hepburn': "zendo", 'kunrei': "zendo", 'passport': "zendo"},
                {'orig': "にわたつて", 'kana': "ニワタツテ", 'hira': "にわたつて", 'hepburn': "niwatatsute", 'kunrei': "niwatatute", 'passport': "niwatatsute"},
                {'orig': "自由", 'kana': "ジユウ", 'hira': "じゆう", 'hepburn': "jiyuu", 'kunrei': "ziyuu", 'passport': "jiyuu"},
                {'orig': "のもたらす", 'kana': "ノモタラス", 'hira': 'のもたらす', 'hepburn': "nomotarasu", 'kunrei': "nomotarasu", 'passport': "nomotarasu"},
                {'orig': "恵沢", 'kana': "ケイタク", 'hira': "けいたく", 'hepburn': "keitaku", 'kunrei': "keitaku", 'passport': "keitaku"},
                {'orig': "を", 'kana': "ヲ", 'hira': "を", 'hepburn': 'wo', 'kunrei': 'wo', 'passport': 'wo'},
                {'orig': "確保", 'kana': "カクホ", 'hira': "かくほ", 'hepburn': "kakuho", 'kunrei': "kakuho", 'passport': "kakuho"},
                {'orig': "し、", 'kana': "シ、", 'hira': "し、", 'hepburn': "shi,", 'kunrei': "si,", 'passport': "shi,"},
                {'orig': "政府", 'kana': "セイフ", 'hira': "せいふ", 'hepburn': "seifu", 'kunrei': "seifu", 'passport': "seifu"},
                {'orig': "の", 'kana': "ノ", 'hira': "の", 'hepburn': "no", 'kunrei': "no", 'passport': "no"},
                {'orig': "行為", 'kana': "コウイ", 'hira': "こうい", 'hepburn': "koui", 'kunrei': "koui", 'passport': "koi"},
                {'orig': "によつて", 'kana': "ニヨツテ", 'hira': "によつて", 'hepburn': "niyotsute", 'kunrei': "niyotute", 'passport': "niyotsute"},
                {'orig': "再び", 'kana': "フタタビ", 'hira': "ふたたび", 'hepburn': "futatabi", 'kunrei': "futatabi", 'passport': "futatabi"},
                {'orig': "戦争", 'kana': "センソウ", 'hira': "せんそう", 'hepburn': "sensou", 'kunrei': "sensou", 'passport': "senso"},
                {'orig': "の", 'kana': "ノ", 'hira': "の", 'hepburn': "no", 'kunrei': "no", 'passport': "no"},
                ]

    kakasi = pykakasi.kakasi()
    result = kakasi.convert(original_text)
    for i, e in enumerate(expected):
        assert result[i]['orig'] == e['orig']
        assert result[i]['hira'] == e['hira']
        assert result[i]['kana'] == e['kana']
        assert result[i]['hepburn'] == e['hepburn']
        assert result[i]['kunrei'] == e['kunrei']
        assert result[i]['passport'] == e['passport']
