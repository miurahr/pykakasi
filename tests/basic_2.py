# -*- coding: utf-8 -*-
import unittest

class TestPyKakasi(unittest.TestCase):

    def test_J2H(self):
        import pykakasi

        TESTS = [
            (u"構成",         (u"こうせい",2,False)),
            (u"好き",          (u"すき",2,False)),
            (u"大きい",       (u"おおき",2,False)),
        ]

        j = pykakasi.J2H()
        for case, result in TESTS:
            self.failUnlessEqual(j.convert(case), result)


