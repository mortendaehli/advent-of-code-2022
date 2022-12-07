import re
from collections import defaultdict
from pathlib import Path

from aoc import logger

if __name__ == "__main__":
    logger.info("Day 7")
    with open("input.txt", "r") as file:
        data = file.read()

    navigate_down = re.compile("^\\$ cd")  # noqa
    file_size = "(d+) (?:[A-Za-z0-9]+)"

    total_directory_sizes = defaultdict(int)
    ROOT_PATH = Path("/")
    cwd = ROOT_PATH
    for line in data.splitlines()[1:]:
        if navigate_down.match(line):
            relative_path = line[5:]
            if relative_path == "..":
                cwd = cwd.parent
            else:
                cwd = cwd / relative_path
        if line.split(" ")[0].isnumeric():
            file_size = int(line.split(" ")[0])
            total_directory_sizes[cwd] += file_size
            for parent in cwd.parents:
                total_directory_sizes[parent] += file_size

    result_part_1 = sum([v for k, v in total_directory_sizes.items() if v <= 100000])

    TOTAL_DISK_SPACE = 70000000
    MIN_FREE_SPACE = 30000000
    current_usage = total_directory_sizes[ROOT_PATH]
    result_part_2 = min(
        [v for k, v in total_directory_sizes.items() if TOTAL_DISK_SPACE - current_usage + v >= MIN_FREE_SPACE]
    )

    logger.info(
        "Find all of the directories with a total size of at most 100000. "
        "What is the sum of the total sizes of those directories?: "
        f"{result_part_1}"
    )

    logger.info(
        "Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. "
        "What is the total size of that directory?: "
        f"{result_part_2}"
    )
