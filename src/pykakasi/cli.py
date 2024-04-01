#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import platform
import re
import sys
import warnings
from typing import Any, Optional

import pykakasi

from importlib import metadata as importlib_metadata


class Cli:

    romanvals = {"h": "Hepburn", "k": "Kunrei", "p": "Passport"}

    def __init__(self):
        self.kakasi = None
        self.parser = argparse.ArgumentParser(
            prog="kakasi",
            description="kakasi implementation on Python",
            formatter_class=argparse.RawTextHelpFormatter,
            add_help=True,
        )
        self.parser.add_argument("-v", "--version", action="store_true", help="Show version string")
        self.parser.add_argument(
            "-I", type=argparse.FileType("r"), default=sys.stdin, help="Specify input file (default STDIN)"
        )
        self.parser.add_argument(
            "-O", type=argparse.FileType("w"), default=sys.stdout, help="Specify output file (default STDOUT)"
        )
        self.parser.add_argument("-w", "--wakati", action="store_true", help="Wakati gaki mode")
        self.parser.add_argument(
            "-r",
            "--roman",
            action="store",
            choices=["k", "h", "p"],
            help="Set romanize method; k:kunrei, h:hepburn, or p:passport",
        )
        self.parser.add_argument("-s", "--space", action="store_true", help="Add spacing between tokens")
        self.parser.add_argument("-S", "--separator", action="store", help="Set separator character")
        self.parser.add_argument("-f", "--furigana", action="store_true", help="Furigana output")
        self.parser.add_argument("-C", "--capital", action="store_true", help="Capitalize output")
        self.parser.add_argument("-U", "--upper", action="store_true", help="Upper case output")
        self.parser.add_argument("-E", action="store", choices=["a", "N"], help="Full-width roman characters conversion")
        self.parser.add_argument("-J", action="store", choices=["a", "H", "K", "N"], help="Kanji characters conversion")
        self.parser.add_argument("-K", action="store", choices=["a", "H", "N"], help="Katakana conversion")
        self.parser.add_argument("-H", action="store", choices=["a", "K", "N"], help="Hiragana conversion")
        self.parser.add_argument("-a", action="store", choices=["E", "N"], help="Alphabet conversion")

    def run(self, arg: Optional[Any] = None) -> int:
        outfile = None
        infile = None
        mode = {}
        args = self.parser.parse_args(arg)
        if args.version:
            return self.show_version()
        if args.space:
            mode["s"] = True
        if args.separator is not None:
            mode["S"] = args.separator
        if args.roman is not None:
            mode["r"] = args.roman
        if args.furigana:
            mode["f"] = True
        if args.capital:
            mode["C"] = True
        if args.upper:
            mode["U"] = True
        if args.J is not None and "N" != args.J:
            mode["J"] = args.J
        if args.H is not None and "N" != args.H:
            mode["H"] = args.H
        if args.K is not None and "N" != args.K:
            mode["K"] = args.K
        if args.E is not None and "N" != args.E:
            mode["E"] = args.E
        if args.a is not None and "N" != args.a:
            mode["a"] = args.a
        infile = args.I
        outfile = args.O
        if args.wakati:
            self.kakasi = pykakasi.wakati()
            self.do_it(mode, infile, outfile)
        else:
            self.kakasi = pykakasi.kakasi()
            self.do_it(mode, infile, outfile)
        return 0

    def show_version(self):
        dist = importlib_metadata.distribution("pykakasi")
        py_version = platform.python_version()
        py_impl = platform.python_implementation()
        py_build = platform.python_compiler()
        print("pykakasi: version {} on Python {} [{} {}]".format(dist.version, py_version, py_impl, py_build))
        return 0

    def do_it(self, mode, infile, outfile):
        for k, v in mode.items():
            self.kakasi.setMode(k, v)
        converter = self.kakasi.getConverter()
        for line in infile:
            outfile.write(converter.do(line))


def cli_main():
    warnings.simplefilter("ignore", category=DeprecationWarning)
    sys.exit(Cli().run())


if __name__ == "__main__":
    sys.argv[0] = re.sub(r"(-script\.pyw|\.exe)?$", "", sys.argv[0])
    sys.exit(cli_main())
