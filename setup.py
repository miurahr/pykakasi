#!/usr/bin/env python

import io
import os
import shutil
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py

import pykakasi.genkanwadict as genkanwadict


def readme():
    with io.open(os.path.join(os.path.dirname(__file__),'README.rst'), mode="r", encoding="UTF-8") as f:
        return f.read()

class MyBuild(build_py):

    def generate_dictionaries(self):
        DICTS = [
            ('itaijidict.utf8', 'itaijidict2.pickle'),
            ('hepburndict.utf8', 'hepburndict2.pickle'),
            ('kunreidict.utf8', 'kunreidict2.pickle'),
            ('passportdict.utf8', 'passportdict2.pickle'),
            ('hepburnhira.utf8', 'hepburnhira2.pickle'),
            ('kunreihira.utf8', 'kunreihira2.pickle'),
            ('passporthira.utf8', 'passporthira2.pickle')
        ]
        kanwa = genkanwadict.mkkanwa()
        for (src_f,pkl_f) in DICTS:
            src = os.path.join('pykakasi', 'data', src_f)
            dst = os.path.join(os.path.join(self.build_lib, 'pykakasi'), pkl_f)
            if (os.path.exists(dst)):
                os.unlink(dst)
            kanwa.mkdict(src, dst)
        src = os.path.join('pykakasi','data','kakasidict.utf8')
        dst = os.path.join(os.path.join(self.build_lib, 'pykakasi'),'kanwadict3.db')
        if (os.path.exists(dst)):
            shutil.rmtree(dst)
        kanwa.run(src, dst)

    def run(self):
        build_py.run(self)
        if not self.dry_run:
            self.generate_dictionaries()


setup(name='pykakasi',
      version='0.94',
      description='Python implementation of kakasi - kana kanji simple inversion library',
      url='http://github.com/miurahr/pykakasi',
      license='GPLv3',
      long_description=readme(),
      author='Hioshi Miura',
      author_email='miurahr@linux.com',
      packages = [ 'pykakasi', 'pykakasi.genkanwadict' ],
      provides = [ 'pykakasi' ],
      scripts = ["kakasi"],
      include_package_data = True,
      package_data = {'pykakasi':  ['*.pickle'],
                      'pykakasi/kanwadict3.db': ['data']},
      test_suite = 'nose.collector',
      tests_require = ['nose','coverage','mock'],
      install_requires=['six','semidbm'],
      cmdclass={'build_py': MyBuild}
)
