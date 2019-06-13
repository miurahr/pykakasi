# -*- coding: utf-8 -*-

import threading

import pykakasi
import pykakasi.kanwa

I_TEST = [
    (u"菟", u"兎"),
    (u"菟集", u"兎集"),
    (u"熙", u"煕"),
    (u"壱弍", u"一二"),
    (u"森鷗外", u"森鴎外"),
]


def test_thread_itaiji():
    for i in range(10):
        t = threading.Thread(target=worker_itaiji)
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()


def worker_itaiji():
    j = pykakasi.J2("H")
    for case, result in I_TEST:
        assert j.itaiji_conv(case) == result


def test_thread_kanwa():
    for i in range(10):
        t = threading.Thread(target=worker_kanwa)
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()


def worker_kanwa():
    k = pykakasi.kanwa.kanwa()
    d = k.load(u"春")
    assert d[u"春"] is not None
