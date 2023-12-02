from pathlib import Path
import re
from word2number import w2n

if __name__ == "__main__":
    with Path("2023/Day_1/data/input.txt").open() as fd:
        data = fd.readlines()
    r = re.compile("([0-9]|one|two|three|four|five|six|seven|eight|nine)")
    rs = [
        (re.compile("one"), "on1e"),
        (re.compile("two"), "tw2o"),
        (re.compile("three"), "thre3e"),
        (re.compile("four"), "four4"),
        (re.compile("five"), "fiv5e"),
        (re.compile("six"), "six6"),
        (re.compile("seven"), "senve7n"),
        (re.compile("eight"), "eigh8t"),
        (re.compile("nine"), "nin9e"),
    ]
    sums = 0
    for line in data:
        line = line.strip()
        for rx, s in rs:
            line = re.sub(rx, s, line)
        line = re.sub("[a-zA-Z]", "", line)
        items = r.findall(line)
        if not items:
            print("error")
            assert False
        first, second = str(items[0]), str(items[-1])
        if first.isalpha():
            first = w2n.word_to_num(first)
        if second.isalpha():
            second = w2n.word_to_num(second)
        num = int(f"{first}{second}")
        print(num, items, line)
        sums += num
    print(sums)
