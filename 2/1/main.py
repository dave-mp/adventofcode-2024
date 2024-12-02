with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    safe_reports = 0
    for line in lines:
        values = line.split(" ")
        is_safe = True
        trend = ""

        for i in range((len(values) - 1)):
            diff = int(values[i]) - int(values[i + 1])

            if trend == "":
                if diff > 0:
                    trend = "up"
                else:
                    trend = "down"
            else:
                if (trend == "up" and diff < 1) or (trend == "down" and diff > -1):
                    is_safe = False

            variation = abs(diff)
            if variation < 1 or variation > 3:
                is_safe = False

        if is_safe:
            safe_reports += 1

    print(safe_reports)
