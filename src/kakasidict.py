import codecs
import os
import pickle
import re
from typing import Dict, List, Optional, Tuple, Union

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Genkanwadict:
    records = {}  # type: Dict[str, Dict[str, List[Tuple[str, str]]]]

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

    def run(self, src: str, dst: str):
        with open(src, "r", encoding="utf-8") as f:
            for line in f:
                self.parse_kakasi_dict(line.strip())
            f.close()
        self.kanwaout(dst)

    def parse_kakasi_dict(self, line: str):
        if line.startswith(";;"):  # skip comment
            return
        token = line.split(" ")
        yomi = token[0]
        kanji = token[1]
        if ord(yomi[-1:]) <= ord("z"):
            tail = yomi[-1:]
            yomi = yomi[:-1]
        else:
            tail = ""
        if len(token) > 2:  # has context
            val = (yomi, tail) + tuple(token[2:])
        else:
            val = (yomi, tail)
        self.updaterec(kanji, val)

    def updaterec(self, kanji: str, val: Tuple[str]):
        key = "%04x" % ord(kanji[0])
        if key in self.records:
            if kanji in self.records[key]:
                rec = self.records[key][kanji]
                rec.append(val)
                self.records[key].update({kanji: rec})
            else:
                self.records[key][kanji] = [val]
        else:
            self.records[key] = {}
            self.records[key][kanji] = [val]

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
        dst = os.path.join(dstdir, "kanwadict4.db")
        if os.path.exists(dst):
            os.unlink(dst)
        self.run(src, dst)
