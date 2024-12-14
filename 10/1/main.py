def get_viable_moves(current_position, full_map):
    current_height = full_map[current_position[0]][current_position[1]]
    viable_moves = []

    if current_position[1] - 1 >= 0:
        if full_map[current_position[0]][current_position[1] - 1] - current_height == 1:
            viable_moves.append((current_position[0], current_position[1] - 1))

    if current_position[1] + 1 < len(full_map[0]):
        if full_map[current_position[0]][current_position[1] + 1] - current_height == 1:
            viable_moves.append((current_position[0], current_position[1] + 1))

    if current_position[0] - 1 >= 0:
        if full_map[current_position[0] - 1][current_position[1]] - current_height == 1:
            viable_moves.append((current_position[0] - 1, current_position[1]))

    if current_position[0] + 1 < len(full_map):
        if full_map[current_position[0] + 1][current_position[1]] - current_height == 1:
            viable_moves.append((current_position[0] + 1, current_position[1]))

    return viable_moves


def get_trail_heads(full_map):
    trail_heads = []

    for i, row in enumerate(full_map):
        for j, height in enumerate(row):
            if height == 0:
                trail_heads.append((i, j))

    return trail_heads


def get_trail_goals(trail_head, full_map):
    trail_goals = []
    moves = [trail_head]

    while len(moves) > 0:
        current_position = moves.pop(0)
        viable_moves = get_viable_moves(current_position, full_map)
        moves.extend(viable_moves)

        if (
            full_map[current_position[0]][current_position[1]] == 9
            and current_position not in trail_goals
        ):
            trail_goals.append(current_position)

        if len(viable_moves) == 0 and len(moves) == 0:
            break

    return trail_goals


def get_score_sum(trail_heads, full_map):
    score_sum = 0
    for trail_head in trail_heads:
        head_goals = get_trail_goals(trail_head, full_map)
        score_sum += len(head_goals)

    return score_sum


with open("input.txt", "r") as f:
    full_map = [list(int(x) for x in line.strip()) for line in f.readlines()]
    score_sum = get_score_sum(get_trail_heads(full_map), full_map)
    print(score_sum)
