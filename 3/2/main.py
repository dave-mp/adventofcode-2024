import re

with open("input.txt", "r") as f:
    split_input = f.read().split("do()")

    mul_matches = []
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"

    for section in split_input:
        split_section = section.split("don't()")
        matches = re.findall(mul_pattern, split_section[0])
        mul_matches.extend(matches)

    num_pattern = r"\d+"
    uncorrupted_sum = 0
    for mul_match in mul_matches:
        num_match = re.findall(num_pattern, mul_match)
        uncorrupted_sum += int(num_match[0]) * int(num_match[1])

    print(uncorrupted_sum)
