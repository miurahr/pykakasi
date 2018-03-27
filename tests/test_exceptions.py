# -*- coding: utf-8 -*-
import unittest
import pykakasi
from pykakasi.exceptions import UnsupportedRomanRulesException

class TestPyKakasiExceptions(unittest.TestCase):

    def test_kakasi_unknown_rule(self):
        with self.assertRaises(UnsupportedRomanRulesException):
            kakasi = pykakasi.kakasi()
            kakasi.setMode("H","a")
            kakasi.setMode("K","a")
            kakasi.setMode("J","a")
            kakasi.setMode("r","hogefuga")
