# -*- coding: utf-8 -*-
import unittest
import pykakasi
from pykakasi.exceptions import UnsupportedRomanRulesException, InvalidModeValueException, InvalidFlagValueException

class TestPyKakasiExceptions(unittest.TestCase):

    def test_kakasi_unknown_rule(self):
        with self.assertRaises(UnsupportedRomanRulesException):
            kakasi = pykakasi.kakasi()
            kakasi.setMode("H","a")
            kakasi.setMode("K","a")
            kakasi.setMode("J","a")
            kakasi.setMode("r","hogefuga")

    def test_kakasi_unknown_mode(self):
        with self.assertRaises(InvalidModeValueException):
            kakasi = pykakasi.kakasi()
            kakasi.setMode("H","a")
            kakasi.setMode("K","a")
            kakasi.setMode("J","X")

    def test_kakasi_invalid_flag_value(self):
        with self.assertRaises(InvalidFlagValueException):
            kakasi = pykakasi.kakasi()
            kakasi.setMode("H","a")
            kakasi.setMode("K","a")
            kakasi.setMode("s","yes")
