import codecs
import os
import pickle
import re
from typing import Dict, List, Optional, Tuple, Union

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

    def _makekanwa(self, sources: List[str], dst: str):
        self.records: Dict[int, Dict[str, List[Tuple[str, ...]]]] = {}
        for src in sources:
            with open(src, "r", encoding="utf-8") as f:
                for line in f:
                    self._parse_kakasi_dict(line.strip())
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

    _cletters = {
        "a": ("あ", "ぁ", "っ", "わ", "ゎ"),
        "i": ("い", "ぃ", "っ", "ゐ"),
        "u": ("う", "ぅ", "っ"),
        "e": ("え", "ぇ", "っ", "ゑ"),
        "o": ("お", "ぉ", "っ"),
        "k": ("か", "ゕ", "き", "く", "け", "ゖ", "こ", "っ"),
        "g": ("が", "ぎ", "ぐ", "げ", "ご", "っ"),
        "s": ("さ", "し", "す", "せ", "そ", "っ"),
        "z": ("ざ", "じ", "ず", "ぜ", "ぞ", "っ"),
        "j": ("ざ", "じ", "ず", "ぜ", "ぞ", "っ"),
        "t": ("た", "ち", "つ", "て", "と", "っ"),
        "d": ("だ", "ぢ", "づ", "で", "ど", "っ"),
        "c": ("ち", "っ"),
        "n": ("な", "に", "ぬ", "ね", "の", "ん"),
        "h": ("は", "ひ", "ふ", "へ", "ほ", "っ"),
        "b": ("ば", "び", "ぶ", "べ", "ぼ", "っ"),
        "f": ("ふ", "っ"),
        "p": ("ぱ", "ぴ", "ぷ", "ぺ", "ぽ", "っ"),
        "m": ("ま", "み", "む", "め", "も"),
        "y": ("や", "ゃ", "ゆ", "ゅ", "よ", "ょ"),
        "r": ("ら", "り", "る", "れ", "ろ"),
        "l": ("ら", "り", "る", "れ", "ろ"),
        "w": ("わ", "ゐ", "ゑ", "ゎ", "を", "っ"),
        "v": ("ゔ"),
    }

    def _updaterec(self, kanji: str, yomi, tail) -> None:
        key = ord(kanji[0])
        if tail == "":
            if key in self.records:
                if kanji in self.records[key]:
                    rec = self.records[key][kanji]
                    rec.append(yomi)
                    self.records[key].update({kanji: rec})
                else:
                    self.records[key][kanji] = [yomi]
            else:
                self.records[key] = {}
                self.records[key][kanji] = [yomi]
        else:
            for c in self._cletters.get(tail, ""):
                self._updaterec(kanji + c, yomi + c, "")

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

        sources = [
            os.path.join(srcdir, "kakasidict.utf8"),
            os.path.join(srcdir, "unidict_noun.utf8"),
            os.path.join(srcdir, "unidict_adj.utf8"),
        ]
        dst = os.path.join(dstdir, "kanwadict4.db")
        if os.path.exists(dst):
            os.unlink(dst)
        self._makekanwa(sources, dst)
