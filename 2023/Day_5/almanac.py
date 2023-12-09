from math import ceil, inf
from multiprocessing import Pool
from pathlib import Path
from tqdm import tqdm


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


def get_seeds(seeds: list[int]):
    for i, seed in enumerate(seeds[::2]):
        yield (seed, seeds[(2 * i) + 1])


def worker_2(seed: int):
    origin = seed
    for mapper in data_sepd:
        dest = get_mapped_value(origin, mapper)
        origin = dest
    return origin


def worker(seed: int, length: int):
    max_per_map = 100_000_000
    iters = ceil(length / max_per_map)
    procd = 0
    results = list()
    while procd < length:
        remaining = min(max_per_map, length - procd)
        with Pool() as pool:
            partial_results = list(
                tqdm(
                    pool.imap(
                        worker_2,
                        (seed + i for i in range(procd, procd + remaining)),
                        chunksize=2048,
                    ),
                    desc=f"Part {ceil(procd/max_per_map)} of {iters}",
                    total=length,
                    position=1,
                )
            )
            results.append(min(partial_results))
        procd += remaining
    minimun = min(results)
    return minimun


if __name__ == "__main__":
    with Path("2023/Day_5/data/input.txt").open() as fd:
        data = fd.readlines()
    minimun = inf

    seeds = list(
        get_seeds(list(map(int, data[0].strip().split(":")[1].strip().split(" "))))
    )
    data_sepd = list(separate_maps(data[1:]))
    results = [
        worker(seed, length)
        for seed, length in tqdm(seeds, total=len(seeds), position=0)
    ]
    print(results)
    print("Result: ", min(results))
