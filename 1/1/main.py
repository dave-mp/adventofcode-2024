list_1 = []
list_2 = []
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
        values = line.split("   ")
        list_1.append(int(values[0]))
        list_2.append(int(values[1]))

    list_1.sort()
    list_2.sort()

    distance = 0
    for i in range(len(list_1)):
        distance += abs(list_1[i] - list_2[i])

    print(distance)
