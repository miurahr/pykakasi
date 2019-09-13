import os
import re

from klepto.archives import file_archive
from six import unichr

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Genkanwadict(object):
    records = {}

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
                    (v, k) = (re.sub(r'\\u([0-9a-fA-F]{4})',
                                     lambda x: unichr(int(x.group(1), 16)), line)).split(' ')
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
