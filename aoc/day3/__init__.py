import string

from aoc import logger

if __name__ == "__main__":
    logger.info("Day 3")

    alpha_dict = {k: ord(k) % 32 for k in string.ascii_lowercase}
    alpha_dict.update({k: ord(k) % 32 + 26 for k in string.ascii_uppercase})

    with open("input.txt", "r") as file:
        data = file.read().strip().split("\n")

    result_part_1 = 0
    for rucksack in data:
        length = int(len(rucksack) / 2)
        a, b = rucksack[:length], rucksack[length:]
        duplicate = set(a).intersection(set(b))
        for alpha in duplicate:
            result_part_1 += alpha_dict[alpha]

    logger.info(
        "Find the item type that appears in both compartments of each rucksack. "
        f"What is the sum of the priorities of those item types?: {result_part_1}"
    )

    result_part_2 = 0
    for i in range(0, len(data), 3):
        intersect = set(string.ascii_letters)
        for j in range(3):
            intersect = intersect.intersection(set(data[i + j]))
        for alpha in intersect:
            result_part_2 += alpha_dict[alpha]

    logger.info(
        f"Find the item type that corresponds to the badges of each three-Elf group. "
        f"What is the sum of the priorities of those item types?: {result_part_2}"
    )
