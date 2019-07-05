#!/usr/bin/env python

import io
import os
import re
import sys

from setuptools import setup
from setuptools.command.build_py import build_py

package_name = "pykakasi"
root_dir = os.path.abspath(os.path.dirname(__file__))


class MyBuild(build_py):

    def run(self):
        build_py.run(self)
        sys.path.insert(1, os.path.join(root_dir, 'src'))
        from kakasidict import Genkanwadict
        if not self.dry_run:
            kanwa = Genkanwadict()
            dstdir = os.path.join(self.build_lib, 'pykakasi', 'data')
            kanwa.generate_dictionaries(dstdir)


def readme():
    with io.open(os.path.join(root_dir, 'README.rst'), mode="r", encoding="UTF-8") as f:
        return f.read()


with open(os.path.join(root_dir, 'src', package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    license = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

assert version
assert license
assert author
assert author_email
assert url


setup(name=package_name,
      version=version,
      description='Python implementation of kakasi - kana kanji simple inversion library',
      url=url,
      license=license,
      long_description=readme(),
      author=author,
      author_email=author_email,
      package_dir={'pykakasi': 'src/pykakasi'},
      packages=[package_name],
      provides=[package_name],
      scripts=["bin/kakasi"],
      include_package_data=True,
      package_data={'src/data': ['*.utf8']},
      tests_require=['pytest', 'coverage'],
      setup_requires=['six', 'klepto'],
      install_requires=['six', 'klepto'],
      extras_require={'dev': ['pytest']},
      cmdclass={'build_py': MyBuild},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development :: Libraries :: Python Modules']
      )
