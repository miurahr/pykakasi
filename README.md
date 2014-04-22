Pykakasi library
==================

pykakasi is re-imprelemtation of kakasi library by Python.

How To Use pykakasi
------------------

```python
    import pykakasi.kakasi as kakasi

    kakasi = kakasi()
    kakasi.setMode("H","a") # default: Hiragana -> Roman
    kakasi.setMode("K","a") # default: Katakana -> Roman
    kakasi.setMode("J","a") # default: Japanese -> Roman
    kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
    kakasi.setMode("C", true) # default: Separator
    kakasi.setMode("c", false) # default: no Capitalize
    conv = kakasi.getConverter()
    result = conv.do(text)
```

You can use output `Mode` values from "h", "k", "a" which is each means
"Hiragana", "Katakana" and "Alphabet".
For input, you can use "J" that means "Japanese" that is
mixture of Kanji, Katakana and Hiragana.
Also there is values of "H", "K" that means "Hiragana", and "Katakana".
You can use  "Hepburn" or "Kunrei" as mode "r", Roman table switch.
Also "C" used for separator switch, "c" for capitalize switch.


Options
-------------------

These switch alphabets are derived from original Kakasi.
Now it support following options:

| option | description         | possible values | note                  |
| ------ | :----------         | --------------- | :----------           |
| "K"    | Katakana convertion | "a" or None     | roman or noconversion |
| "H"    | Hiragana convertion | "a" or None     | roman or noconversion |
| "J"    | Kanji conversion    | "a", "h", "k", or None | roman or Hiragana, Katakana |

Original kakasi defines following options:

```
  -a[jE] -j[aE] -g[ajE] -k[ajKH]
  -E[aj] -K[ajkH] -H[ajkK] -J[ajkKH]
  -i{oldjis,newjis,dec,euc,sjis}
   -o{oldjis,newjis,dec,euc,sjis}
  -r{hepburn,kunrei} -p -s -f -c"chars" 
   [jisyo1, jisyo2,,,]

  Character Sets:
       a: ascii  j: jisroman  g: graphic  k: kana 
       (j,k     defined in jisx0201)
       E: kigou  K: katakana  H: hiragana J: kanji
       (E,K,H,J defined in jisx0208)

  Options:
    -i: input coding system    -o: output coding system
    -r: romaji conversion system
    -p: list all readings (with -J option)
    -s: insert separate characters (with -J option)
    -f: furigana mode (with -J option)
    -c: skip chars within jukugo
        (with -J option: default TAB CR LF BLANK)
    -C: romaji Capitalize (with -Ja or -Jj option)
    -U: romaji Upcase     (with -Ja or -Jj option)
    -u: call fflush() after 1 character output
    -w: wakatigaki mode
```
