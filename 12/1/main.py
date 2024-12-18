def find_neighbors(arr):
    result = []
    visited = set()

    def dfs(i, j, value):
        if (i, j) in visited:
            return []
        visited.add((i, j))
        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        group = [(i, j)]
        for x, y in neighbors:
            if 0 <= x < len(arr) and 0 <= y < len(arr[x]) and arr[x][y] == value:
                group.extend(dfs(x, y, value))
        return group

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            value = arr[i][j]
            if (i, j) not in visited:
                group = dfs(i, j, value)
                result.append((value, group))
    return result


def count_external_neighbors(region):
    external_neighbors = 0
    for i, j in region[1]:
        possible_neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for x, y in possible_neighbors:
            if (x, y) not in region[1]:
                external_neighbors += 1
    return external_neighbors


with open("input.txt", "r") as f:
    garden = [list(x for x in line.strip()) for line in f.readlines()]
    regions = find_neighbors(garden)

    total_cost = 0
    for region in regions:
        total_cost += count_external_neighbors(region) * len(region[1])

    print(total_cost)
