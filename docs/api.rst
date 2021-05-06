.. _api-documents-ref:

=====================
Programming Interface
=====================

Conversion Usage
================

convert method
--------------

"convert" returns result as dictionary.
There are keys: 'orig', 'kana', 'hira', 'hepburn', 'kunrei', 'passport'

Example:

.. code-block:: python

    kks = pykakasi.kakasi()
    text = 'かな漢字'
    result = kks.convert(text)
    for item in result:
        print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))

    かな: kana 'カナ', hiragana: 'かな', romaji: 'kana'
    漢字: kana 'カンジ', hiragana: 'かんじ', romaji: 'kanji'



Old API (v1.2)
==============

.. warning::
    The OLD v1.2 API, wakati class, and setMode(), getConverter() and do() functions,  will be deprecated when v3.0 released.
    Please consider to use convert() method.

Conversion Options
------------------

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
-----------------

How to Install::

    pip install pykakasi

Building library, setup script build dictionary db file and generate pickled db files.
Without dictionary files, a library fails to run.

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
