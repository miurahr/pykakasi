========
Pykakasi
========


Overview
========

.. image:: https://travis-ci.org/miurahr/pykakasi.svg?branch=master
   :target: https://travis-ci.org/miurahr/pykakasi
   :alt: Travis-CI

.. image:: https://badge.fury.io/py/pykakasi.png
   :target: http://badge.fury.io/py/Pykakasi
   :alt: PyPI version

.. image:: https://coveralls.io/repos/miurahr/pykakasi/badge.svg?branch=master
   :target: https://coveralls.io/r/miurahr/pykakasi?branch=master
   :alt: Coverage status

.. image:: https://ci.appveyor.com/api/projects/status/mhej9bbe5jomvaj4/branch/master?svg=true
   :target: https://ci.appveyor.com/project/miurahr/pykakasi/branch/master
   :alt: Build status

pykakasi is re-implementation of kakasi library (original is written in C) in Python.

How To Use pykakasi
===================

Build and install from source(recommended)::

    pip install git+https://github.com/miurahr/pykakasi

Building library, setup script build dictionary db file and generate pickled db files.
Without dictionary files, a library fails to run.

Sample source code::

    from pykakasi import kakasi,wakati
    
    kakasi = kakasi()
    kakasi.setMode("H","a") # default: Hiragana no conversion
    kakasi.setMode("K","a") # default: Katakana no conversion
    kakasi.setMode("J","a") # default: Japanese no conversion
    kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
    kakasi.setMode("s", True) # add space default: no Separator
    kakasi.setMode("C", True) # capitalize default: no Capitalize
    conv = kakasi.getConverter()
    result = conv.do(text)
    
    wakati = wakati()
    conv = kawati.getConverter()
    result = conv.do(text)

You can use output `Mode` values from "H", "K", "a" which is each means
"Hiragana", "Katakana" and "Alphabet".
For input, you can use "J" that means "Japanese" that is
mixture of Kanji, Katakana and Hiragana.
Also there is values of "H", "K" that means "Hiragana", and "Katakana".
You can use  "Hepburn" , "Kunrei" or "Passport" as mode "r", Roman table switch.
Also "s" used for separator switch, "C" for capitalize switch.
"S" for separator storing option.

`wakati` is an implementation of kakasi's wakati gaki option.

Options
=======

These switch alphabets are derived from original Kakasi.
Now it support following options:

+--------+---------------------+------------+-----------------------------+
| Option | Description         | Values     | Note                        |
+========+=====================+============+=============================+
| K      | Katakana convertion | a,H,None   | roman or noconversion       |
+--------+---------------------+------------+-----------------------------+
| H      | Hiragana convertion | a,K,None   | roman or noconversion       |
+--------+---------------------+------------+-----------------------------+
| J      | Kanji conversion    | a,H,K,None | roman or Hiragana, Katakana |
+--------+---------------------+------------+-----------------------------+
| E      | Eigou convesion     | a,None     | roman or noconversion       |
+--------+---------------------+------------+-----------------------------+

Each character means character sets as follows::

    Character Sets
       a: ascii  j: jisroman  g: graphic  k: kana 
       (j,k     defined in jisx0201)
       E: kigou  K: katakana  H: hiragana J: kanji
       (E,K,H,J defined in jisx0208)


