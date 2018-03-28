# -*- coding: utf-8 -*-
import os,sys,bz2
import unittest
from six.moves import cPickle as pickle

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
        dst = os.path.join(self.tmpdir,'test_kanwadict3.db') # FIXME:  no hardcoded filename
        self.kanwa.run(src, dst)
