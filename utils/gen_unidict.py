import os
import pathlib
import shutil
import sys
import tempfile

import py7zr

root_dir = pathlib.Path(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


class GenUnidict:
    def __init__(self, unidicz):
        self.unidicz = unidicz

    def generate(self, target):
        tmpd = tempfile.mkdtemp()
        with py7zr.SevenZipFile(self.unidicz, "r") as u:
            u.extractall(path=tmpd)
        with open(os.path.join(tmpd, "lex_3_1.csv"), "r", encoding="utf-8") as f:
            with target.open("w") as o:
                o.write(";; KAKASI (Kanji Kana Simple inversion program)\n"
                        ";; unidict - dictionary distilled from unidic v3.1.0\n"
                        ";; Copyright (c) 2011-2021, The UniDic Consortium\n")
                for line in f:
                    rec = self._parse_unidic(line.strip())
                    if rec is not None:
                        o.write(rec)
                        o.write("\n")
        shutil.rmtree(tmpd)

    def _parse_unidic(self, line: str):
        token = line.split(",")
        key = token[0]
        yomi = token[10]
        role = token[4]
        if role not in ["名詞"]:
            return None
        if not self._is_kanji(key):
            return None
        hira = self._k2h(yomi)
        return "{} {}".format(hira, key)

    def _is_symbol(self, c: int):
        return (
            Ch.ideographic_space <= c <= Ch.postal_mark_face
            or (Ch.wavy_dash <= c <= Ch.ideographic_half_fill_space)
            or (Ch.greece_Alpha <= c <= Ch.greece_Rho)
            or (Ch.greece_Sigma <= c <= Ch.greece_Omega)
            or (Ch.greece_alpha <= c <= Ch.greece_omega)
            or (Ch.cyrillic_A <= c <= Ch.cyrillic_ya)
            or (Ch.zenkaku_exc_mark <= c <= Ch.zenkaku_number_nine)
            or (0xFF20 <= c <= 0xFF5E)
            or c == 0x0451
            or c == 0x0401
        )

    def _k2h(self, text):
        _diff = 0x30A1 - 0x3041  # KATAKANA LETTER A - HIRAGANA A
        _ediff = 0x1B164 - 0x1B150
        Hstr = ""
        max_len = 0
        r = len(text)
        x = 0
        while x < r:
            if 0x1B164 <= ord(text[x]) < 0x1B167:
                Hstr = Hstr + chr(ord(text[x]) - _ediff)
                max_len += 1
                x += 1
            elif ord(text[x]) == 0x1B167:
                Hstr = Hstr + "\u3093"
                max_len += 1
                x += 1
            elif 0x30A0 < ord(text[x]) < 0x30F7:
                Hstr = Hstr + chr(ord(text[x]) - _diff)
                max_len += 1
                x += 1
            elif 0x30F7 <= ord(text[x]) < 0x30FD:
                Hstr = Hstr + text[x]
                max_len += 1
                x += 1
            else:  # pragma: no cover
                break
        return Hstr

    def _is_kanji(self, word: str):
        for c in word:
            if not (0x3400 <= ord(c[0]) < 0xE000):
                return False
        return True


class Ch:
    space = 0x20
    at_mark = 0x40
    alphabet_A = 0x41
    alphabet_Z = 0x5A
    square_bra = 0x5B
    back_quote = 0x60
    alphabet_a = 0x61
    alphabet_z = 0x7A
    bracket_bra = 0x7B
    tilda = 0x7E
    delete = 0x7F
    ideographic_space = 0x3000
    postal_mark_face = 0x3020
    wavy_dash = 0x3030
    ideographic_half_fill_space = 0x303F
    greece_Alpha = 0x0391
    greece_Rho = 0x30A1
    greece_Sigma = 0x30A3
    greece_Omega = 0x03A9
    greece_alpha = 0x03B1
    greece_omega = 0x03C9
    cyrillic_A = 0x0410
    cyrillic_E = 0x0401
    cyrillic_e = 0x0451
    cyrillic_ya = 0x044F
    zenkaku_exc_mark = 0xFF01
    zenkaku_slash_mark = 0xFF0F
    zenkaku_number_zero = 0xFF10
    zenkaku_number_nine = 0xFF1A
    zenkaku_A = 0xFF21
    zenkaku_a = 0xFF41
    zenkaku_z = 0xFF5A
    endmark = [ord(a) for a in [")", "]", "!", ",", ".", u"\u3001", u"\u3002"]]


Ch = Ch()  # type: ignore


def main():
    unidicz = root_dir / "src" / "data" / "unidic" / "lex.7z"
    target = root_dir / "src" / "data" / "unidict.utf8"
    generator = GenUnidict(unidicz)
    generator.generate(target)
    return 0

if __name__ == "__main__":
    sys.exit(main())
