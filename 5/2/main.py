with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    separator = lines.index("")
    rules = [r.split("|") for r in lines[:separator]]
    updates = [u.split(",") for u in lines[separator + 1 :]]
    corrected_middle_sum = 0

    def custom_bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                for rule in rules:
                    if arr[j] == rule[1] and arr[j + 1] == rule[0]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

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

        if not correct:
            corrected_update = custom_bubble_sort(update[:])
            corrected_middle_sum += int(corrected_update[len(corrected_update) // 2])

    print(corrected_middle_sum)
