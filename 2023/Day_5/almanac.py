from math import inf
from pathlib import Path
from pprint import pprint


def separate_maps(data: list[str]):
    actual_map: list[tuple[int, int, int]] = []
    for line in data[2:]:
        line = line.strip()
        if not line:
            continue
        if ":" in line:
            yield actual_map
            actual_map = list()
            continue
        dest, origin, length = map(int, line.split(" "))
        actual_map.append((dest, origin, length))
    yield actual_map


def get_mapped_value(origin: int, mapped_dests: list[tuple[int, int, int]]):
    for mapped_dest, mapped_origin, length in mapped_dests:
        if origin >= mapped_origin and origin < mapped_origin + length:
            return mapped_dest + (origin - mapped_origin)
    return origin


if __name__ == "__main__":
    with Path("2023/Day_5/data/input.txt").open() as fd:
        data = fd.readlines()
    minimun = inf
    seeds = list(map(int, data[0].strip().split(":")[1].strip().split(" ")))
    data_sepd = list(separate_maps(data[1:]))
    for seed in seeds:
        origin = seed
        for mapper in data_sepd:
            dest = get_mapped_value(origin, mapper)
            origin = dest
        minimun = min(minimun, origin)
    print(minimun)