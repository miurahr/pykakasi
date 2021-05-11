import codecs
import os
import pickle
import re
import shutil
import tempfile
from typing import Dict, List, Optional, Tuple, Union

import py7zr  # type: ignore  # noqa

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Genkanwadict:

    ESCAPE_SEQUENCE_RE = re.compile(
        r"""
        ( \\U........      # 8-digit hex escapes
        | \\u....          # 4-digit hex escapes
        | \\x..            # 2-digit hex escapes
        | \\[0-7]{1,3}     # Octal escapes
        | \\N\{[^}]+\}     # Unicode characters by name
        | \\[\\'"abfnrtv]  # Single-character escapes
        )""",
        re.UNICODE | re.VERBOSE,
    )

    def decode_escapes(self, s: str) -> str:
        def decode_match(match):
            return codecs.decode(match.group(0), "unicode-escape")

        return self.ESCAPE_SEQUENCE_RE.sub(decode_match, s)

    # for kana dict

    def mkdict(self, src: str, dst: str):
        max_key_len = 0
        dic: Dict[str, Union[str, int]] = {}
        with open(src, "r", encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if line.startswith(";;"):  # skip comment
                    continue
                if re.match(r"^$", line):
                    continue
                try:
                    (v, k) = self.decode_escapes(line).split(" ")
                    dic[k] = v
                    max_key_len = max(max_key_len, len(k))
                except ValueError:
                    raise Exception("Cannot process dictionary line: ", line)
        dic["_max_key_len_"] = max_key_len
        with open(dst, "wb") as o:
            pickle.dump(dic, o)

    def maketrans(self, src, dst):
        dict: Dict[str, Optional[str]] = {}
        with open(src, "r", encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if line.startswith(";;"):  # skip commnet
                    continue
                if re.match(r"^$", line):
                    continue
                try:
                    (v, k) = self.decode_escapes(line).split(" ")
                    dict[ord(k)] = v
                except ValueError:
                    raise Exception("Cannot process dictionary line: ", line)
        for i in range(0xFE00, 0xFE02):
            dict[i] = None
        for i in range(0xE0100, 0xE01EF):
            dict[i] = None
        with open(dst, "wb") as f:
            pickle.dump(dict, f)

    # for kanwadict

    def _makekanwa(self, src: str, unidicz, dst: str):
        self.records: Dict[str, Dict[str, List[Tuple[str, ...]]]] = {}
        with open(src, "r", encoding="utf-8") as f:
            for line in f:
                self._parse_kakasi_dict(line.strip())
            f.close()
        unidic = tempfile.mkdtemp()
        with py7zr.SevenZipFile(unidicz, "r") as u:
            u.extractall(path=unidic)
        with open(os.path.join(unidic, "lex_3_1.csv"), "r", encoding="utf-8") as f:
            for line in f:
                self._parse_unidic(line.strip())
        shutil.rmtree(unidic)
        self.kanwaout(dst)

    def _parse_kakasi_dict(self, line: str) -> None:
        if line.startswith(";;"):  # skip comment
            return
        (yomi, kanji) = line.split(" ")
        if ord(yomi[-1:]) <= ord("z"):
            tail = yomi[-1:]
            yomi = yomi[:-1]
        else:
            tail = ""
        self._updaterec(kanji, yomi, tail)

    def _parse_unidic(self, line: str) -> None:
        token = line.split(",")
        key = token[0]
        yomi = token[10]
        role = token[4]
        if role not in ["名詞"]:
            return
        if not self._is_kanji(key):
            return
        hira = self._k2h(yomi)
        self._updaterec(key, hira, "")

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

    def _updaterec(self, kanji: str, yomi, tail) -> None:
        key = "%04x" % ord(kanji[0])
        if key in self.records:
            if kanji in self.records[key]:
                rec = self.records[key][kanji]
                rec.append((yomi, tail))
                self.records[key].update({kanji: rec})
            else:
                self.records[key][kanji] = [(yomi, tail)]
        else:
            self.records[key] = {}
            self.records[key][kanji] = [(yomi, tail)]

    def kanwaout(self, out):
        with open(out, "wb") as f:
            pickle.dump(self.records, f, protocol=4)

    def generate_dictionaries(self, dstdir):
        DICTS = [
            ("hepburndict.utf8", "hepburndict3.db"),
            ("kunreidict.utf8", "kunreidict3.db"),
            ("passportdict.utf8", "passportdict3.db"),
            ("hepburnhira.utf8", "hepburnhira3.db"),
            ("kunreihira.utf8", "kunreihira3.db"),
            ("passporthira.utf8", "passporthira3.db"),
            ("halfkana.utf8", "halfkana3.db"),
        ]
        srcdir = os.path.join(root_dir, "src", "data")
        if not os.path.exists(dstdir):
            os.makedirs(dstdir)
        for (src_f, pkl_f) in DICTS:
            src = os.path.join(srcdir, src_f)
            dst = os.path.join(dstdir, pkl_f)
            if os.path.exists(dst):
                os.unlink(dst)
            self.mkdict(src, dst)

        src = os.path.join(srcdir, "itaijidict.utf8")
        dst = os.path.join(dstdir, "itaijidict4.db")
        if os.path.exists(dst):
            os.unlink(dst)
        self.maketrans(src, dst)

        src = os.path.join(srcdir, "kakasidict.utf8")
        unidic = os.path.join(srcdir, "unidic", "lex.7z")
        dst = os.path.join(dstdir, "kanwadict4.db")
        if os.path.exists(dst):
            os.unlink(dst)
        self._makekanwa(src, unidic, dst)


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
