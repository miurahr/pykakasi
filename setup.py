#!/usr/bin/python
# derivered from unihandecode setup.py

from setuptools import Command,setup

import unittest
import os
import nose

class GenKanwa(Command):
    user_options = [ ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def genDict(self, src_f, pkl_f):
        import genkanwadict
        kanwa = genkanwadict.mkkanwa()
        src = os.path.join('data',src_f)
        dst = os.path.join('pykakasi',pkl_f)
        try:
            os.unlink(dst)
        except:
            pass
        kanwa.mkdict(src, dst)

    def run(self):
        import genkanwadict

        DICTS = [
            ('itaijidict.utf8', 'itaijidict2.pickle'),
            ('hepburndict.utf8', 'hepburndict2.pickle'),
            ('kunreidict.utf8', 'kunreidict2.pickle')
        ]
        for (s,p) in DICTS:
            self.genDict(s, p)

        src = os.path.join('data','kakasidict.utf8')        
        dst = os.path.join('pykakasi','kanwadict2.db')
        try:
            os.unlink(dst)
        except:
            pass
        kanwa = genkanwadict.mkkanwa()
        kanwa.run(src, dst)

setup(name='pykakasi',
      version='0.01',
      description='Python implementation of kakasi - kana kanji simple inversion library',
      url='http://github.com/miurahr/pykakasi',
      license='GPLv3',
      long_description="",
      author='Hioshi Miura',
      author_email='miurahr@linux.com',
      packages = [ 'pykakasi' ],
      provides = [ 'pykakasi' ],
      include_package_data = True,
      test_suite = 'nose.collector',
      cmdclass = { 'genkanwa':GenKanwa }
)
