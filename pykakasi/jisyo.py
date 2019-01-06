# -*- coding: utf-8 -*-
#  jisyo.py
#
# Copyright 2011-2019 Hiroshi Miura <miurahr@linux.com>

from pkg_resources import resource_filename
from six.moves import cPickle


class jisyo (object):
    _dict = None
    _len = 4

    def __init__(self, pklname):
        with open(resource_filename(__name__, pklname), 'rb') as dict_pkl:
            (self._dict, self._len) = cPickle.load(dict_pkl)

    def haskey(self, key):
        return key in self._dict

    def lookup(self, key):
        return self._dict[key]

    def maxkeylen(self):
        return self._len
