========
Pykakasi
========

Overview
========

.. image:: https://readthedocs.org/projects/pykakasi/badge/?version=latest
   :target: https://pykakasi.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://badge.fury.io/py/pykakasi.png
   :target: http://badge.fury.io/py/Pykakasi
   :alt: PyPI version

.. image:: https://github.com/miurahr/pykakasi/workflows/Run%20Tox%20tests/badge.svg
   :target: https://github.com/miurahr/pykakasi/actions?query=workflow%3A%22Run+Tox+tests%22
   :alt: Run Tox tests

.. image:: https://dev.azure.com/miurahr/github/_apis/build/status/miurahr.pykakasi?branchName=master
   :target: https://dev.azure.com/miurahr/github/_build?definitionId=13&branchName=master
   :alt: Azure-Pipelines

.. image:: https://coveralls.io/repos/miurahr/pykakasi/badge.svg?branch=master
   :target: https://coveralls.io/r/miurahr/pykakasi?branch=master
   :alt: Coverage status


``pykakasi`` is a Python Natural Language Processing (NLP) library to transliterate *hiragana*, *katakana* and *kanji* (Japanese text) into *rōmaji* (Latin/Roman alphabet). It can handle characters in NFC form.

Its algorithms are based on the `kakasi`_ library, which is written in C.

* Install (from `PyPI`_): ``pip install pykakasi``
* `Documentation available on readthedocs`_

.. _`PyPI`: https://pypi.org/project/pykakasi/
.. _`kakasi`: http://kakasi.namazu.org/
.. _`Documentation available on readthedocs`: https://pykakasi.readthedocs.io/en/latest/index.html


Supported python versions
=========================

* pykakasi supports python 3.6, 3.7, 3.8, 3.9, and pypy3

Usage
=====

Transliterate Japanese text to kana, hiragana and romaji:

.. code-block:: python

    import pykakasi
    kks = pykakasi.kakasi()
    text = "かな漢字"
    result = kks.convert(text)
    for item in result:
        print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))

    かな: kana 'カナ', hiragana: 'かな', romaji: 'kana'
    漢字: kana 'カンジ', hiragana: 'かんじ', romaji: 'kanji'


Here is an example that output as similar with furigana mode.

.. code-block:: python

    import pykakasi
    kks = pykakasi.kakasi()
    text = "かな漢字交じり文"
    result = kks.convert(text)
    for item in result:
        print("{}[{}] ".format(item['orig'], item['hepburn'].capitalize()), end='')
    print()

    かな[Kana] 漢字[Kanji] 交じり[Majiri] 文[Bun]


Benchmark result
================

You can see benchmark result on various versions and platforms at https://github.com/miurahr/pykakasi/issues/123


Copyright and License
=====================

Copyright 2010-2020 Hiroshi Miura <miurahr@linux.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

