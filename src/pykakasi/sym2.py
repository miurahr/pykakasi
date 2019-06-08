# -*- coding: utf-8 -*-
#  symbols.py
#
# Copyright 2014,2018 Hiroshi Miura <miurahr@linux.com>
#
from __future__ import unicode_literals

import six

__license__ = 'GPL 3'
__copyright__ = '2014,2018, Hiroshi Miura <miurahr@linux.com>'
__docformat__ = 'restructuredtext en'

'''
convert symbols to alphabet
based on Original KAKASI's EUC_JP - alphabet converter table
--------------------------------------------------------------------------
 a1 a0 | 　 、 。 ， ． ・ ： ； ？ ！ ゛ ゜ ´ ｀ ¨
         " ",",",".",",",".",".",":",";","?",
         "!","\"","(maru)","'","`","..",
 a1 b0 | ＾ ￣ ＿ ヽ ヾ ゝ ゞ 〃 仝 々 〆 〇 ー ― ‐ ／
       "~","~","_","(kurikaesi)","(kurikaesi)","(kurikaesi)",
       "(kurikaesi)","(kurikaesi)","(kurikaesi)","(kurikaesi)",
       "sime","(maru)","^","-","-","/",
 a1 c0 | ＼ ～ ∥ ｜ … ‥ ‘ ’ “ ” （ ） 〔 〕 ［ ］
      "\\","~","||","|","...","..","`","'","\"","\"","(",")","[","]","[","]",
      "{","}","<",">","<<",">>","(",")","(",")","(",")","+","-","+-","X",
 a1 d0 | ｛ ｝ 〈 〉 《 》 「 」 『 』 【 】 ＋ － ± ×

 a1 e0 | ÷ ＝ ≠ ＜ ＞ ≦ ≧ ∞ ∴ ♂ ♀ ° ′ ″ ℃ ￥
      "/","=","!=","<",">","<=",">=","(kigou)","...",
      "(osu)","(mesu)","(do)","'","\"","(Sessi)","\\",
 a1 f0 | ＄ ￠ ￡ ％ ＃ ＆ ＊ ＠ § ☆ ★ ○ ● ◎ ◇
      "$","(cent)","(pound)","%","#","&","*","@",
      "(setu)","(hosi)","(hosi)","(maru)","(maru)","(maru)","(diamond)"
---------------------------------------------------------------------------

----------------------------------------------------------
 a2 a0 | ◆ □ ■ △ ▲ ▽ ▼ ※ 〒 → ← ↑ ↓ 〓
 a2 b0 | ∈ ∋ ⊆ ⊇ ⊂ ⊃ a2 c0 | ∪ ∩ ∧ ∨ ￢ ⇒ ⇔ ∀
 a2 d0 | ∃ ∠ ⊥ ⌒ ∂
 a2 e0 | ∇ ≡ ≒ ≪ ≫ √ ∽ ∝ ∵ ∫ ∬
 a2 f0 | Å ‰ ♯ ♭ ♪ † ‡ ¶ ◯
----------------------------------------------------------

Greek convertion table
----------------------------------------------------------
   "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta",
   "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho",
   "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega",
   "", "", "", "", "", "", "", "",
   "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta",
   "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi", "rho",
   "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega"
----------------------------------------------------------
'''


