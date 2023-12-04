from pathlib import Path
import re

import numpy as np

if __name__ == "__main__":
    with Path("2023/Day_4/data/input.txt").open() as fd:
        data = fd.readlines()
    sums = 0
    amount = [1]*len(data)
    for i, line in enumerate(data):
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
        for j in range(i+1, i+1+len_winners):
            amount[j] += amount[i]
    print(sum(amount))
