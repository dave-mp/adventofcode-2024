from collections import deque
from tqdm import tqdm


def least_expensive_path(a, b, p):
    """
    Find the least expensive path to reach the goal p using steps a and b.

    Args:
        a (tuple): Step a = (x1, y1)
        b (tuple): Step b = (x2, y2)
        p (tuple): Goal p = (x, y)

    Returns:
        tuple: (cost, path) if a path is found, otherwise None
    """
    # Define the cost of each step
    cost_a = 3
    cost_b = 1

    # Create a queue for BFS, containing the initial state
    queue = deque([(0, 0, 0, [])])  # (x, y, cost, path)

    # Create a set to store visited states
    visited = set((0, 0))

    # Set a maximum number of steps based on the smallest type of step
    max_steps = p[0] // min(a[0], b[0]) + p[1] // min(a[1], b[1])

    while queue:
        x, y, cost, path = queue.popleft()

        # If we've reached the goal, return the cost and path
        if (x, y) == p:
            return (cost, path)

        # If we've exceeded the maximum number of steps, terminate
        if len(path) >= max_steps:
            return None

        # Explore neighbors using step a
        nx, ny = x + a[0], y + a[1]
        if (nx, ny) not in visited:
            queue.append((nx, ny, cost + cost_a, path + ["a"]))
            visited.add((nx, ny))

        # Explore neighbors using step b
        nx, ny = x + b[0], y + b[1]
        if (nx, ny) not in visited:
            queue.append((nx, ny, cost + cost_b, path + ["b"]))
            visited.add((nx, ny))

    # If no path is found, return None
    return None


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line != "\n"]
    plain_machines = [lines[i : i + 3] for i in range(0, len(lines), 3)]
    machines_config = []

    for pm in plain_machines:
        a = pm[0].split(":")
        a_x = a[1].split(",")[0].split("+")[1].strip()
        a_y = a[1].split(",")[1].split("+")[1].strip()

        b = pm[1].split(":")
        b_x = b[1].split(",")[0].split("+")[1].strip()
        b_y = b[1].split(",")[1].split("+")[1].strip()

        prize = pm[2].split(":")
        p_x = prize[1].split(",")[0].split("=")[1].strip()
        p_y = prize[1].split(",")[1].split("=")[1].strip()

        machines_config.append(
            {
                "a": {"x": int(a_x), "y": int(a_y)},
                "b": {"x": int(b_x), "y": int(b_y)},
                "prize": {"x": int(p_x), "y": int(p_y)},
            }
        )

    fewest_tokens = 0
    for mc in tqdm(machines_config):
        a = (mc["a"]["x"], mc["a"]["y"])
        b = (mc["b"]["x"], mc["b"]["y"])
        p = (mc["prize"]["x"], mc["prize"]["y"])
        result = least_expensive_path(a, b, p)

        if result:
            fewest_tokens += result[0]

    print(f"Fewest tokens: {fewest_tokens}")
