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

.. image:: https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg
   :target: https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md


``pykakasi`` is a Python Natural Language Processing (NLP) library to transliterate *hiragana*, *katakana* and *kanji* (Japanese text) into *rōmaji* (Latin/Roman alphabet). It can handle characters in NFC form.

Its algorithms are based on the `kakasi`_ library, which is written in C.

* Install (from `PyPI`_): ``pip install pykakasi``
* Install (from `conda-forge`_): ``conda install -c conda-forge pykakasi``
* `Documentation available on readthedocs`_

.. _`PyPI`: https://pypi.org/project/pykakasi/
.. _`conda-forge`: https://github.com/conda-forge/pykakasi-feedstock
.. _`kakasi`: http://kakasi.namazu.org/
.. _`Documentation available on readthedocs`: https://pykakasi.readthedocs.io/en/latest/index.html


Supported python versions
=========================

* pykakasi supports python 3.8, 3.9, 3.10, 3.11, 3.12, 3.13 and pypy3

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




Copyright and License
=====================

PyKakasi::
    Copyright (C) 2010-2024 Hiroshi Miura and contributors(see AUTHORS)

KAKASI Dictionary::
    Copyright (C) 2010-2021 Hiroshi Miura and contributors(see AUTHORS)

    Copyright (C) 1992 1993 1994 Hironobu Takahashi, Masahiko Sato,
    Yukiyoshi Kameyama, Miki Inooka, Akihiko Sasaki, Dai Ando, Junichi Okukawa,
    Katsushi Sato and Nobuhiro Yamagishi

UniDic::
    Copyright (c) 2011-2021, The UniDic Consortium

    All rights reserved.

    Unidic is released under any of the GPL2, the LGPL2.1,
    or the 3-clause BSD License. (See src/data/unidic/BSD.txt)
    PyKakasi relicenses a part of the unidic with GPL3+.

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
