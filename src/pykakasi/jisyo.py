# -*- coding: utf-8 -*-
#  jisyo.py
#
# Copyright 2011-2019 Hiroshi Miura <miurahr@linux.com>

from klepto.archives import file_archive
from pkg_resources import resource_filename


class jisyo (object):
    _dict = None

    def __init__(self, dictname):
        self._dict = file_archive(resource_filename(__name__, dictname), {}, serialized=True )
        self._dict.load()

    def haskey(self, key):
        return key in self._dict

    def lookup(self, key):
        return self._dict[key]

    def maxkeylen(self):
        return self._dict['_max_key_len_']
