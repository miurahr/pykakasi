# -*- coding: utf-8 -*-
import unittest
from j2h import J2H

class TestUnidecode(unittest.TestCase):
	def test_basic(self):

	    TESTS = [
				(u"Hello, World!", 
				"Hello, World!"),
        ]

		j = J2H()
		for case, result in TESTS:
			self.failUnlessEqual(j.convert(case), result)

