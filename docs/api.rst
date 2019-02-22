.. _api-documents-ref:

=====================
Programming Interface
=====================


Conversion Options
==================

These switch alphabets are derived from original Kakasi.
Now it support following options:

+--------+---------------------+------------+---------------------------------------+
| Option | Description         | Values     | Note                                  |
+========+=====================+============+=======================================+
| K      | Katakana conversion | a,H,None   | roman, Hiragana or non conversion     |
+--------+---------------------+------------+---------------------------------------+
| H      | Hiragana conversion | a,K,None   | roman, Katakana or non conversion     |
+--------+---------------------+------------+---------------------------------------+
| J      | Kanji conversion    | a,H,K,None | roman or Hiragana, Katakana or noconv |
+--------+---------------------+------------+---------------------------------------+
| a      | Roman conversion    | E,None     | JIS ROMAN or non conversion           |
+--------+---------------------+------------+---------------------------------------+
| E      | JIS ROMAN conversion| a,None     | ascii roman or non conversion         |
+--------+---------------------+------------+---------------------------------------+

Each character means character sets as follows::

    Character Sets
       a: ascii  j: jisroman  g: graphic  k: kana
       (j,k     defined in jisx0201)
       E: kigou  K: katakana  H: hiragana J: kanji
       (E,K,H,J defined in jisx0208)



API usage example
=================

How to Install::

    pip install pykakasi

Building library, setup script build dictionary db file and generate pickled db files.
Without dictionary files, a library fails to run.

Dependencies::

    six and semidbm

Sample source code::

    from pykakasi import kakasi,wakati

    text = u"かな漢字交じり文"
    kakasi = kakasi()
    kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
    kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
    kakasi.setMode("J","a") # Japanese to ascii, default: no conversion
    kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
    kakasi.setMode("s", True) # add space, default: no separator
    kakasi.setMode("C", True) # capitalize, default: no capitalize
    conv = kakasi.getConverter()
    result = conv.do(text)
    print(result)

    wakati = wakati()
    conv = wakati.getConverter()
    result = conv.do(text)
    print(result)

You can use output `Mode` values from "H", "K", "a" which is each means
"Hiragana", "Katakana" and "Alphabet".
For input, you can use "J" that means "Japanese" that is
mixture of Kanji, Katakana and Hiragana.
Also there is values of "H", "K" that means "Hiragana", and "Katakana".
You can use  "Hepburn" , "Kunrei" or "Passport" as mode "r", Roman table switch.
Also "s" used for separator switch, "C" for capitalize switch.
"S" for separator storing option.

