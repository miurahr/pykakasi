import os
import sys

import cpuinfo
import pytest


@pytest.fixture(scope="session", autouse=True)
def dictionary_setup_fixture():
    root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    if "TOX_ENV_DIR" not in os.environ:
        sys.path.insert(1, os.path.join(root_dir, "src"))
        import kakasidict
        from pykakasi.properties import Configurations

        dpath = os.path.join(root_dir, "build", "lib", "pykakasi", "data")
        print("Generating kanwa dictionary in %s\n" % dpath)
        kanwa = kakasidict.Genkanwadict()
        kanwa.generate_dictionaries(dpath)
        Configurations.data_path = dpath


def pytest_benchmark_update_json(config, benchmarks, output_json):
    """Calculate speed and add as extra_info"""
    for benchmark in output_json["benchmarks"]:
        if "data_size" in benchmark["extra_info"]:
            rate = (
                benchmark["extra_info"].get("data_size", 0.0)
                / benchmark["stats"]["mean"]
            )
            benchmark["extra_info"]["rate"] = rate


def pytest_benchmark_update_machine_info(config, machine_info):
    cpu_info = cpuinfo.get_cpu_info()
    brand = cpu_info.get("brand_raw", None)
    if brand is None:
        brand = "{} core(s) {} CPU ".format(
            cpu_info.get("count", "unknown"), cpu_info.get("arch", "unknown")
        )
    machine_info["cpu"]["brand"] = brand
    machine_info["cpu"]["hz_actual_friendly"] = cpu_info.get(
        "hz_actual_friendly", "unknown"
    )
