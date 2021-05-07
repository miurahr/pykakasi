# -*- coding: utf-8 -*-
#  kakasi.py
#
# Copyright 2011-2021 Hiroshi Miura <miurahr@linux.com>
#

__license__ = "GPL 3"
__copyright__ = "2014-2021 Hiroshi Miura <miurahr@linux.com>"
__docformat__ = "restructuredtext en"

from .kakasi import Kakasi, PyKakasiException, UnknownCharacterException
from .legacy import (
    InvalidFlagValueException,
    InvalidModeValueException,
    UnknownOptionsException,
    UnsupportedRomanRulesException,
    kakasi,
    wakati,
)

__all__ = [
    "Kakasi",
    "kakasi",
    "wakati",
    "PyKakasiException",
    "UnknownCharacterException",
    "UnsupportedRomanRulesException",
    "UnknownOptionsException",
    "InvalidModeValueException",
    "InvalidFlagValueException",
]
