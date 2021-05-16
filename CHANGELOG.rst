==================
PyKakasi ChangeLog
==================

All notable changes to this project will be documented in this file.

Unreleased_
===========

Added
-----
* dictionary: add noun and adjectives from UniDic(#140)

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

v2.1.1_ (16, May 2021)
======================

Added
-----
* Provide Kakasi.normalize(text) class method
* Add unidic data into data (not used yet), and add parse utility.

Fixed
-----
* Put type hint stub into package
* Copyright notifications

Changed
-------
* Expand all cletter into dictionary (#139)
* Change primary kanwadict index from str to int
* test: gather all legacy test into test_pykakasi_legacy.py file.


v2.1.0_ (6, May 2021)
=====================

Added
-----
* Deprecation warning when using old api(#124)
* Add type hint file(pyi) (#124)
* Benchmark test codes(#122)

Changed
-------
* Cache internal results and improve performance about 30-40 times.(#128)
* Use standard pickle for database file(#128)
* Exceptions module is now `pykakasi`, not `pykakasi.exceptions`

Removed
-------
* Dependency for klepto(#128)


v2.0.8_ (4, May 2021)
=====================

Added
-----

* test: Benchmark and profiling (#122)

Changed
-------

* Performance: avoid ord() when checking long-mark, speed up about 6%
* Reformat code by black(#121)


v2.0.7_ (26, Feb. 2021)
=======================

Fixed
-----

* Infinite loop after running for a while,
  handle independent HW VOICED SOUND MARK (#115, #118)


v2.0.6_ (7, Feb. 2021)
======================

Fixed
-----

* Hiragana for Age countersa(#116,#117)


v2.0.5_ (5, Feb. 2021)
======================

Changed
-------

* CLI: use argparse for option parse(#113)

Fixed
-----

* Handle 思った、言った、行った properly.(#114)
* CI: fix coveralls error

Deprecated
----------

* CI: drop travis-ci test and badge


v2.0.4_ (26, Nov. 2020)
=======================

Fixed
-----

* CLI: Fix -v and -h option crash on python 3.7 and before (#108).

v2.0.3_ (25, Nov. 2020)
=======================

Fixed
-----

* CLI: Fix -v and -h option crash (#108).


v2.0.2_ (23, Jul. 2020)
=======================

Fixed
-----

* Fix convert() to handle Katakana correctly.(#103)


v2.0.1_ (23, Jul. 2020)
=======================

Changed
-------

* Update setup.py, setup.cfg, tox.ini(#102)


Fixed
-----

* Fix convert() misses last part of a text (#99, #100)
* Fix CI, coverage, and coveralls configurations(#101)


v2.0.0_ (31, May. 2020)
=======================


.. _Unreleased: https://github.com/miurahr/pykakasi/compare/v2.1.1...HEAD
.. _v2.1.1: https://github.com/miurahr/pykakasi/compare/v2.1.0...v2.1.1
.. _v2.1.0: https://github.com/miurahr/pykakasi/compare/v2.0.8...v2.1.0
.. _v2.0.8: https://github.com/miurahr/pykakasi/compare/v2.0.7...v2.0.8
.. _v2.0.7: https://github.com/miurahr/pykakasi/compare/v2.0.6...v2.0.7
.. _v2.0.6: https://github.com/miurahr/pykakasi/compare/v2.0.5...v2.0.6
.. _v2.0.5: https://github.com/miurahr/pykakasi/compare/v2.0.4...v2.0.5
.. _v2.0.4: https://github.com/miurahr/pykakasi/compare/v2.0.3...v2.0.4
.. _v2.0.3: https://github.com/miurahr/pykakasi/compare/v2.0.2...v2.0.3
.. _v2.0.2: https://github.com/miurahr/pykakasi/compare/v2.0.1...v2.0.2
.. _v2.0.1: https://github.com/miurahr/pykakasi/compare/v2.0.0...v2.0.1
.. _v2.0.0: https://github.com/miurahr/pykakasi/compare/v2.0.0b1...v2.0.0
