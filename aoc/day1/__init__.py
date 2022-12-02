from aoc import logger

if __name__ == "__main__":
    logger.info("Day 1")
    with open("input.txt", "r") as file:
        data = file.read().strip()

    result_part_1 = max([sum([int(x) for x in elf.split("\n")]) for elf in data.split("\n\n")])
    logger.info(
        f"Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?: {result_part_1}"
    )

    result_part_2 = sum(sorted([sum([int(x) for x in elf.split("\n")]) for elf in data.split("\n\n")])[-3:])
    logger.info(
        f"Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?: "
        f"{result_part_2}"
    )
