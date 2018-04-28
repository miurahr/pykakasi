# -*- coding: utf-8 -*-
#  symbols.py
#
# Copyright 2014 Hiroshi Miura <miurahr@linux.com>
#
__license__ = 'GPL 3'
__copyright__ = '2014, Hiroshi Miura <miurahr@linux.com>'
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

import six

class sym2 (object):
    # U3000 - 301F
    # \u3000、。〃〄〇〆々〈〉《》「」『』【】〒〓〔〕〖〗〘〙
    # 〚〛〜〝〞〟〠
    _table_1 = [" ",",",".",'"',"(kigou)","(kurikaesi)","(sime)","(maru)","<",">","<<",">>","(",")","(",")",
            "(",")","(kigou)","(geta)","(",")","(",")","(",")","(",
            ")","~","(kigou)","\"","(kigou)","(kigou)"]
    # U3030 - 3040
    # 〰〱〲〳〴〵〶〷〼〽〾〿
    _table_2 = [ "-","(kurikaesi)",
            "(kurikaesi)","(kurikaesi)","(kurikaesi)","(kurikaesi)",
            "(kigou)","XX",None,None,None,None,"(masu)","(kurikaesi)"," "," "]
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
    cyrillicTable = {
            # basic cyrillic characters
            u'\u0410': u'A',u'\u0411': u'B',u'\u0412': u'V',#АБВ
            u'\u0413': u'G',u'\u0414': u'D',u'\u0415': u'E',#ГДЕ
            u'\u0401': u'E',u'\u0416': u'Zh',u'\u0417': u'Z',#ЁЖЗ
            u'\u0418': u'I',u'\u0419': u'Y',u'\u041a': u'K',#ИЙК
            u'\u041b': u'L',u'\u041c': u'M',u'\u041d': u'N',#ЛМН
            u'\u041e': u'O',u'\u041f': u'P',u'\u0420': u'R',#ОПР
            u'\u0421': u'S',u'\u0422': u'T',u'\u0423': u'U',#СТУ
            u'\u0424': u'F',u'\u0425': u'H',u'\u0426': u'Ts',#ФХЦ
            u'\u0427': u'Ch',u'\u0428': u'Sh',u'\u0429': u'Sch',#ЧШЩ
            u'\u042a': u'' ,u'\u042b': u'Y',u'\u042c': u'',#ЪЫЬ
            u'\u042d': u'E',u'\u042e': u'Yu',u'\u042f': u'Ya',#ЭЮЯ
            u'\u0430': u'a',u'\u0431': u'b', u'\u0432': u'v',#абв
            u'\u0433': u'g',u'\u0434': u'd',u'\u0435': u'e',#где
            u'\u0451': u'e',u'\u0436': u'zh',u'\u0437': u'z',#ёжз
            u'\u0438': u'i',u'\u0439': u'y',u'\u043a': u'k',#ийк
            u'\u043b': u'l',u'\u043c': u'm',u'\u043d': u'n',#лмн
            u'\u043e': u'o',u'\u043f': u'p',u'\u0440': u'r',#опр
            u'\u0441': u's',u'\u0442': u't',u'\u0443': u'u',#сту
            u'\u0444': u'f',u'\u0445': u'h',u'\u0446': u'ts',#фхц
            u'\u0447': u'ch',u'\u0448': u'sh',u'\u0449': u'sch',#чшщ
            u'\u044a': u'',u'\u044b': u'y',u'\u044c': u'',#ъыь
            u'\u044d': u'e',u'\u044e': u'yu',u'\u044f': u'ya'#эюя
            }

    def __init__(self):
        pass

    def isRegion(self, char):
        c = ord(char[0])
        return ((0x3000 <= c and c< 0x3021) or (0x3030 <= c and c < 0x3040) or
                 (0x0391 <= c and c < 0x03a2) or (0x03a2 < c and c <= 0x03a9) or
                 (0x03b1 <= c and c <= 0x03c9) or
                 (0x0410 <= c and c <= 0x044f) or
                 (0xff01 <= c and c <= 0xff1a) or
                 (0xff20 <= c and c <= 0xff5e) or
                 c == 0x0451 or c == 0x0401)

    def convert(self, text):
        c = ord(text[0])
        if   (0x3000<= c and c < 0x3021):
            return self._table_1[c-0x3000]
        elif (0x3030 <= c and c < 0x3040):
            return self._table_2[c-0x3030]
        elif (0x0391 <= c and c <= 0x03a9):
            return self._table_3[c-0x0391]
        elif (0x03b1 <= c and c <= 0x03c9):
            return self._table_4[c-0x03b1]
        elif (0x0410 <= c and c <= 0x044f) or c == 0x0451 or c == 0x0401:
            return self.cyrillicTable[text[0]]
        elif (0xff01 <= c and c <= 0xff0f):
            return self._table_5[c-0xff01]
        elif (0xff10 <= c and c < 0xff1a):
            return six.unichr(c - 0xff10 + ord('0'))
        elif (0xff20 <= c and c <= 0xff40):
            return six.unichr(0x0041+c-0xff21)# u\ff21Ａ => u\0041:@A..Z[\]^_`
        elif (0xff41 <= c and c < 0xff5f):
            return six.unichr(0x0061+c-0xff41)# u\ff41ａ => u\0061:a..z{|}
        else:
            return None # pragma: no cover

