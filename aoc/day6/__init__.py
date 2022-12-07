from aoc import logger

if __name__ == "__main__":
    logger.info("Day 6")
    with open("input.txt", "r") as file:
        data = file.read()

    #
    def func(n):
        """
        Note that this function is of O(nk) and can be done at O(n) by using a more efficiency rolling window algorithm.
        """
        return next(i for i in range(len(data)) if len(set(data[i - n : i])) == n)

    logger.info(
        "How many characters need to be processed before the first start-of-packet marker is detected?: " f"{func(4)}"
    )

    logger.info(
        "How many characters need to be processed before the first start-of-message marker is detected?: " f"{func(14)}"
    )
