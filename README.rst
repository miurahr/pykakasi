=======
Pykakasi
=======

      pykakasi is re-imprelemtation of kakasi library by Python.

How To Use pykakasi
==================

::

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

