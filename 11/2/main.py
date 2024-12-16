import sys
import numpy as np
import itertools
from tqdm import tqdm


def process_stone(stone):
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        return [stone[: len(stone) // 2], f"{int(stone[len(stone) // 2 :])}"]
    else:
        return [f"{int(stone) * 2024}"]


def blink(line):
    vectorized_func = np.frompyfunc(process_stone, 1, 1)
    result = vectorized_func(np.array(line, str))
    new_line = list(itertools.chain(*result))

    return new_line


if __name__ == "__main__":
    if len(sys.argv) > 1:
        line = sys.argv[1].split(" ")

        for i in range(75):
            print("BLINK ==>", i, "STONES ==>", len(line), end="\r")
            line = blink(line)

        print("STONES AFTER 25 BLINKS ==>", len(line))
    else:
        print("No input line provided")
