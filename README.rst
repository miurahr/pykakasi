=======
Pykakasi
=======

      pykakasi is re-imprelemtation of kakasi library by Python.

How To Use pykakasi
==================

::

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
    conv = kawati.getConverter()
    result = conv.do(text)

You can use output `Mode` values from "h", "k", "a" which is each means
"Hiragana", "Katakana" and "Alphabet".
For input, you can use "J" that means "Japanese" that is
mixture of Kanji, Katakana and Hiragana.
Also there is values of "H", "K" that means "Hiragana", and "Katakana".
You can use  "Hepburn" or "Kunrei" as mode "r", Roman table switch.
Also "C" used for separator switch, "c" for capitalize switch.

