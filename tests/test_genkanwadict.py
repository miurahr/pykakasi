# -*- coding: utf-8 -*-
import os,sys,bz2
from types import *
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
try: #python2
    import cPickle as pickle
except: #python3
    import pickle

import shutil
import tempfile
import pykakasi.genkanwadict as genkanwadict

class TestGenkanwadict(unittest.TestCase):
    kanwa = None
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def constructor(self):
        self.kanwa = genkanwadict.mkkanwa()
        self.assertEqual(self.kanwa, object)

    def test_mkdict(self):
        if self.kanwa is None:
            self.kanwa = genkanwadict.mkkanwa()

        src = os.path.join('tests','kanadict.utf8')
        dst = os.path.join(self.tmpdir,'test_kanadict.pickle')
        self.kanwa.mkdict(src, dst)
        # load test
        with open(dst,'rb') as f:
            (mydict, maxkeylen) = pickle.load(f)
            f.close()
        self.assertTrue(isinstance(mydict, dict))
        self.assertEqual(maxkeylen, 3)

    def test_mkkanwa(self):
        if self.kanwa is None:
            self.kanwa = genkanwadict.mkkanwa()

        src = os.path.join('tests','kakasidict.utf8')
        dst = os.path.join(self.tmpdir,'test_kanwadict2.db')
        self.kanwa.run(src, dst)
