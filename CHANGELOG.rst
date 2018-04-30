====================
PyKakasi ChangeLog
====================

All notable changes to this project will be documented in this file.

`Unreleased`_
=============

Added
-----

Changed
-------

Fixed
-----

Deprecated
----------

Removed
-------

Security
--------


`v0.92`_ (30, Apr., 2018)
=========================

Changed
-------

* Release wheel binary packages for each python versions.(#50)


`v0.91`_ (29, Apr., 2018)
=========================

Added
-----

* Test case convert from Full-width Alphabet/symbols to Half-width (E2a).
* Convert logic from Full-width alphabet/symbols to Half-width (E2a).
* Add more words with repeat mark from SKK-JISYO.L (#46)

Changed
-------

* Not distribute binary wheel package, because of dictionary data depends on python version.

Fixed
-----

* Conversion from ○々 become 'TypeError: must be str, not NoneType' (#46)
* Appveyor: update deployment script.


`v0.90`_ (29, Mar., 2018)
=========================

Changed
-------

* Update release script
* Update version number for kakasi script


`v0.83`_ (29, Mar., 2018)
=========================

Fixed
-----

* Appveyor: fix twine not found error in deploy script 
* setup: clean old dictionary when building


`v0.82`_ (29, Mar., 2018)
=============

Added
-----

* Russian characters defined in JIS X0208(#13)

Changed
-------

* README: fix typo and add description for Kigou conversion.
* README: update sample code to working one.
* Appveyor: generate wheel artifacts 

Fixed
-----

* MANIFEST: update to specify kanwadict3.db explicitly.
* setup.py: allow reading README.rst written in UTF-8. 

`v0.80`_ (28, Mar., 2018)
=========================

Here is a release candicate for v1.0

Added
-----

* Readme: add dependency description.

Changed
-------

* Bump up version number.
* Readme: recommend `pip install pykakasi`
* Replace anydbm with semidbm that is a pure dbm implementation with performance.

Fixed
-----

* Reduce test warnings.
* No platform dependency now.
* Fix dependency in wheel package that depend on gdbm in previous release.

Removed
-------

* Binary release for windows and linux.


`v0.28`_  (26, Mar., 2018)
===========================

Fixed
-----

* wheel platform tag for linux is now manylinux1_i686 or _x86_64

`v0.26`_ (26, Mar., 2018)
=============================

Changed
-------

* Use six for python 2 and 3 compatility code.

Fixed
-----

* Build wheel with platform names.

`v0.25`_ (25, Mar., 2018)
=============================


Added
-----

* Test on Python 3.5 and Python 3.6
* Test on Windows using AppVeyor
* Mesure test coverage and monitor on coveralls.io

Changed
-------

* Move dictionary data to pykakasi/data
* Build dictionary when setup.py build
* Recoomend installation from github source not pypi. (#17)
* Converter configuration become per instance not class wide.

Fixed
-----

* kakasi.py: Fix exception class name typo of InvalidFlagValueException
* kakasi.py, h2a.py, k2a.py: Do not import all exception class.
* test_genkanwadict.py: Multi platform support for temp directory(#27). 
* setup.py: change _pre_build() to pre_build() (#17).

`v0.23`_ (25, May., 2014)
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


`v0.22`_ (3, May., 2014)
=============================

* Introduced kakasi command
* Symbols support

`v0.21`_ (27, April., 2014)
=============================

* Wakati conversion support

`v0.20`_ (27, April., 2014)
=============================

* Pickled roman tables

Version 0.10 (25, April, 2014)
==============================

* Work on python 2.6, 2.7, 3.3, 3.4
  (Thanks @FGtatsuro)
* Kunrei and Hepburn roman table

.. _Unreleased: https://github.com/miurahr/pykakasi/compare/v0.92...HEAD
.. _v0.92: https://github.com/miurahr/pykakasi/compare/v0.91...v0.92
.. _v0.91: https://github.com/miurahr/pykakasi/compare/v0.90...v0.91
.. _v0.90: https://github.com/miurahr/pykakasi/compare/v0.83...v0.90
.. _v0.83: https://github.com/miurahr/pykakasi/compare/v0.82...v0.83
.. _v0.82: https://github.com/miurahr/pykakasi/compare/v0.80...v0.82
.. _v0.80: https://github.com/miurahr/pykakasi/compare/v0.28...v0.80
.. _v0.28: https://github.com/miurahr/pykakasi/compare/v0.26...v0.28
.. _v0.26: https://github.com/miurahr/pykakasi/compare/v0.25...v0.26
.. _v0.25: https://github.com/miurahr/pykakasi/compare/v0.23...v0.25
.. _v0.23: https://github.com/miurahr/pykakasi/compare/v0.22...v0.23
.. _v0.22: https://github.com/miurahr/pykakasi/compare/v0.21...v0.22
.. _v0.21: https://github.com/miurahr/pykakasi/compare/v0.20...v0.21
.. _v0.20: https://github.com/miurahr/pykakasi/compare/v0.10...v0.20
