LEFT = "<"
UP = "^"
RIGHT = ">"
DOWN = "v"


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


def find_sides(coords):
    result = []
    visited = set()

    def dfs(coord, group):
        if coord in visited:
            return
        visited.add(coord)
        neighbors = [
            (coord[0], (coord[1][0] - 1, coord[1][1])),
            (coord[0], (coord[1][0] + 1, coord[1][1])),
            (coord[0], (coord[1][0], coord[1][1] - 1)),
            (coord[0], (coord[1][0], coord[1][1] + 1)),
        ]
        for neighbor in neighbors:
            if neighbor in coords and neighbor not in group:
                group.append(neighbor)
                dfs(neighbor, group)

    for coord in coords:
        if coord not in visited:
            group = [coord]
            dfs(coord, group)
            result.append(group)

    return result


def find_external_neighbors(region):
    external_neighbors = []
    for i, j in region[1]:
        possible_neighbors = [
            (UP, (i - 1, j)),
            (DOWN, (i + 1, j)),
            (LEFT, (i, j - 1)),
            (RIGHT, (i, j + 1)),
        ]
        for pn in possible_neighbors:
            if pn[1] not in region[1]:
                external_neighbors.append(pn)

    return external_neighbors


with open("input.txt", "r") as f:
    garden = [list(x for x in line.strip()) for line in f.readlines()]
    regions = find_neighbors(garden)

    total_cost = 0
    for region in regions:
        total_cost += len(find_sides(find_external_neighbors(region))) * len(region[1])

    print(total_cost)
