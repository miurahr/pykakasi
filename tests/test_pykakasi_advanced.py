# -*- coding: utf-8 -*-

import pykakasi


def test_kakasi_constitution():

    original_text = u"日本国民は、正当に選挙された国会における代表者を通じて行動し、われらとわれらの子孫のために、" \
                    u"諸国民との協和による成果と、わが国全土にわたつて自由のもたらす恵沢を確保し、" \
                    u"政府の行為によつて再び戦争の惨禍が起ることのないやうにすることを決意し、ここに主権が国民に存することを宣言し、" \
                    u"この憲法を確定する。そもそも国政は、国民の厳粛な信託によるものであつて、その権威は国民に由来し、" \
                    u"その権力は国民の代表者がこれを行使し、その福利は国民がこれを享受する。これは人類普遍の原理であり、" \
                    u"この憲法は、かかる原理に基くものである。われらは、これに反する一切の憲法、法令及び詔勅を排除する。"
    result = "Nihonkokumin ha, Seitou ni Senkyo sareta Kokkai niokeru Daihyousha wo Tsuuji te Koudou shi, " \
             "wareratowarerano Shison notameni, Shokokumin tono Kyouwa niyoru Seika to, waga Kuni Zendo " \
             "niwatatsute Jiyuu nomotarasu Keitaku wo Kakuho shi," \
             " Seifu no Koui niyotsute Futatabi Sensou no Sanka ga Okoru kotononaiyaunisurukotowo Ketsui shi, " \
             "kokoni Shuken ga Kokumin ni Sonsu rukotowo Sengen shi, kono Kenpou wo Kakuteisu ru. " \
             "somosomo Kokusei ha, Kokumin no Genshuku na Shintaku niyorumonodeatsute, sono Ken'i ha Kokumin ni " \
             "Yurai shi, sono Kenryoku ha Kokumin no Daihyousha gakorewo Koushi shi, sono Fukuri ha Kokumin " \
             "gakorewo Kyouju suru. koreha Jinruifuhen no Genri deari, kono Kenpou ha, kakaru Genri ni Motozuku " \
             "monodearu. wareraha, koreni Hansu ru Issai no Kenpou, Hourei Oyobi Shouchoku wo Haijo suru."

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

    original_text = u"日本国民は、正当に選挙された国会における代表者を通じて行動し、われらとわれらの子孫のために、" \
                    u"諸国民との協和による成果と、わが国全土にわたつて自由のもたらす恵沢を確保し、" \
                    u"政府の行為によつて再び戦争の惨禍が起ることのないやうにすることを決意し、ここに主権が国民に存することを宣言し、" \
                    u"この憲法を確定する。そもそも国政は、国民の厳粛な信託によるものであつて、その権威は国民に由来し、" \
                    u"その権力は国民の代表者がこれを行使し、その福利は国民がこれを享受する。これは人類普遍の原理であり、" \
                    u"この憲法は、かかる原理に基くものである。われらは、これに反する一切の憲法、法令及び詔勅を排除する。"
    result = u"日本国民 は、 正当 に 選挙 された 国会 における 代表者 を 通じ て 行動 し、われらとわれらの 子孫 のために、 " \
             u"諸国民 との 協和 による 成果 と、わが 国 全土 にわたつて 自由 のもたらす 恵沢 を 確保 し、 政府 の 行為 によつて 再び 戦争 " \
             u"の 惨禍 が 起る ことのないやうにすることを 決意 し、ここに 主権 が 国民 に 存す ることを " \
             u"宣言 し、この 憲法 を 確定す る。そもそも 国政 は、 国民 の 厳粛 な 信託 によるものであつて、" \
             u"その 権威 は 国民 に 由来 し、その 権力 は 国民 の 代表者 がこれを 行使 し、その 福利 は 国民 " \
             u"がこれを 享受 する。これは 人類普遍 の 原理 であり、この 憲法 は、かかる 原理 に 基く ものである。われらは、" \
             u"これに 反す る 一切 の 憲法 、 法令 及び 詔勅 を 排除 する。"

    wakati = pykakasi.wakati()
    converter = wakati.getConverter()
    assert converter.do(original_text) == result
