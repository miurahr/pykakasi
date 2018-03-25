#!/usr/bin/env python
from zlib import compress
import re
from marshal import dumps
try:
    from cPickle import dump
except:
    from pickle import dump
try:
    import anydbm as dbm
except:
    import dbm

class mkkanwa(object):

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
        for line in open(src, "rb"):
            line = line.decode("utf-8").strip()
            if line.startswith(';;'): # skip comment
                continue
            if re.match(r"^$",line):
                continue
            try:
                (v, k) = (re.sub(r'\\u([0-9a-fA-F]{4})',
                          lambda x:unichr(int(x.group(1),16)), line)).split(' ')
                dic[k] = v
                max_key_len = max(max_key_len, len(k))
            except:
                raise Exception("Cannot process dictionary line: ", line)
        dump((dic, max_key_len), open(dst, 'wb'), protocol=2)

# for kanwadict

    def parsekdict(self, line):
        line = line.strip()
        if line.startswith(';;'): # skip comment
            return
        (yomi, kanji) = line.split(' ')
        if ord(yomi[-1:]) <= ord('z'): 
            tail = yomi[-1:]
            yomi = yomi[:-1]
        else:
            tail = ''
        self.updaterec(kanji, yomi, tail)

    def updaterec(self, kanji, yomi, tail):
            key = "%04x"%ord(kanji[0]) 
            if key in self.records:
                if kanji in self.records[key]:
                    rec = self.records[key][kanji]
                    rec.append((yomi,tail))
                    self.records[key].update( {kanji: rec} )
                else:
                    self.records[key][kanji]=[(yomi, tail)]
            else:
                self.records[key] = {}
                self.records[key][kanji]=[(yomi, tail)]

    def kanwaout(self, out):
        dic = dbm.open(out, 'c')
        for (k, v) in self.records.items():
            dic[k] = compress(dumps(v))
        dic.close()
