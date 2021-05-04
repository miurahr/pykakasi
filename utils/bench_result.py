import argparse
import json
import pathlib
import sys

from tabulate import tabulate  # type: ignore


def generate_results(results_files, type):
    table = []
    for f in results_files:
        with open(f, 'r') as results:
            root = json.load(results)
        benchmarks = root['benchmarks']
        machine_info = root['machine_info']
        meta = '{} {} on {} {}'.format(machine_info["python_implementation"], machine_info["python_version"],
                                       machine_info['system'], machine_info['release'])
        assert len(benchmarks) == 1
        for bm in benchmarks:
            rate = bm['extra_info']['rate']
            if rate < 100:
                rate = round(rate, 1)
            else:
                rate = round(rate, 0)
            min = bm['stats']['min']
            max = bm['stats']['max']
            avr = bm['stats']['mean']
            table.append([meta, rate, min, max, avr])
    sortsecond = lambda val: val[1]
    table.sort(reverse=True, key=sortsecond)
    return tabulate(table, headers=['platform', 'rate(char/sec)', 'min(sec)', 'max(sec)', 'mean(sec)'],
                    tablefmt=type)


def main():
    parser = argparse.ArgumentParser(prog='benchmark_result')
    parser.add_argument('--markdown', action='store_true', help='print markdown table')
    parser.add_argument('jsonfiles', nargs='+', type=pathlib.Path, help='pytest-benchmark saved result.')
    args = parser.parse_args()
    if args.markdown:
        type = 'github'
    else:
        type = 'simple'
    body = generate_results(args.jsonfiles, type)
    print(body)


if __name__ == "__main__":
    sys.exit(main())
