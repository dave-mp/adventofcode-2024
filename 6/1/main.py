LEFT = "<"
UP = "^"
RIGHT = ">"
DOWN = "v"
ORIENTATIONS = [LEFT, UP, RIGHT, DOWN]
OBSTACLE = "#"
VISITED = "x"


def current_position(map_):
    for i, line in enumerate(map_):
        for j, char in enumerate(line):
            if char in ORIENTATIONS:
                return i, j
    return None


def next_state(map_, current_position):
    (i, j) = current_position
    orientation = map_[i][j]
    map_[i][j] = VISITED
    next_position = None
    next_orientation = None

    if orientation == UP:
        if (i - 1) >= 0:
            if map_[i - 1][j] == OBSTACLE and (j + 1) < len(map_[i]):
                next_position = (i, j + 1)
                next_orientation = RIGHT
            else:
                next_position = (i - 1, j)
                next_orientation = UP
    elif orientation == RIGHT:
        if (j + 1) < len(map_[i]):
            if map_[i][j + 1] == OBSTACLE and (i + 1) < len(map_):
                next_position = (i + 1, j)
                next_orientation = DOWN
            else:
                next_position = (i, j + 1)
                next_orientation = RIGHT
    elif orientation == DOWN:
        if (i + 1) < len(map_):
            if map_[i + 1][j] == OBSTACLE and (j - 1) >= 0:
                next_position = (i, j - 1)
                next_orientation = LEFT
            else:
                next_position = (i + 1, j)
                next_orientation = DOWN
    elif orientation == LEFT:
        if (j - 1) >= 0:
            if map_[i][j - 1] == OBSTACLE and (i - 1) >= 0:
                next_position = (i - 1, j)
                next_orientation = UP
            else:
                next_position = (i, j - 1)
                next_orientation = LEFT

    new_map = map_[:]
    new_map[i][j] = VISITED

    if next_position and next_orientation:
        (n, m) = next_position
        new_map[n][m] = next_orientation

    return (new_map, next_position)


def print_map(map_):
    print("\n".join(["".join(line) for line in map_]))


def count_visited(map_):
    c = 0
    for line in map_:
        for position in line:
            if position == VISITED:
                c += 1
    return c


it = 0
with open("input.txt", "r") as f:
    map_ = [list(line.strip()) for line in f.readlines()]
    position = current_position(map_)
    print_map(map_)

    while position:
        (map_, position) = next_state(map_, position)
        it += 1

    print(f"\nITERATION {it} RESULT:", position)
    print_map(map_)
    print(count_visited(map_))
