import argparse
import json
import pathlib
import sys

from tabulate import tabulate  # type: ignore


def generate_results(results_files, type):
    table = []
    for f in results_files:
        with open(f, "r") as results:
            root = json.load(results)
        benchmarks = root["benchmarks"]
        machine_info = root["machine_info"]
        commit_info = root["commit_info"]
        meta = "{}-{}({})".format(
            machine_info["python_implementation"],
            machine_info["python_version"],
            machine_info["system"],
        )
        commit = "{}@{}".format(commit_info["id"], commit_info["branch"])
        assert len(benchmarks) == 1
        for bm in benchmarks:
            rate = bm["extra_info"]["rate"] / 1000
            if rate < 100:
                rate = round(rate, 1)
            else:
                rate = round(rate, 0)
            min = bm["stats"]["min"]
            max = bm["stats"]["max"]
            avr = bm["stats"]["mean"]
            table.append([meta, commit, rate, min, max, avr])
    sortrate = lambda val: val[2]
    table.sort(reverse=True, key=sortrate)
    return tabulate(
        table,
        headers=[
            "platform",
            "commit",
            "rate (char/mSec)",
            "min(sec)",
            "max(sec)",
            "mean(sec)",
        ],
        tablefmt=type,
    )


def main():
    parser = argparse.ArgumentParser(prog="benchmark_result")
    parser.add_argument("--markdown", action="store_true", help="print markdown table")
    parser.add_argument(
        "jsonfiles", nargs="+", type=pathlib.Path, help="pytest-benchmark saved result."
    )
    args = parser.parse_args()
    if args.markdown:
        type = "github"
    else:
        type = "simple"
    body = generate_results(args.jsonfiles, type)
    print(body)


if __name__ == "__main__":
    sys.exit(main())
