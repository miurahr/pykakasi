# -*- coding: utf-8 -*-
#  jisyo.py
#
# Copyright 2011,2014 Hiroshi Miura <miurahr@linux.com>
from pkg_resources import resource_filename
try: #python2
    from cPickle import load
except: #python3
    from pickle import load

class jisyo (object):
    _dict = None

    def __init__(self, pklname):
        dict_pkl = open(resource_filename(__name__, pklname), 'rb')
        self._dict = load(dict_pkl)

    def haskey(self, key):
        return key in self._dict

    def lookup(self,key):
        return self._dict[key]
