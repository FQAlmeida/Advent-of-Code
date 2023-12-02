from functools import reduce
from pathlib import Path
import re


def check_subset(cube_qtd_color: list[tuple[int, str]]):
    mins = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    is_valid = True
    for cube_qtd, cube_color in cube_qtd_color:
        mins[cube_color] = max(cube_qtd, mins[cube_color])
        match cube_color:
            case "red":
                if cube_qtd > 12:
                    is_valid = False
            case "green":
                if cube_qtd > 13:
                    is_valid = False
            case "blue":
                if cube_qtd > 14:
                    is_valid = False
    return is_valid, mins


def check_set(r: re.Pattern[str], subsets: list[str]):
    mins = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    is_valid = True
    for subset in subsets:
        cube = subset.split(",")
        cube_qtd_color = list(
            map(
                lambda x: (int(x[0]), x[1]),
                map(lambda x: x[0], map(r.findall, cube)),
            )
        )
        is_valid, sub_mins = check_subset(cube_qtd_color)
        for key, value in sub_mins.items():
            mins[key] = max(value, mins[key])
        if not check_subset(cube_qtd_color):
            is_valid = False
    return is_valid, mins


if __name__ == "__main__":
    with Path("2023/Day_2/data/input.txt").open() as fd:
        data = fd.readlines()
    r = re.compile("^([0-9]+)(blue|red|green)$")
    sum_games = 0
    sum_powers = 0
    for line in data:
        game, cubes = line.split(":")
        game = int(game[5:])
        subsets = cubes.replace(" ", "").split(";")
        is_valid, mins = check_set(r, subsets)
        if is_valid:
            sum_games += game
        if 0 in mins.values():
            print("has zero")
        cubes_power = reduce(lambda prod, value: prod * value, mins.values(), 1)
        sum_powers += cubes_power
    print(sum_games)
    print(sum_powers)
