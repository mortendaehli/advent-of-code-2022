from __future__ import annotations

from itertools import takewhile, zip_longest
from typing import List

from aoc import logger


def transpose(data: List[List[int]]) -> List[List[int]]:
    return list(zip_longest(*data, fillvalue=None))


if __name__ == "__main__":
    logger.info("Day 8")
    with open("input.txt", "r") as file:
        data = file.read()

    array = [list(map(int, line)) for line in data.splitlines()]
    array_transposed = transpose(array)

    array_part_1 = [[0] * len(row) for row in array]
    array_part_2 = [[1] * len(row) for row in array]

    for i, row in zip(range(len(array)), array):
        for j, column in zip(range(len(array[0])), array_transposed):
            val = array[i][j]
            if all(val > x for x in row[:j]):
                array_part_1[i][j] = 1
            elif all(val > x for x in row[j + 1 :]):
                array_part_1[i][j] = 1
            elif all(val > x for x in column[:i]):
                array_part_1[i][j] = 1
            elif all(val > x for x in column[i + 1 :]):
                array_part_1[i][j] = 1

    result_part_1 = sum(sum(row) for row in array_part_1)

    for i, row in zip(range(len(array)), array):
        for j, column in zip(range(len(array[0])), array_transposed):
            val = array[i][j]
            a, b, c, d = (
                len(list(takewhile(lambda x: x < val, row[:j][::-1]))) + 1,
                len(list(takewhile(lambda x: x < val, row[j + 1 :]))) + 1,
                len(list(takewhile(lambda x: x < val, column[:i][::-1]))) + 1,
                len(list(takewhile(lambda x: x < val, column[i + 1 :]))) + 1,
            )
            array_part_2[i][j] = min(a, j) * min(b, len(row) - (j + 1)) * min(c, i) * min(d, len(column) - (i + 1))

    result_part_2 = max(max(row) for row in array_part_2)

    logger.info(f"Consider your map; how many trees are visible from outside the grid?: {result_part_1}")  # 1776

    logger.info(  # 234416
        f"Consider each tree on your map. What is the highest scenic score possible for any tree?: {result_part_2}"
    )
