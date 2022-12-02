from aoc import logger

if __name__ == "__main__":
    logger.info("Day 2")

    """
    We map the whole outcome space into a dictionary since we only have 9 outcomes:
    shape_scores:
        X: 1  # Rock
        Y: 2,  # Paper
        Z: 3,  # Scissors

    outcome_scores:
        win: 6
        draw: 3
        lose: 0
    """

    strategy = {
        "A": {"X": 3 + 1, "Y": 6 + 2, "Z": 0 + 3},  # Opponent Rock
        "B": {"X": 0 + 1, "Y": 3 + 2, "Z": 6 + 3},  # Opponent Paper
        "C": {"X": 6 + 1, "Y": 0 + 2, "Z": 3 + 3},  # Opponent Scissors
    }

    with open("input.txt", "r") as file:
        data = file.read().strip().split("\n")

    games = [game.split() for game in data]
    result_part_1 = sum([strategy[opponent_shape][my_shape] for opponent_shape, my_shape in games])

    logger.info(
        f"What would your total score be if everything goes exactly according to your strategy guide?: {result_part_1}"
    )  # 17189

    new_strategy = {
        "A": {"X": 0 + 3, "Y": 3 + 1, "Z": 6 + 2},  # Opponent Rock
        "B": {"X": 0 + 1, "Y": 3 + 2, "Z": 6 + 3},  # Opponent Paper
        "C": {"X": 0 + 2, "Y": 3 + 3, "Z": 6 + 1},  # Opponent Scissors
    }

    result_part_2 = sum([new_strategy[opponent_shape][my_shape] for opponent_shape, my_shape in games])
    logger.info(
        "Following the Elf's instructions for the second column, what would your total score be if everything goes "
        f"exactly according to your strategy guide?: {result_part_2}"
    )
