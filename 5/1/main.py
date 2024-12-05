with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    separator = lines.index("")
    rules = [r.split("|") for r in lines[:separator]]
    updates = [u.split(",") for u in lines[separator + 1 :]]
    correct_middle_sum = 0

    for update in updates:
        correct = True
        for index, page in enumerate(update):
            for rule in rules:
                if index > 0 and page == rule[0] and rule[1] in update[:index]:
                    correct = False
                    break
                if (
                    index < len(update) - 1
                    and page == rule[1]
                    and rule[0] in update[index + 1 :]
                ):
                    correct = False
                    break
            if not correct:
                break

        if correct:
            correct_middle_sum += int(update[len(update) // 2])

    print(correct_middle_sum)
