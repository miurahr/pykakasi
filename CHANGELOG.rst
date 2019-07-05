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

* pytest: now run on project root without tox, by generating
  dictionary as a test fixture.
* tox: run tox test with installed dictionary instead of
  a generated fixture.
* Optimize kana conversion function.


Fixed
-----

* Version naming follows PEP386.
* Sometimes fails to insert space after punctuation(#79).
* Special case in kana-roman passport conversion such as 'etchu' etc.

Deprecated
----------

Removed
-------

Security
--------



.. _Unreleased: https://github.com/miurahr/pykakasi/compare/v1.0c2...HEAD
