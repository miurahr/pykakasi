# -*- coding: utf-8 -*-
#  jisyo.py
#
# Copyright 2011-2018 Hiroshi Miura <miurahr@linux.com>
from pkg_resources import resource_filename
from six.moves.cPickle import load

class jisyo (object):
    _dict = None
    _len = 4

    def __init__(self, pklname):
        dict_pkl = open(resource_filename(__name__, pklname), 'rb')
        (self._dict, self._len) = load(dict_pkl)

    def haskey(self, key):
        return key in self._dict

    def lookup(self,key):
        return self._dict[key]

    def maxkeylen(self):
        return self._len
