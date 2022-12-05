import re
from collections import defaultdict, deque
from typing import DefaultDict

from aoc import logger


def parse_stack_data(data: str) -> DefaultDict[int, deque]:
    crates = defaultdict(deque)
    for row in data.splitlines()[:-1]:
        for i, value in enumerate(row[1::4]):
            if value.strip():
                crates[i + 1].appendleft(value)
    return crates


def do_part_1(stack_data: str) -> str:
    stacks = parse_stack_data(stack_data)
    for action in rearrangements.splitlines():
        amount, from_stack, to_stack = map(int, re.findall(r"\d+", action))
        stacks[to_stack].extend([stacks[from_stack].pop() for _ in range(int(amount))])

    return "".join([stacks[i][-1] for i in range(1, 10)])


def do_part_2(stack_data: str) -> str:
    stacks = parse_stack_data(stack_data)
    for action in rearrangements.splitlines():
        amount, from_stack, to_stack = map(int, re.findall(r"\d+", action))
        stacks[to_stack].extend(reversed([stacks[from_stack].pop() for _ in range(int(amount))]))

    return "".join([stacks[i][-1] for i in range(1, 10)])


if __name__ == "__main__":
    logger.info("Day 5")

    with open("input.txt", "r") as file:
        stack_data, rearrangements = file.read().split("\n\n")

    result_part_1 = do_part_1(stack_data)
    logger.info(
        f"After the rearrangement procedure completes, what crate ends up on top of each stack?: {result_part_1}"
    )

    result_part_2 = do_part_2(stack_data)
    logger.info(
        f"After the rearrangement procedure completes, what crate ends up on top of each stack?: {result_part_2}"
    )
