# -*- coding: utf-8 -*-
import unittest
import pykakasi

class TestPyKakasiAdvanced(unittest.TestCase):

    def test_kakasi_constitution(self):

        original_text = u"日本国民は、正当に選挙された国会における代表者を通じて行動し、われらとわれらの子孫のために、諸国民との協和による成果と、わが国全土にわたつて自由のもたらす恵沢を確保し、政府の行為によつて再び戦争の惨禍が起ることのないやうにすることを決意し、ここに主権が国民に存することを宣言し、この憲法を確定する。そもそも国政は、国民の厳粛な信託によるものであつて、その権威は国民に由来し、その権力は国民の代表者がこれを行使し、その福利は国民がこれを享受する。これは人類普遍の原理であり、この憲法は、かかる原理に基くものである。われらは、これに反する一切の憲法、法令及び詔勅を排除する。"
        result = "NihonKokumin Ha, Seitou Ni Senkyosareta Kokkaini Okeru Daihyousha Wo Tsuujite Koudoushi, Wareratowarerano Shison notameni, Shokokumin tono Kyouwa niyoru Seika To, "

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","a")
        kakasi.setMode("K","a")
        kakasi.setMode("J","a")
        kakasi.setMode("r","Hepburn")
        converter  = kakasi.getConverter()
        otext = ""
        for line in original_text:
            otext = otext + converter.do(line)
        self.maxDiff = None
        self.assertEqual(otext, result)

    def test_wakati_constitution(self):

        original_text = u"日本国民は、正当に選挙された国会における代表者を通じて行動し、われらとわれらの子孫のために、諸国民との協和による成果と、わが国全土にわたつて自由のもたらす恵沢を確保し、政府の行為によつて再び戦争の惨禍が起ることのないやうにすることを決意し、ここに主権が国民に存することを宣言し、この憲法を確定する。そもそも国政は、国民の厳粛な信託によるものであつて、その権威は国民に由来し、その権力は国民の代表者がこれを行使し、その福利は国民がこれを享受する。これは人類普遍の原理であり、この憲法は、かかる原理に基くものである。われらは、これに反する一切の憲法、法令及び詔勅を排除する。"
        result = u"日本国民は、 正当に 選挙された 国会に おける 代表者を 通じて 行動し、 われらと われらの 子孫の ために 、 諸国民 と の 協和 に よる 成果 と、 わが国 全土 に わたつて 自由 の もたらす 恵沢 を 確保し 、 政府 の 行為 に よつて 再び 戦争 の 惨禍 が 起る こと の ないやうに する こと を 決意し 、 ここ に 主権 が 国民 に 存する こと を 宣言し 、 この 憲法 を 確定 する 。 そもそも 国政 は 、 国民 の 厳粛な 信託 に よる もの で あつて 、 その 権威 は 国民 に 由来し 、 その 権力 は 国民 の 代表者 が これ を 行使し 、 その 福利 は 国民 が これ を 享受する 。 これ は 人類 普遍 の 原理 で あり 、 この 憲法 は 、 かかる 原理 に 基く もの で ある。 われら は 、 これ に 反する 一切 の 憲法 、 法令 及び 詔勅 を 排除する 。"

        wakati = pykakasi.wakati()
        converter = wakati.getConverter()
        otext = ""
        for line in original_text:
            otext = otext + converter.do(line)
        self.maxDiff = None
        self.assertEqual(otext, result)

