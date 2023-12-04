from functools import partial
from pathlib import Path
import re

import numpy as np

if __name__ == "__main__":
    with Path("2023/Day_4/data/input.txt").open() as fd:
        data = fd.readlines()
    sums = 0
    for line in data:
        line = re.sub(r"\ \ ", " ", line)
        card, numbers = line.split(":")
        winners_line, got_line = numbers.strip().split("|")
        winner_numbers = list(map(int, winners_line.strip().split(" ")))
        got_numbers = list(map(int, got_line.strip().split(" ")))
        numbers_got_winner = set(
            [got_number for got_number in got_numbers if got_number in winner_numbers]
        )
        len_winners = len(numbers_got_winner)
        if len_winners == 0:
            continue
        sums += 2 ** (len(numbers_got_winner) - 1)
    print(sums)
