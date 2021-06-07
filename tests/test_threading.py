# -*- coding: utf-8 -*-
import threading

import pytest

import pykakasi
import pykakasi.kanji

I_TEST = [
    ("菟", "兎"),
    ("菟集", "兎集"),
    ("熙", "煕"),
    ("壱弍", "一二"),
    ("森鷗外", "森鴎外"),
    ("\U0000845B\U000E0101城市", "\U0000845B城市"),
    ("\U0000845B\U000E0100飾区", "\U0000845B飾区"),
]


def test_worker_itaiji():
    assert worker_itaiji()


@pytest.mark.thread
def test_thread_itaiji():
    tasks = []
    for i in range(10):
        t = threading.Thread(target=worker_itaiji)
        tasks.append(t)
        t.start()
    for t in tasks:
        t.join()


def worker_itaiji():
    try:
        j = pykakasi.kanji.JConv()
        for case, result in I_TEST:
            assert j._itaiji.convert(case) == result
    except AssertionError:
        return False
    return True


@pytest.mark.thread
def test_thread_kanwa():
    tasks = []
    for i in range(10):
        t = threading.Thread(target=worker_kanwa)
        tasks.append(t)
        t.start()
    for t in tasks:
        t.join()


def worker_kanwa():
    try:
        k = pykakasi.kanji.Kanwa()
        d = k.load("春")
        assert d["春"] is not None
    except AssertionError:
        return False
    return True
