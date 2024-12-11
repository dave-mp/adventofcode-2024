import itertools

TIMES = "*"
PLUS = "+"

operands = [TIMES, PLUS]

with open("input.txt", "r") as f:
    equations = [
        [
            int(line.strip().split(":")[0]),
            list(int(x) for x in line.split(":")[1].strip().split(" ")),
        ]
        for line in f.readlines()
    ]

    total_calibration_result = 0

    for equation in equations:
        test_value = equation[0]
        numbers = equation[1]
        operand_sequences = list(itertools.product(operands, repeat=len(equation[1])))

        for operand_sequence in operand_sequences:
            result = None
            for i in range(len(numbers)):
                if i == 0:
                    result = numbers[0]
                else:
                    operand = operand_sequence[i - 1]
                    if operand == TIMES:
                        result *= numbers[i]
                    else:
                        result += numbers[i]

            if result == test_value:
                total_calibration_result += test_value
                break

    print(total_calibration_result)
