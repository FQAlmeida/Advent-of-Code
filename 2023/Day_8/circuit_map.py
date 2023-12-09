from math import gcd
from pathlib import Path


def get_steps_to_z(origin, locs, dirs):
    len_dirs = len(dirs)
    step = 0
    while not origin.endswith('Z'):
        next_dir_index = step % len_dirs
        step += 1
        next_dir = dirs[next_dir_index]
        next_dir_s = 0 if next_dir == "L" else 1
        origin = locs[origin][next_dir_s]
    return step


if __name__ == "__main__":
    with Path("2023/Day_8/data/input.txt").open("r") as fd:
        lines = fd.readlines()
    dirs = lines[0].strip()
    locs = {line[:3]: (line[7:10], line.strip()[12:-1]) for line in lines[2:]}
    origins = list(filter(lambda loc: loc.endswith("A"), locs.keys()))
    dists = map(lambda origin: get_steps_to_z(origin, locs, dirs), origins)
    lcm = 1
    for i in dists:
        lcm = lcm*i //gcd(lcm, i)
    print(origins, lcm)
