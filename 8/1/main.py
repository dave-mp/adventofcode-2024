import itertools
from tqdm import tqdm

EMPTY = "."

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    antennas = {}

    for i, line in tqdm(enumerate(lines)):
        for j, value in enumerate(line):
            if value != EMPTY:
                antenna_locations = (
                    antennas[value][:] if value in list(antennas.keys()) else []
                )
                antenna_locations.append((i, j))
                antennas[value] = antenna_locations[:]

    antinodes = []

    for key in tqdm(list(antennas.keys())):
        if len(antennas[key]) > 1:
            pairs = list(itertools.combinations(antennas[key], 2))

            for pair in pairs:
                (i1, j1) = pair[0]
                (i2, j2) = pair[1]

                if i1 < i2 and j1 > j2:
                    antinode_1 = (i1 - (i2 - i1), j1 + (j1 - j2))
                    if 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(
                        lines[0]
                    ):
                        if antinode_1 not in antinodes:
                            antinodes.append(antinode_1)

                    antinode_2 = (i2 + (i2 - i1), j2 - (j1 - j2))
                    if 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(
                        lines[0]
                    ):
                        if antinode_2 not in antinodes:
                            antinodes.append(antinode_2)

                elif i1 < i2 and j1 < j2:
                    antinode_1 = (i1 - (i2 - i1), j1 - (j2 - j1))
                    if 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(
                        lines[0]
                    ):
                        if antinode_1 not in antinodes:
                            antinodes.append(antinode_1)

                    antinode_2 = (i2 + (i2 - i1), j2 + (j2 - j1))
                    if 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(
                        lines[0]
                    ):
                        if antinode_2 not in antinodes:
                            antinodes.append(antinode_2)

                elif j1 == j2 and i1 < i2:
                    antinode_1 = (i1 - (i2 - i1), j1)
                    if 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(
                        lines[0]
                    ):
                        if antinode_1 not in antinodes:
                            antinodes.append(antinode_1)

                    antinode_2 = (i2 + (i2 - i1), j2)
                    if 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(
                        lines[0]
                    ):
                        if antinode_2 not in antinodes:
                            antinodes.append(antinode_2)

                elif i1 == i2 and j1 < j2:
                    antinode_1 = (i1, j1 - (j2 - j1))
                    if 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(
                        lines[0]
                    ):
                        if antinode_1 not in antinodes:
                            antinodes.append(antinode_1)

                    antinode_2 = (i2, j2 + (j2 - j1))
                    if 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(
                        lines[0]
                    ):
                        if antinode_2 not in antinodes:
                            antinodes.append(antinode_2)

    print(len(antinodes))
