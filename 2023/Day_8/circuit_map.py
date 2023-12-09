from pathlib import Path


if __name__ == "__main__":
    with Path("2023/Day_8/data/input.txt").open("r") as fd:
        lines = fd.readlines()
    dirs = lines[0].strip()
    locs = {
        line[:3]: (line[7:10], line.strip()[12:-1])
        for line in lines[2:]
    }
    origin = 'AAA'
    len_dirs= len(dirs)
    step = 0
    while origin != 'ZZZ':
        next_dir_index = step % len_dirs
        step += 1
        next_dir = dirs[next_dir_index]
        if next_dir == 'L':
            origin = locs[origin][0]
        else:
            origin = locs[origin][1]
    print(origin, step)
