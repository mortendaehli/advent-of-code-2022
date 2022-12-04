from aoc import logger

if __name__ == "__main__":
    logger.info("Day 4")

    with open("input.txt", "r") as file:
        data = file.read().strip().split("\n")

    result_part_1 = 0
    result_part_2 = 0
    for pair in data:
        a, b = pair.split(",")
        a_start, a_stop = map(int, a.split("-"))
        b_start, b_stop = map(int, b.split("-"))
        a_set = set(range(a_start, a_stop + 1))
        b_set = set(range(b_start, b_stop + 1))

        if not a_set - b_set:
            result_part_1 += 1
        elif not b_set - a_set:
            result_part_1 += 1

        if a_set.intersection(b_set):
            result_part_2 += 1

    logger.info(f"In how many assignment pairs does one range fully contain the other?: {result_part_1}")

    logger.info(f"In how many assignment pairs do the ranges overlap?: {result_part_2}")
