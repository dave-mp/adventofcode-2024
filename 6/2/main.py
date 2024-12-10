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


class LoopReachedException(Exception):
    pass


def current_position(map_):
    for i, line in enumerate(map_):
        for j, char in enumerate(line):
            if char in ORIENTATIONS:
                return i, j
    return None


def next_state(
    current_map,
    current_position,
    previous_value,
    position_orientation=None,
    seen_obstacles=None,
):
    (i, j) = current_position
    new_map = current_map[:]
    orientation = position_orientation if position_orientation else new_map[i][j]
    next_position = None
    next_orientation = None

    if orientation == UP:
        if (i - 1) >= 0:
            if new_map[i - 1][j] == OBSTACLE:
                if seen_obstacles is not None:
                    if ((i - 1, j), orientation) in seen_obstacles:
                        raise LoopReachedException
                    else:
                        seen_obstacles.append(((i - 1, j), orientation))

                if (j + 1) < len(new_map[i]):
                    return next_state(
                        new_map,
                        current_position,
                        VISITED_VERTICAL,
                        RIGHT,
                        seen_obstacles,
                    )
            else:
                next_position = (i - 1, j)
                next_orientation = UP
    elif orientation == RIGHT:
        if (j + 1) < len(new_map[i]):
            if new_map[i][j + 1] == OBSTACLE:
                if seen_obstacles is not None:
                    if ((i, j + 1), orientation) in seen_obstacles:
                        raise LoopReachedException
                    else:
                        seen_obstacles.append(((i, j + 1), orientation))

                if (i + 1) < len(new_map):
                    return next_state(
                        new_map,
                        current_position,
                        VISITED_HORIZONTAL,
                        DOWN,
                        seen_obstacles,
                    )
            else:
                next_position = (i, j + 1)
                next_orientation = RIGHT
    elif orientation == DOWN:
        if (i + 1) < len(new_map):
            if new_map[i + 1][j] == OBSTACLE:
                if seen_obstacles is not None:
                    if ((i + 1, j), orientation) in seen_obstacles:
                        raise LoopReachedException
                    else:
                        seen_obstacles.append(((i + 1, j), orientation))

                if (j - 1) >= 0:
                    return next_state(
                        new_map,
                        current_position,
                        VISITED_VERTICAL,
                        LEFT,
                        seen_obstacles,
                    )
            else:
                next_position = (i + 1, j)
                next_orientation = DOWN
    elif orientation == LEFT:
        if (j - 1) >= 0:
            if new_map[i][j - 1] == OBSTACLE:
                if seen_obstacles is not None:
                    if ((i, j - 1), orientation) in seen_obstacles:
                        raise LoopReachedException
                    else:
                        seen_obstacles.append(((i, j - 1), orientation))

                if (i - 1) >= 0:
                    return next_state(
                        new_map,
                        current_position,
                        VISITED_HORIZONTAL,
                        UP,
                        seen_obstacles,
                    )
            else:
                next_position = (i, j - 1)
                next_orientation = LEFT

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

    return (
        new_map,
        next_position,
        previous_value,
    )


def print_map(map_):
    print("\n".join(["".join(line) for line in map_]), end="\n\n")


def get_visited(map_):
    visited_positions = []
    for i, line in enumerate(map_):
        for j, cell in enumerate(line):
            position = (i, j)
            if (
                cell in [VISITED_CORNER, VISITED_HORIZONTAL, VISITED_VERTICAL]
                and position not in visited_positions
            ):
                visited_positions.append(position)
    return visited_positions


def check_loop(new_map, step):
    try:
        map_ = new_map[:]

        map_[step[0]][step[1]] = OBSTACLE

        position = current_position(map_)
        previous_value = NOT_VISITED
        seen_obstacles = []

        while position:
            try:
                (map_, position, previous_value) = next_state(
                    map_, position, previous_value, seen_obstacles=seen_obstacles
                )
            except LoopReachedException:
                # print_map(map_)
                return True

            seen_obstacles_set = set(seen_obstacles)
            if len(seen_obstacles_set) != len(seen_obstacles):
                return True

    except IndexError:
        return False

    return False


def draw_path(map_):
    it = 0
    position = current_position(map_)
    print_map(map_)
    previous_value = NOT_VISITED

    while position:
        (map_, position, previous_value) = next_state(map_, position, previous_value)
        it += 1

    # print(f"\nITERATION {it} RESULT:", position)
    # print_map(map_)

    return map_


with open("input.txt", "r") as f:
    drawn_map = draw_path([list(line.strip()) for line in f.readlines()])
    path = get_visited(drawn_map)
    print("VISITED POSITIONS: ", len(path))

    loop_positions = []

    for step in path[:]:
        if step not in loop_positions:
            with open("input.txt", "r") as f2:
                original_map = [list(line.strip()) for line in f2.readlines()]
                causes_loop = check_loop(original_map, step)
                if causes_loop and step not in loop_positions:
                    loop_positions.append(step)

    print("LOOP CAUSING POSITIONS: ", len(loop_positions))
