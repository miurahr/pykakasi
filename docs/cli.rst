.. _string-options-ref:

*********************
Command Line Options
*********************

The CLI uses getopt to parse the command line options so the short or long versions may be used and the
long options may be truncated to the shortest unambiguous abbreviation.


Executable Options
==================

.. option:: --version, -v

	Display version

.. option:: --help, -h

	Display help text

.. option:: --input, -i <filename>

	input file name

.. option:: --output, -o <filename>

	output file name

Command line executable return codes::

	0. convert successful

Mode Options
============

.. option:: --wakati, -w

	wakati gaki mode

.. option:: -f

	furigana mode


Conversion Options
==================

These switch alphabets are derived from original Kakasi.

.. option:: -K

	How convert Katakana to: a,H,None

.. option:: -H

	How convert Hiragana to: a,K,None

.. option:: -J

	How convert Kanji to: a,H,K,None

.. option:: -a

	How convert ASCII Roman to: E,None

.. option:: -E

	How convert JIS Roman to: a,None


Each character means character sets as follows::

	Character Sets
       a: ascii  j: jisroman  g: graphic  k: kana
       (j,k     defined in jisx0201)
       E: kigou  K: katakana  H: hiragana J: kanji
       (E,K,H,J defined in jisx0208)



Behavior Options
================

.. option:: -U

	Output characters in uppercase

.. option:: -C

	Capitalize first roman character of each words

.. option:: --space, -s

	Insert space character between words

.. option:: --roman, -r <h|k|p>

	Roman word conversion rule
	it takes following keywords::
		- h: hepburn
		- k: kunrei
		- p: passport

.. option:: --separator, -S <character>

	Specify separator character for inserting between words

