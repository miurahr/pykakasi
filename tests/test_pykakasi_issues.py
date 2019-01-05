# -*- coding: utf-8 -*-
import unittest
import pykakasi

class TestPyKakasiIssues(unittest.TestCase):

    def test_kakasi_issues(self):

        TESTS = [
            (60, u"市立", u"しりつ")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H",None)
        kakasi.setMode("K",None)
        kakasi.setMode("J","H")
        kakasi.setMode("s",False)
        kakasi.setMode("C",True)
        kakasi.setMode("E",None)
        kakasi.setMode("a",None)
        converter  = kakasi.getConverter()
        for issue, case, result in TESTS:
            self.assertEqual(converter.do(case), result)

