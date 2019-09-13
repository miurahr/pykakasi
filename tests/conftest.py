import os
import sys

import pytest


def pytest_addoption(parser):
    parser.addoption('--runenv', action='store', default="pytest", help='Specify tox or pytest')


@pytest.fixture(scope='session')
def runenv(request):
    return request.config.getoption('runenv')


@pytest.fixture(scope="session", autouse=True)
def dictionary_setup_fixture(runenv):
    root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    if runenv == 'pytest':
        sys.path.insert(1, os.path.join(root_dir, 'src'))
        import kakasidict
        from pykakasi.properties import Configurations
        dpath = os.path.join(root_dir, 'build', 'lib', 'pykakasi', 'data')
        print("Generating kanwa dictionary in %s\n" % dpath)
        kanwa = kakasidict.Genkanwadict()
        kanwa.generate_dictionaries(dpath)
        Configurations().data_path = dpath
    elif runenv == 'tox':
        pass
    else:
        pass
