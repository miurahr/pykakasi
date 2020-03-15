import codecs
import os
import re
from typing import Dict, Tuple

from klepto.archives import file_archive  # type: ignore # noqa

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Genkanwadict(object):
    records = {}  # type: Dict[str, Tuple[str, str]]

    ESCAPE_SEQUENCE_RE = re.compile(r'''
        ( \\U........      # 8-digit hex escapes
        | \\u....          # 4-digit hex escapes
        | \\x..            # 2-digit hex escapes
        | \\[0-7]{1,3}     # Octal escapes
        | \\N\{[^}]+\}     # Unicode characters by name
        | \\[\\'"abfnrtv]  # Single-character escapes
        )''', re.UNICODE | re.VERBOSE)

    def decode_escapes(self, s):
        def decode_match(match):
            return codecs.decode(match.group(0), 'unicode-escape')
        return self.ESCAPE_SEQUENCE_RE.sub(decode_match, s)

    def run(self, src, dst):
        with open(src, 'rb') as f:
            for line in f:
                self.parsekdict(line.decode("utf-8"))
            f.close()
        self.kanwaout(dst)

    # for itaiji and kana dict

    def mkdict(self, src, dst):
        max_key_len = 0
        dic = {}
        with open(src, "rb") as f:
            for line in f:
                line = line.decode("utf-8").strip()
                if line.startswith(';;'):  # skip comment
                    continue
                if re.match(r"^$", line):
                    continue
                try:
                    (v, k) = self.decode_escapes(line).split(' ')
                    dic[k] = v
                    max_key_len = max(max_key_len, len(k))
                except ValueError:
                    raise Exception("Cannot process dictionary line: ", line)
        d = file_archive(dst, dic, serialized=True)
        d['_max_key_len_'] = max_key_len
        d.dump()

    # for kanwadict

    def parsekdict(self, line):
        line = line.strip()
        if line.startswith(';;'):  # skip comment
            return
        (yomi, kanji) = line.split(' ')
        if ord(yomi[-1:]) <= ord('z'):
            tail = yomi[-1:]
            yomi = yomi[:-1]
        else:
            tail = ''
        self.updaterec(kanji, yomi, tail)

    def updaterec(self, kanji, yomi, tail):
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
        dic = file_archive(out, self.records, serialized=True)
        dic.dump()

    def generate_dictionaries(self, dstdir):
        DICTS = [
            ('itaijidict.utf8', 'itaijidict3.db'),
            ('hepburndict.utf8', 'hepburndict3.db'),
            ('kunreidict.utf8', 'kunreidict3.db'),
            ('passportdict.utf8', 'passportdict3.db'),
            ('hepburnhira.utf8', 'hepburnhira3.db'),
            ('kunreihira.utf8', 'kunreihira3.db'),
            ('passporthira.utf8', 'passporthira3.db')
        ]
        srcdir = os.path.join(root_dir, 'src', 'data')
        if not os.path.exists(dstdir):
            os.makedirs(dstdir)
        for (src_f, pkl_f) in DICTS:
            src = os.path.join(srcdir, src_f)
            dst = os.path.join(dstdir, pkl_f)
            if (os.path.exists(dst)):
                os.unlink(dst)
            self.mkdict(src, dst)
        src = os.path.join(srcdir, 'kakasidict.utf8')
        dst = os.path.join(dstdir, 'kanwadict4.db')
        if (os.path.exists(dst)):
            os.unlink(dst)
        self.run(src, dst)
