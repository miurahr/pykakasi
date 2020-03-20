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

.. image:: https://travis-ci.org/miurahr/pykakasi.svg?branch=master
   :target: https://travis-ci.org/miurahr/pykakasi
   :alt: Travis-CI

.. image:: https://dev.azure.com/miurahr/github/_apis/build/status/miurahr.pykakasi?branchName=master
   :target: https://dev.azure.com/miurahr/github/_build?definitionId=13&branchName=master
   :alt: Azure-Pipelines

.. image:: https://coveralls.io/repos/miurahr/pykakasi/badge.svg?branch=master
   :target: https://coveralls.io/r/miurahr/pykakasi?branch=master
   :alt: Coverage status


``pykakasi`` is a Python Natural Language Processing (NLP) library to transliterate *hiragana*, *katakana* and *kanji* (Japanese text) into *rōmaji* (Latin/Roman alphabet).

It is based on the `kakasi`_ library, which is written in C.

* Install (from `PyPI`_): ``pip install pykakasi``
* `Documentation available on readthedocs`_

.. _`PyPI`: https://pypi.org/project/pykakasi/
.. _`kakasi`: http://kakasi.namazu.org/
.. _`Documentation available on readthedocs`: https://pykakasi.readthedocs.io/en/latest/index.html


Supported python versions
=========================

* pykakasi 1.2 supports python 2.7, python 3.5, 3.6, 3.7

* pykakasi 2.0 supports python 3.6, 3.7, 3.8, pypy3.6-7.1.1

Usage
=====

Here is an usage of NewAPI for pykakasi v2.0.0 and later.
Transliterate Japanese text to kana, hiragana and romaji:

.. code-block:: pycon

    import pykakasi
    kks = pykakasi.kakasi()
    text = "かな漢字"
    result = kks.convert(text)
    for item in result:
        print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))

    かな: kana 'カナ', hiragana: 'かな', romaji: 'kana'
    漢字: kana 'カンジ', hiragana: 'かんじ', romaji: 'kanji'


Here is an example that output as similar with furigana mode.

.. code-block:: pycon

    import pykakasi
    kks = pykakasi.kakasi()
    text = "かな漢字交じり文"
    result = kks.convert(text)
    for item in result:
        print("{}[{}] ".format(item['orig'], item['hepburn'].capitalize()), end='')
    print()

    かな[Kana] 漢字[Kanji] 交じり[Majiri] 文[Bun]


Old API
=======

There is also an old API for v1.2.

Transliterate Japanese text to rōmaji:

.. code-block:: pycon

    >>> import pykakasi
    >>>
    >>> text = u"かな漢字交じり文"
    >>> kakasi = pykakasi.kakasi()
    >>> kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
    >>> kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
    >>> kakasi.setMode("J","a") # Japanese to ascii, default: no conversion
    >>> kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
    >>> kakasi.setMode("s", True) # add space, default: no separator
    >>> kakasi.setMode("C", True) # capitalize, default: no capitalize
    >>> conv = kakasi.getConverter()
    >>> result = conv.do(text)
    >>> print(result)
    kana Kanji Majiri Bun

Tokenize Japanese text (split by word boundaries), equivalent to ``kakasi``'s wakati gaki option:

.. code-block:: pycon

    >>> wakati = pykakasi.wakati()
    >>> conv = wakati.getConverter()
    >>> result = conv.do(text)
    >>> print(result)
    かな 漢字 交じり 文

Add `furigana`_ (pronounciation aid) in rōmaji to text:

.. code-block:: pycon

    >>> kakasi = pykakasi.kakasi()
    >>> kakasi.setMode("J","aF") # Japanese to furigana
    >>> kakasi.setMode("H","aF") # Japanese to furigana
    >>> conv = kakasi.getConverter()
    >>> result = conv.do(text)
    >>> print(result)
    かな[kana] 漢字[Kanji] 交じり[Majiri] 文[Bun]

Input mode values: "J" (Japanese: kanji, hiragana and katakana), "H" (hiragana), "K" (katakana).

Output mode values: "H" (hiragana), "K" (katakana), "a" (alphabet / rōmaji), "aF" (furigana in rōmaji).

There are other ``setMode`` switches which control output:

* "r": Romanisation table: `Hepburn`_ (default), `Kunrei`_ or ``Passport``
* "s": Separator: ``False`` adds no spaces between words (default), ``True`` adds spaces between words
* "C": Capitalize: ``False`` adds no capital letters (default), ``True`` makes each word start with a capital letter

.. _`furigana`: https://en.wikipedia.org/wiki/Furigana
.. _`Hepburn`: https://en.wikipedia.org/wiki/Hepburn_romanization
.. _`Kunrei`: https://en.wikipedia.org/wiki/Kunrei-shiki_romanization

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

