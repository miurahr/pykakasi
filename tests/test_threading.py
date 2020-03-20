# -*- coding: utf-8 -*-
import concurrent.futures
import threading

import pytest

import pykakasi
import pykakasi.kanji

I_TEST = [
    (u"菟", u"兎"),
    (u"菟集", u"兎集"),
    (u"熙", u"煕"),
    (u"壱弍", u"一二"),
    (u"森鷗外", u"森鴎外"),
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


@pytest.mark.thread
@pytest.mark.skip
def test_threadpool_itaiji():
    with concurrent.futures.ThreadPoolExecutor(3) as texec:
        tasks = [texec.submit(worker_itaiji) for _ in range(10)]
        for task in concurrent.futures.as_completed(tasks):
            if not task.result():
                raise Exception("Failed.")


def worker_itaiji():
    try:
        j = pykakasi.kanji.J2("H")
        for case, result in I_TEST:
            assert j.itaiji_conv(case) == result
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


@pytest.mark.thread
@pytest.mark.skip
def test_threadpool_kanwa():
    with concurrent.futures.ThreadPoolExecutor(3) as texec:
        tasks = [texec.submit(worker_kanwa) for _ in range(10)]
        for task in concurrent.futures.as_completed(tasks):
            if not task.result():
                raise Exception("Failed.")


def worker_kanwa():
    try:
        k = pykakasi.kanji.Kanwa()
        d = k.load(u"春")
        assert d[u"春"] is not None
    except AssertionError:
        return False
    return True
