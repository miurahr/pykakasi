#!/usr/bin/env python
# derivered from unihandecode setup.py

import os, sys, io, shutil
from setuptools import Command,setup
from setuptools.command.install import install
from distutils.command.build import build

import pykakasi.genkanwadict as genkanwadict

def gen_dict(src_f, pkl_f):
    kanwa = genkanwadict.mkkanwa()
    src = os.path.join('pykakasi', 'data', src_f)
    dst = os.path.join('pykakasi', pkl_f)
    if (os.path.exists(dst)):
        os.unlink(dst)
    kanwa.mkdict(src, dst)

def gen_kanwa(src, dst):
    if (os.path.exists(dst)):
        shutil.rmtree(dst)
    kanwa = genkanwadict.mkkanwa()
    kanwa.run(src, dst)

def readme():
    with io.open(os.path.join(os.path.dirname(__file__),'README.rst'), mode="r", encoding="UTF-8") as f:
        return f.read()

def pre_build():
    DICTS = [
        ('itaijidict.utf8', 'itaijidict2.pickle'),
        ('hepburndict.utf8', 'hepburndict2.pickle'),
        ('kunreidict.utf8', 'kunreidict2.pickle'),
        ('passportdict.utf8', 'passportdict2.pickle'),
        ('hepburnhira.utf8', 'hepburnhira2.pickle'),
        ('kunreihira.utf8', 'kunreihira2.pickle'),
        ('passporthira.utf8', 'passporthira2.pickle')
    ]
    for (s,p) in DICTS:
        gen_dict(s, p)
    src = os.path.join('pykakasi','data','kakasidict.utf8')
    dst = os.path.join('pykakasi','kanwadict3.db')
    gen_kanwa(src, dst)

class my_build(build):
    def run(self):
        self.execute(pre_build, (),
                    msg="Running pre build task")
        build.run(self)

tests_require = ['nose','coverage','mock']
if sys.version_info < (2, 7):
    tests_require.append('unittest2')

setup(name='pykakasi',
      version='0.93',
      description='Python implementation of kakasi - kana kanji simple inversion library',
      url='http://github.com/miurahr/pykakasi',
      license='GPLv3',
      long_description=readme(),
      author='Hioshi Miura',
      author_email='miurahr@linux.com',
      packages = [ 'pykakasi',
                   'pykakasi.genkanwadict'
                 ],
      provides = [ 'pykakasi' ],
      scripts = ["kakasi"],
      include_package_data = True,
      package_data = {'pykakasi':  ['*.pickle'],
                      'pykakasi/kanwadict3.db': ['data']},
      test_suite = 'nose.collector',
      tests_require = tests_require,
      install_requires=['six','semidbm'],
      cmdclass = {
          'build':my_build
        }
)
