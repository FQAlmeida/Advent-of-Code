from pathlib import Path

from tqdm.auto import tqdm


if __name__ == "__main__":
    with Path("2023/Day_8/data/input.txt").open("r") as fd:
        lines = fd.readlines()
    dirs = lines[0].strip()
    locs = {line[:3]: (line[7:10], line.strip()[12:-1]) for line in lines[2:]}
    origins = list(filter(lambda loc: loc.endswith("A"), locs.keys()))
    len_dirs = len(dirs)
    step = 0
    with tqdm(total=1000000000) as pbar:
        while not all(map(lambda loc: loc.endswith("Z"), origins)):
            next_dir_index = step % len_dirs
            step += 1
            next_dir = dirs[next_dir_index]
            next_dir_s = 0 if next_dir == 'L' else 1
            for i, origin in enumerate(origins):
                origins[i] = locs[origin][next_dir_s]
            pbar.update(1)
    print(origins, step)
