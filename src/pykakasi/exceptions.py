# -*- coding: utf-8 -*-
#  exceptions.py
#
# Copyright 2015-2019 Hiroshi Miura <miurahr@linux.com>
#


class PyKakasiException(Exception):
    pass


class UnknownCharacterException(PyKakasiException):
    pass


class UnsupportedRomanRulesException(PyKakasiException):
    pass


class UnknownOptionsException(PyKakasiException):
    pass


class InvalidModeValueException(PyKakasiException):
    pass


class InvalidFlagValueException(PyKakasiException):
    pass
