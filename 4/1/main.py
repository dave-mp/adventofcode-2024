import re

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    word = "XMAS"
    times = 0

    for i, line in enumerate(lines):
        for j in range(len(line)):
            if j + 3 < len(line):
                if "".join(line[j : j + 4]) == word:
                    times += 1

            if j - 3 >= 0:
                segment = []
                for k in range(4):
                    segment.append(line[j - k])
                if "".join(segment) == word:
                    times += 1

            if i + 3 < len(lines):
                segment = []
                for k in range(4):
                    segment.append(lines[i + k][j])
                if "".join(segment) == word:
                    times += 1

            if i - 3 >= 0:
                segment = []
                for k in range(4):
                    segment.append(lines[i - k][j])
                if "".join(segment) == word:
                    times += 1

            if j + 3 < len(line) and i + 3 < len(lines):
                segment = []
                for k in range(4):
                    segment.append(lines[i + k][j + k])
                if "".join(segment) == word:
                    times += 1

            if j + 3 < len(line) and i - 3 >= 0:
                segment = []
                for k in range(4):
                    segment.append(lines[i - k][j + k])
                if "".join(segment) == word:
                    times += 1

            if j - 3 >= 0 and i - 3 >= 0:
                segment = []
                for k in range(4):
                    segment.append(lines[i - k][j - k])
                if "".join(segment) == word:
                    times += 1

            if j - 3 >= 0 and i + 3 < len(lines):
                segment = []
                for k in range(4):
                    segment.append(lines[i + k][j - k])
                if "".join(segment) == word:
                    times += 1

    print(times)