class sym2 (object):
    # U3000 - 301F
    # \u3000、。〃〄〇〆々〈〉《》「」『』【】〒〓〔〕〖〗〘〙
    # 〚〛〜〝〞〟〠
    _table_1 = [" ", ",", ".", '"', "(kigou)", "(kurikaesi)", "(sime)", "(maru)", "<", ">",
                "<<", ">>", "(", ")", "(", ")", "(", ")", "(kigou)", "(geta)",
                "(", ")", "(", ")", "(", ")", "(", ")", "~", "(kigou)", "\"",
                "(kigou)", "(kigou)"]
    # U3030 - 3040
    # 〰〱〲〳〴〵〶〷〼〽〾〿
    _table_2 = ["-", "(kurikaesi)",
                "(kurikaesi)", "(kurikaesi)", "(kurikaesi)", "(kurikaesi)",
                "(kigou)", "XX", None, None, None, None, "(masu)", "(kurikaesi)", " ", " "]
    # U0391-03A9
    _table_3 = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta",
                "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", None,
                "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega"]
    # U03B1-03C9
    _table_4 = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta",
                "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi", "rho", "final sigma",
                "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega"]
    # UFF01-FF0F
    _table_5 = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+",
                ",", "-", ".", "/"]
    # cyriilic
    cyrillicTable = {  # basic cyrillic characters
        '\u0410': 'A', '\u0411': 'B', '\u0412': 'V',  # АБВ
        '\u0413': 'G', '\u0414': 'D', '\u0415': 'E',  # ГДЕ
        '\u0401': 'E', '\u0416': 'Zh', '\u0417': 'Z',  # ЁЖЗ
        '\u0418': 'I', '\u0419': 'Y', '\u041a': 'K',  # ИЙК
        '\u041b': 'L', '\u041c': 'M', '\u041d': 'N',  # ЛМН
        '\u041e': 'O', '\u041f': 'P', '\u0420': 'R',  # ОПР
        '\u0421': 'S', '\u0422': 'T', '\u0423': 'U',  # СТУ
        '\u0424': 'F', '\u0425': 'H', '\u0426': 'Ts',  # ФХЦ
        '\u0427': 'Ch', '\u0428': 'Sh', '\u0429': 'Sch',  # ЧШЩ
        '\u042a': '', '\u042b': 'Y', '\u042c': '',  # ЪЫЬ
        '\u042d': 'E', '\u042e': 'Yu', '\u042f': 'Ya',  # ЭЮЯ
        '\u0430': 'a', '\u0431': 'b', '\u0432': 'v',  # абв
        '\u0433': 'g', '\u0434': 'd', '\u0435': 'e',  # где
        '\u0451': 'e', '\u0436': 'zh', '\u0437': 'z',  # ёжз
        '\u0438': 'i', '\u0439': 'y', '\u043a': 'k',  # ийк
        '\u043b': 'l', '\u043c': 'm', '\u043d': 'n',  # лмн
        '\u043e': 'o', '\u043f': 'p', '\u0440': 'r',  # опр
        '\u0441': 's', '\u0442': 't', '\u0443': 'u',  # сту
        '\u0444': 'f', '\u0445': 'h', '\u0446': 'ts',  # фхц
        '\u0447': 'ch', '\u0448': 'sh', '\u0449': 'sch',  # чшщ
        '\u044a': '', '\u044b': 'y', '\u044c': '',  # ъыь
        '\u044d': 'e', '\u044e': 'yu', '\u044f': 'ya'  # эюя
    }

    def __init__(self, mode):
        if mode == "a":
            self.convert = self.convert_a
        else:
            self.convert = self.convert_noop

    def isRegion(self, char):
        c = ord(char[0])
        return (0x3000 <= c < 0x3021) or (0x3030 <= c < 0x3040) or (0x0391 <= c < 0x03a2) or (0x03a2 < c <= 0x03a9) or \
               (0x03b1 <= c <= 0x03c9) or (0x0410 <= c <= 0x044f) or (0xff01 <= c <= 0xff1a) or \
               (0xff20 <= c <= 0xff5e) or c == 0x0451 or c == 0x0401

    def _convert(self, text):
        c = ord(text[0])
        if 0x3000 <= c < 0x3021:
            return self._table_1[c - 0x3000]
        elif 0x3030 <= c < 0x3040:
            return self._table_2[c - 0x3030]
        elif 0x0391 <= c <= 0x03a9:
            return self._table_3[c - 0x0391]
        elif 0x03b1 <= c <= 0x03c9:
            return self._table_4[c - 0x03b1]
        elif 0x0410 <= c <= 0x044f:
            return self.cyrillicTable[text[0]]
        elif c == 0x0451 or c == 0x0401:
            return self.cyrillicTable[text[0]]
        elif 0xff01 <= c <= 0xff0f:
            return self._table_5[c - 0xff01]
        elif 0xff10 <= c <= 0xff1a:
            return six.unichr(c - 0xff10 + ord('0'))
        elif 0xff20 <= c <= 0xff40:
            return six.unichr(0x0041 + c - 0xff21)  # u\ff21Ａ => u\0041:@A..Z[\]^_`
        elif 0xff41 <= c < 0xff5f:
            return six.unichr(0x0061 + c - 0xff41)  # u\ff41ａ => u\0061:a..z{|}
        else:
            return ""  # pragma: no cover

    def convert_a(self, text):
        t = self._convert(text)
        if len(t):
            return t, 1
        else:
            return "", 0

    def convert_noop(self, text):
        return text[0], 1
