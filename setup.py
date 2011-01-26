#!/usr/bin/python
# derivered from unidecode setup.py

from setuptools import Command,setup

import unittest
import os

UNITTESTS = [
        "tests", 
    ]

class TestCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        suite = unittest.TestSuite()

        suite.addTests( 
            unittest.defaultTestLoader.loadTestsFromNames( 
                                UNITTESTS ) )

        result = unittest.TextTestRunner(verbosity=2).run(suite)

setup(name='pykakasi',
      version='0.01',
      description='',
      url='http://launchpad.net/miurahr/+junk/pykakasi',
      license='GPLv3',
      long_description="",
      author='Hioshi Miura',
      author_email='miurahr@linux.com',

      packages = [ 'pykakasi' ],

      provides = [ 'pykakasi' ],

      cmdclass = { 'test': TestCommand }
)
