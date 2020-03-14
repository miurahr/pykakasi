#!/usr/bin/env python
import os
import sys

from setuptools import setup
from setuptools.command.build_py import build_py


class MyBuild(build_py):

    def run(self):
        build_py.run(self)

        root_dir = os.path.abspath(os.path.dirname(__file__))
        sys.path.insert(1, os.path.join(root_dir, 'src'))

        from kakasidict import Genkanwadict
        if not self.dry_run:
            kanwa = Genkanwadict()
            dstdir = os.path.join(self.build_lib, 'pykakasi', 'data')
            kanwa.generate_dictionaries(dstdir)


setup(cmdclass={'build_py': MyBuild},
      use_scm_version={"local_scheme": "no-local-version"},
      setup_requires=['setuptools-scm>=3.5.0', 'setuptools>=42'])
