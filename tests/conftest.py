import os
import sys

import pytest


@pytest.fixture(scope="session", autouse=True)
def dictionary_setup_fixture():
    root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    if "TOX_ENV_DIR" not in os.environ:
        sys.path.insert(1, os.path.join(root_dir, 'src'))
        import kakasidict
        from pykakasi.properties import Configurations
        dpath = os.path.join(root_dir, 'build', 'lib', 'pykakasi', 'data')
        print("Generating kanwa dictionary in %s\n" % dpath)
        kanwa = kakasidict.Genkanwadict()
        kanwa.generate_dictionaries(dpath)
        Configurations().data_path = dpath
