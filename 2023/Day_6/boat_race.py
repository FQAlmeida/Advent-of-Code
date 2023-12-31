from math import ceil, floor
from pathlib import Path
import re


# d(t, th) = (t - th) * th
# th(time, d) => 1*th^2 - t*th + d = 0

def calc_ways_to_win(time: int, distance: int):
    delta = (time**2) - (4 * distance)
    delta_root = delta ** (1 / 2)
    x1 = (time + (delta_root)) / 2
    x2 = (time - (delta_root)) / 2
    x1, x2 = sorted((x1, x2))
    x1 += 1e-12
    x2 -= 1e-12
    x1, x2 = ceil(x1), floor(x2)
    return x2 - x1 + 1


if __name__ == "__main__":
    with Path("2023/Day_6/data/input.txt").open("r") as fd:
        lines = fd.readlines()
    r = re.compile(r"( )+")
    lines = map(lambda line: line.split(":")[1].strip(), lines)
    lines = map(lambda line: list(map(int, r.sub("", line).split(" "))), lines)
    races = list(zip(*lines))

    qtd_ways = 1
    for time, distance in races:
        ways_to_win = calc_ways_to_win(time, distance)
        qtd_ways *= ways_to_win
    print(qtd_ways)
