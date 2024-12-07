LEFT = "<"
UP = "^"
RIGHT = ">"
DOWN = "v"
ORIENTATIONS = [LEFT, UP, RIGHT, DOWN]
OBSTACLE = "#"
NOT_VISITED = "."
VISITED_VERTICAL = "|"
VISITED_HORIZONTAL = "-"
VISITED_CORNER = "+"


def current_position(map_):
    for i, line in enumerate(map_):
        for j, char in enumerate(line):
            if char in ORIENTATIONS:
                return i, j
    return None


def next_state(map_, current_position, looping_obstacles, previous_value):
    (i, j) = current_position
    orientation = map_[i][j]
    next_position = None
    next_orientation = None
    new_map = map_[:]
    potential_obstacles = looping_obstacles[:]

    if orientation == UP:
        if (i - 1) >= 0:
            if map_[i - 1][j] == OBSTACLE and (j + 1) < len(map_[i]):
                next_position = (i, j + 1)
                next_orientation = RIGHT
            else:
                next_position = (i - 1, j)
                next_orientation = UP

            if (
                next_orientation == UP
                and (i - 2) >= 0
                and (i - 2, j) not in potential_obstacles
            ):
                a = j + 2
                while a < len(map_[i - 1]):
                    if (
                        map_[i - 1][a] == OBSTACLE
                        and map_[i - 1][a - 1] == VISITED_CORNER
                    ):
                        potential_obstacles.append((i - 2, j))
                        break
                    a += 1
            elif (
                next_orientation == RIGHT
                and (j + 2) < len(map_[i])
                and (i, j + 2) not in potential_obstacles
            ):
                a = i + 2
                while a < len(map_):
                    if (
                        map_[a][j + 1] == OBSTACLE
                        and map_[a - 1][j + 1] == VISITED_CORNER
                    ):
                        potential_obstacles.append((i, j + 2))
                        break
                    a += 1

    elif orientation == RIGHT:
        if (j + 1) < len(map_[i]):
            if map_[i][j + 1] == OBSTACLE and (i + 1) < len(map_):
                next_position = (i + 1, j)
                next_orientation = DOWN
            else:
                next_position = (i, j + 1)
                next_orientation = RIGHT

            if (
                next_orientation == RIGHT
                and (j + 2) < len(map_)
                and (i, j + 2) not in potential_obstacles
            ):
                a = i + 2
                while a < len(map_):
                    if (
                        map_[a][j + 1] == OBSTACLE
                        and map_[a - a][j + 1] == VISITED_CORNER
                    ):
                        potential_obstacles.append((i, j + 2))
                        break
                    a += 1
            elif (
                next_orientation == DOWN
                and (i + 2) < len(map_)
                and (i + 2, j) not in potential_obstacles
            ):
                a = j - 2
                while a >= 0:
                    if (
                        map_[i + 1][a] == OBSTACLE
                        and map_[i + 1][a - 1] == VISITED_CORNER
                    ):
                        potential_obstacles.append((i + 2, j))
                        break
                    a -= 1

    elif orientation == DOWN:
        if (i + 1) < len(map_):
            if map_[i + 1][j] == OBSTACLE and (j - 1) >= 0:
                next_position = (i, j - 1)
                next_orientation = LEFT
            else:
                next_position = (i + 1, j)
                next_orientation = DOWN

            if (
                next_orientation == DOWN
                and (i + 2) >= 0
                and (i + 2, j) not in potential_obstacles
            ):
                a = j - 2
                while a >= 0:
                    if map_[i + 1][a] == OBSTACLE and map_[i + 1][a] == VISITED_CORNER:
                        potential_obstacles.append((i + 2, j))
                        break
                    a -= 1
            elif (
                next_orientation == LEFT
                and (j - 2) >= 0
                and (i, j - 2) not in potential_obstacles
            ):
                a = i - 2
                while a >= 0:
                    if (
                        map_[a][j - 1] == OBSTACLE
                        and map_[a - 1][j - 1] == VISITED_CORNER
                    ):
                        potential_obstacles.append((i, j - 2))
                        break
                    a -= 1

    elif orientation == LEFT:
        if (j - 1) >= 0:
            if map_[i][j - 1] == OBSTACLE and (i - 1) >= 0:
                next_position = (i - 1, j)
                next_orientation = UP
            else:
                next_position = (i, j - 1)
                next_orientation = LEFT

            if (
                next_orientation == LEFT
                and (j - 2) >= 0
                and (i, j - 2) not in potential_obstacles
            ):
                a = i - 2
                while a >= 0:
                    if (
                        map_[a][j - 1] == OBSTACLE
                        and map_[a - 1][j - 1] == VISITED_CORNER
                    ):
                        potential_obstacles.append((i - 1, j))
                        break
                    a -= 1
            elif (
                next_orientation == UP
                and (i - 2) >= 0
                and (i - 2, j) not in potential_obstacles
            ):
                a = j + 2
                while a < len(map_[i]):
                    if (
                        map_[i - 1][a] == OBSTACLE
                        and map_[i - 1][a - 1] == VISITED_CORNER
                    ):
                        potential_obstacles.append((i - 2, j))
                        break
                    a += 1

    if previous_value == NOT_VISITED:
        if orientation == next_orientation:
            if orientation in [UP, DOWN]:
                new_map[i][j] = VISITED_VERTICAL
            elif orientation in [LEFT, RIGHT]:
                new_map[i][j] = VISITED_HORIZONTAL
        else:
            new_map[i][j] = VISITED_CORNER
    else:
        if orientation == next_orientation:
            if orientation in [UP, DOWN]:
                new_map[i][j] = (
                    VISITED_VERTICAL
                    if previous_value == VISITED_VERTICAL
                    else VISITED_CORNER
                )
            elif orientation in [LEFT, RIGHT]:
                new_map[i][j] = (
                    VISITED_HORIZONTAL
                    if previous_value == VISITED_HORIZONTAL
                    else VISITED_CORNER
                )
        else:
            new_map[i][j] = VISITED_CORNER

    if next_position and next_orientation:
        (n, m) = next_position
        previous_value = new_map[n][m]
        new_map[n][m] = next_orientation

    return (new_map, next_position, potential_obstacles, previous_value)


def print_map(map_):
    print("\n".join(["".join(line) for line in map_]))


def count_visited(map_):
    c = 0
    for line in map_:
        for position in line:
            if position in [VISITED_CORNER, VISITED_HORIZONTAL, VISITED_VERTICAL]:
                c += 1
    return c


it = 0
with open("input.txt", "r") as f:
    map_ = [list(line.strip()) for line in f.readlines()]
    position = current_position(map_)
    print_map(map_)
    looping_obstacles = []
    previous_value = NOT_VISITED

    while position:
        (map_, position, looping_obstacles, previous_value) = next_state(
            map_, position, looping_obstacles, previous_value
        )
        it += 1

    print(f"\nITERATION {it} RESULT:", position)
    print_map(map_)
    print(count_visited(map_), len(looping_obstacles))
