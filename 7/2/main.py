import itertools
from tqdm import tqdm

TIMES = "*"
PLUS = "+"
JOIN = "||"
operands = [TIMES, PLUS, JOIN]

with open("input.txt", "r") as f:
    equations = [
        [
            int(line.strip().split(":")[0]),
            line.split(":")[1].strip().split(" "),
        ]
        for line in f.readlines()
    ]

    total_calibration_result = 0
    solved_equations = []

    for equation in tqdm(equations):
        test_value = equation[0]
        numbers = equation[1]
        operand_sequences = list(
            itertools.product(operands, repeat=(len(equation[1]) - 1))
        )

        for operand_sequence in operand_sequences:
            for i in range(len(numbers)):
                if i == 0:
                    result = int(numbers[0])
                else:
                    operand = operand_sequence[i - 1]
                    if operand == TIMES:
                        result *= int(numbers[i])
                    elif operand == PLUS:
                        result += int(numbers[i])
                    elif operand == JOIN:
                        result = int(f"{result}{numbers[i]}")

                if result > test_value:
                    break

            if result == test_value:
                total_calibration_result += test_value
                solved_equations.append(equation)
                break

    for equation in solved_equations:
        print(equation)

    print(total_calibration_result)
