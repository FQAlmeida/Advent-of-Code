from functools import partial, reduce
import operator
from pathlib import Path
import re

import numpy as np


def convolute(matrix: np.ndarray):
    matrix = np.pad(matrix, pad_width=1, mode="constant", constant_values=0)
    sums = 0
    color = -3
    for i, line in enumerate(matrix[1:-1], 1):
        for j, item in enumerate(line[1:-1], 1):
            if item == -2:
                c, items = check_item(matrix, i, j, color)
                print(matrix)
                print(c)
                if len(items) == 2:
                    sums += reduce(operator.mul, items, 1)
                color = c
    return sums


def paint(matrix, i, j, item, color):
    for y in range(-1, 2):
        if matrix[i, j + y] == item:
            matrix[i, j + y] = color
            paint(matrix, i, j + y, item, color)
    return color - 1


def check_item(matrix, i, j, color: int):
    items: list[int] = list()
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if matrix[i + x, j + y] > 0:
                r = int(matrix[i + x, j + y])
                color = paint(matrix, i + x, j + y, r, color)
                items.append(r)
    return color, items


def encode_symbol(symbol: str):
    r = re.compile("[0-9]+")
    if symbol == ".":
        return [
            0,
        ]
    elif symbol == "*":
        return [
            -2,
        ]
    elif r.match(symbol):
        return [
            int(symbol),
        ] * len(symbol)
    return [
        -1,
    ]


def encoder(symbols: list[str]):
    return list(
        reduce(lambda prev, new: [*prev, *new], map(encode_symbol, symbols), list())
    )


def helper(x: int):
    if x > 0:
        return 1
    if x < 0:
        return 2
    return 0


if __name__ == "__main__":
    with Path("2023/Day_3/data/input.txt").open() as fd:
        data = fd.readlines()
    data_map = list(
        map(
            partial(
                re.findall, re.compile(r"([0-9]+|\.|\$|\#|\*|\+|\%|\=|\&|\/|\\|\@|\-)")
            ),
            map(str.strip, data),
        ),
    )
    data_map = list(map(encoder, data_map))
    max_len = max(map(len, data_map))
    for i, line in enumerate(data_map):
        if len(line) != max_len:
            print(line, len(line), max_len, data[i], sep="\n")
    result = convolute(np.array(data_map))
    print(result)
