import re

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    mul_matches = []
    mul_pattern = r"mul\((\d+),(\d+)\)"
    for line in lines:
        matches = re.findall(mul_pattern, line)
        mul_matches += matches

    num_pattern = r"\d+"
    uncorrupted_sum = 0
    for mul_match in mul_matches:
        uncorrupted_sum += int(mul_match[0]) * int(mul_match[1])

    print(uncorrupted_sum)
