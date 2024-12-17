import sys
import cupy as cp


def process_stone(stone):
    if cp.array(stone) == cp.array([0]):
        return cp.array([cp.array([1]), cp.array([-1])], dtype=cp.int64)

    else:
        num_str = cp.array2string(stone[0])
        if len(num_str) % 2 == 0:
            return cp.array(
                [
                    cp.array([cp.int64(num_str[: len(num_str) // 2])]),
                    cp.array([cp.int64(num_str[len(num_str) // 2 :])]),
                ],
                dtype=cp.int64,
            )

        else:
            new_stone_value = cp.multiply(cp.array(stone), cp.array([2024]))
            return cp.array([new_stone_value, cp.array([-1])], dtype=cp.int64)


def blink(line):
    result = cp.apply_along_axis(process_stone, 1, line)
    chained_result = cp.concatenate(result)
    new_line = cp.array(
        cp.reshape(chained_result[chained_result != cp.array([-1])], (-1, 1)),
        dtype=cp.int64,
    )

    return new_line


if __name__ == "__main__":
    if len(sys.argv) > 1:
        line = cp.array([[int(x)] for x in sys.argv[1].split(" ")], dtype=cp.int64)

        for i in range(75):
            print("BLINK ==>", i, "STONES ==>", len(line))
            line = blink(line)

        print("STONES AFTER 75 BLINKS ==>", len(line))
    else:
        print("No input line provided")
