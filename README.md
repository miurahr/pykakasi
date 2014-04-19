Pykakasi library
==================

pykakasi is re-imprelemtation of kakasi library by Python.

How To Use pykakasi
------------------

```python
    import pykakasi.kakasi as kakasi

    kakasi = kakasi()
    kakasi.setMode("H","a")
    ...
    conv = kakasi.getConverter()
    result = conv.do(text)
```

You can use output `Mode` values from "h", "k", "a" which is each means
"Hiragana", "Katakana" and "Alphabet".
For input, you can use "J" that means each "Japanese" that is
mixture of Kanji, Katakana and Hiragana.
Also there is values of "H", "K" that means "Hiragana", and "Katakana".

