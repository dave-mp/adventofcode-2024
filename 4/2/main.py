import re

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    times = 0

    for i, line in enumerate(lines):
        for j in range(len(line)):
            if (
                lines[i][j] == "A"
                and 0 <= i - 1
                and i + 1 < len(lines)
                and 0 <= j - 1
                and j + 1 < len(line)
            ):
                if (
                    (lines[i + 1][j + 1] == "S" and lines[i - 1][j - 1] == "M")
                    or (lines[i + 1][j + 1] == "M" and lines[i - 1][j - 1] == "S")
                ) and (
                    (lines[i - 1][j + 1] == "S" and lines[i + 1][j - 1] == "M")
                    or (lines[i - 1][j + 1] == "M" and lines[i + 1][j - 1] == "S")
                ):
                    times += 1

    print(times)
