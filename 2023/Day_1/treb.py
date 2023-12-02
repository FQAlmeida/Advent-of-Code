from pathlib import Path
import re
from word2number import w2n

if __name__ == "__main__":
    with Path("2023/Day_1/data/input.txt").open() as fd:
        data = fd.readlines()
    r = re.compile("([0-9]|one|two|three|four|five|six|seven|eight|nine)")
    sums = 0
    for line in data:
        line = line.strip()
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
