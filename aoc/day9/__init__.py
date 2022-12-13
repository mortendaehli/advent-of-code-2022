from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from aoc import logger


@dataclass
class Coordinate:
    x: int
    y: int

    def delta(self, other: Coordinate) -> Tuple[int, int]:
        return self.x - other.x, self.y - other.y

    def __hash__(self) -> int:
        val = (self.x, self.y)
        return val.__hash__()

    def __repr__(self) -> str:
        return str((self.x, self.y))

    def __str__(self) -> str:
        return self.__repr__()


def sign(x: int):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


if __name__ == "__main__":
    logger.info("Day 9")
    with open("input.txt", "r") as file:
        data = file.read()

    rope = [[Coordinate(x=0, y=0)] for _ in range(10)]
    for move in data.splitlines():
        direction = move.split()[0]
        number = int(move.split()[1])
        for i in range(number):
            match direction:
                case "L":
                    rope[0].append(Coordinate(x=rope[0][-1].x - 1, y=rope[0][-1].y))
                case "R":
                    rope[0].append(Coordinate(x=rope[0][-1].x + 1, y=rope[0][-1].y))
                case "U":
                    rope[0].append(Coordinate(x=rope[0][-1].x, y=rope[0][-1].y + 1))
                case "D":
                    rope[0].append(Coordinate(x=rope[0][-1].x, y=rope[0][-1].y - 1))

            for n in range(1, len(rope)):
                dx, dy = rope[n][-1].delta(rope[n - 1][-1])
                x, y = rope[n][-1].x, rope[n][-1].y
                if dx == 0 or dy == 0:
                    if abs(dx) >= 2:
                        x -= sign(dx)
                    if abs(dy) >= 2:
                        y -= sign(dy)
                elif (abs(dx), abs(dy)) != (1, 1):
                    x -= sign(dx)
                    y -= sign(dy)
                rope[n].append(Coordinate(x, y))

        pass

    result_part_1 = len(set(rope[1]))
    result_part_2 = len(set(rope[-1]))

    logger.info(  # 5710
        f"Simulate your complete hypothetical series of motions. "
        f"How many positions does the tail of the rope visit at least once?: {result_part_1}"
    )

    logger.info(  # 2259
        f"Simulate your complete series of motions on a larger rope with ten knots. "
        f"How many positions does the tail of the rope visit at least once?: {result_part_2}"
    )
