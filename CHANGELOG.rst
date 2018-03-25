====================
PyKakasi ChangeLog
====================

.. current developments

Unreleaased
===========

**Added:** None

**Changed:** None

**Fixed:** None

**Deprecated:** None

**Removed:** None

**Security:** None


Version 0.27 (26, Mar., 2018)
=============================

**Fixed:**

* Generate multilinux1 architecture for pypi publishing.

Version 0.26 (26, Mar., 2018)
=============================

**Changed:**

* Use six for python 2 and 3 compatility code.

**Fixed:**

* Build wheel with platform names.

Version 0.25 (25, Mar., 2018)
============================

**Added:** 

* Test on Python 3.5 and Python 3.6
* Test on Windows using AppVeyor
* Mesure test coverage and monitor on coveralls.io

**Changed:**

* Move dictionary data to pykakasi/data
* Build dictionary when setup.py build
* Recoomend installation from github source not pypi. (#17)
* Converter configuration become per instance not class wide.

**Fixed:**

* kakasi.py: Fix exception class name typo of InvalidFlagValueException
* kakasi.py, h2a.py, k2a.py: Do not import all exception class.
* test_genkanwadict.py: Multi platform support for temp directory(#27). 
* setup.py: change _pre_build() to pre_build() (#17).

Version 0.23 (25, May, 2014)
=============================

* Support following options in kakasi command.

 - same as original kakasi::

    -J{aKH} -K{aH} -H{aK} -E{a}
    -rk -rh
    -w -s -S -C

 - additional options::

    -v --version -h --help
    -O --output: output file
    -I --input: input file

* Change default behavior as almost same
  as original kakasi
* Zenkaku numbers conversion
* Passport roman conversion table

Version 0.22 (3, May, 2014)
==============================

* Introduced kakasi command
* Symbols support

Version 0.21 (27, April, 2014)
==============================

* Wakati conversion support

Version 0.20 (27, April, 2014)
==============================

* Pickled roman tables

Version 0.10 (25, April, 2014)
==============================

* Work on python 2.6, 2.7, 3.3, 3.4
  (Thanks @FGtatsuro)
* Kunrei and Hepburn roman table
