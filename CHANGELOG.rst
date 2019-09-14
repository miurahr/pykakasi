==================
PyKakasi ChangeLog
==================

All notable changes to this project will be documented in this file.

***************
Current changes
***************

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

`v1.1b2`_ (14, Sep, 2019)
========================

Fixed
-----

* Fix Long symble issue(#58) (thanks @northernbird and @ta9ya)


`v1.1b1`_ (6, Sep, 2019)
========================

Added
-----
* Add conversions: kya, kyu, kyo

Changed
-------
* Rewording README document

`v1.1a1`_ (8, Jul, 2019)
========================

Changed
-------

* pytest: now run on project root without tox, by generating
  dictionary as a test fixture.
* tox: run tox test with installed dictionary instead of
  a generated fixture.
* Optimize kana conversion function.
* Move kakasidict.py to src and conftest.py to tests

Fixed
-----

* Version naming follows PEP386.
* Sometimes fails to insert space after punctuation(#79).
* Special case in kana-roman passport conversion such as 'etchu' etc.



.. _Unreleased: https://github.com/miurahr/pykakasi/compare/v1.1b2...HEAD
.. _v1.1b2: https://github.com/miurahr/pykakasi/compare/v1.0b1...v1.1b2
.. _v1.1b1: https://github.com/miurahr/pykakasi/compare/v1.0a1...v1.1b1
.. _v1.1a1: https://github.com/miurahr/pykakasi/compare/v1.0c2...v1.1a1
