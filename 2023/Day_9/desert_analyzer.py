from pathlib import Path


def fit(readings: list[int]):
    if not readings:
        return 0
    diffs: list[int] = list()
    for i in range(len(readings[:-1])):
        diff = readings[i + 1] - readings[i]
        diffs.append(diff)
    if all(map(lambda diff: diff == 0, diffs)):
        return readings[-1]
    print(*readings)
    pred = fit(diffs)
    return readings[-1] + pred


if __name__ == "__main__":
    with Path("2023/Day_9/data/input.txt").open("r") as fd:
        lines = fd.readlines()
    data = list(map(lambda line: list(map(int, line.strip().split(" ")[::-1])), lines))
    sums = sum(map(fit, data))
    print(sums)
