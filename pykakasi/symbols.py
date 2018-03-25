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
    # \u3000、。〃〄〆〈〉《》「」『』【】〒〓〔〕〖〗〘〙
    # 〚〛〜〝〞〟〠
    _table_1 = [" ",",",".",'"',"(kigou)",None,"(sime)",None,"<",">","<<",">>","(",")","(",")",
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

    def __init__(self):
        pass

    def isRegion(self, char):
        c = ord(char[0])
        return ((0x3000 <= c and c< 0x3021) or (0x3030 <= c and c < 0x3040) or
                 (0x0391 <= c and c < 0x03a2) or (0x03a2 < c and c <= 0x03a9) or
                 (0x03b1 <= c and c <= 0x03c9) or
                 (0xff10 <= c and c < 0xff20))

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
        elif (0xff10 <= c and c < 0xff20):
            return six.unichr(c - 0xff10 + ord('0'))
        else:
            return None # pragma: no cover

