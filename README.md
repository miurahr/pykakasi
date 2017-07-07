Pykakasi library
==================

[![Join the chat at https://gitter.im/miurahr/pykakasi](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/miurahr/pykakasi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

 [![travis-ci](https://secure.travis-ci.org/miurahr/pykakasi.png)](https://secure.travis-ci.org/miurahr/pykakasi)
 [![PyPI version](https://badge.fury.io/py/pykakasi.png)](http://badge.fury.io/py/Pykakasi)
 [![Coverage Status](https://coveralls.io/repos/miurahr/pykakasi/badge.svg?branch=master)](https://coveralls.io/r/miurahr/pykakasi?branch=master)

pykakasi is re-imprelemtation of kakasi library by Python.

How To Use pykakasi
------------------

```python
    from pykakasi import kakasi,wakati

    kakasi = kakasi()
    kakasi.setMode("H","a") # default: Hiragana no conversion
    kakasi.setMode("K","a") # default: Katakana no conversion
    kakasi.setMode("J","a") # default: Japanese no conversion
    kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
    kakasi.setMode("C", True) # add space default: no Separator
    kakasi.setMode("c", False) # capitalize default: no Capitalize
    conv = kakasi.getConverter()
    result = conv.do(text)

    wakati = wakati()
    conv = wakati.getConverter()
    result = conv.do(text)
```

You can use output `Mode` values from "h", "k", "a" which is each means
"Hiragana", "Katakana" and "Alphabet".
For input, you can use "J" that means "Japanese" that is
mixture of Kanji, Katakana and Hiragana.
Also there is values of "H", "K" that means "Hiragana", and "Katakana".
You can use  "Hepburn", "Kunrei" or "Passport" as mode "r", Roman table switch.
Also "s" used for separator switch, "C" for capitalize switch.
"S" for separator string option.

`wakati` is an implementation of kakasi's wakati gaki option.

Options
-------------------

These switch alphabets are derived from original Kakasi.
Now it support following options:

| Option | Description         | Values     | Note                        |
| ------ | :----------         | --------   | :----------                 |
| K      | Katakana convertion | a,H,None   | roman or noconversion       |
| H      | Hiragana convertion | a,K,None   | roman or noconversion       |
| J      | Kanji conversion    | a,H,K,None | roman or Hiragana, Katakana |
| E      | Eigou convesion     | a,None     | roman or noconversion       |

Each character means character sets as follows:

```
  Character Sets:
       a: ascii  j: jisroman  g: graphic  k: kana 
       (j,k     defined in jisx0201)
       E: kigou  K: katakana  H: hiragana J: kanji
       (E,K,H,J defined in jisx0208)
```
