Pykakasi library
==================

 [![travis-ci](https://secure.travis-ci.org/miurahr/pykakasi.png)](https://secure.travis-ci.org/miurahr/pykakasi)
 [![PyPI version](https://badge.fury.io/py/pykakasi.png)](http://badge.fury.io/py/Pykakasi)

pykakasi is re-imprelemtation of kakasi library by Python.

How To Use pykakasi
------------------

```python
    from pykakasi import kakasi,wakati

    kakasi = kakasi()
    kakasi.setMode("H","a") # default: Hiragana -> Roman
    kakasi.setMode("K","a") # default: Katakana -> Roman
    kakasi.setMode("J","a") # default: Japanese -> Roman
    kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
    kakasi.setMode("C", true) # default: Separator
    kakasi.setMode("c", false) # default: no Capitalize
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
You can use  "Hepburn" or "Kunrei" as mode "r", Roman table switch.
Also "C" used for separator switch, "c" for capitalize switch.

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

Each character means character sets as follows:

```
  Character Sets:
       a: ascii  j: jisroman  g: graphic  k: kana 
       (j,k     defined in jisx0201)
       E: kigou  K: katakana  H: hiragana J: kanji
       (E,K,H,J defined in jisx0208)
```
