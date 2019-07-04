import os
import sys

import pytest

root_dir = os.path.dirname(__file__)
sys.path.insert(1, os.path.join(root_dir, 'src'))

from pykakasi.properties import Configurations

import kakasidict

@pytest.fixture(scope="session", autouse=True)
def dictionary_setup_fixture():
    dpath = os.path.join(root_dir, 'build', 'lib', 'pykakasi', 'data')
    kanwa = kakasidict.Genkanwadict()
    kanwa.generate_dictionaries(dpath)
    Configurations().data_path = dpath
    yield
