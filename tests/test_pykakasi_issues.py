# -*- coding: utf-8 -*-

import unittest
import pykakasi


class TestPyKakasiIssues(unittest.TestCase):

    def test_kakasi_issues60(self):

        TESTS = [
            (u"市立", u"しりつ")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H", None)
        kakasi.setMode("K", None)
        kakasi.setMode("J", "H")
        kakasi.setMode("s", False)
        kakasi.setMode("C", True)
        kakasi.setMode("E", None)
        kakasi.setMode("a", None)
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)

    def test_kakasi_issues59(self):

        TESTS = [
            (u"じゃーん", u"じゃーん"),
            (u"ヷヸヹヺ", u"ヷヸヹヺ")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H", None)
        kakasi.setMode("K", "H")
        kakasi.setMode("J", None)
        kakasi.setMode("s", False)
        kakasi.setMode("C", True)
        kakasi.setMode("E", None)
        kakasi.setMode("a", None)
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)
