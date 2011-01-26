# -*- coding: utf-8 -*-
import unittest

class TestPyKakasi(unittest.TestCase):

    def test_J2H(self):
        import pykakasi

        TESTS = [
            (u"構成",         (u"こうせい",2)),
            (u"好き",          (u"すき",2)),
            (u"大きい",       (u"おおき",2)),
            (u"i大きい",      ("",0)),
        ]

        j = pykakasi.J2H()
        for case, result in TESTS:
            self.failUnlessEqual(j.convert(case), result)

    def test_H2a(self):
        import pykakasi

        TESTS = [
            (u"かんたん",   ("ka", 1)),
        ]

        h = pykakasi.H2a()
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)
