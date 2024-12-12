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
                if pair[0] not in antinodes:
                    antinodes.append(pair[0])
                if pair[1] not in antinodes:
                    antinodes.append(pair[1])

                (i1, j1) = pair[0]
                (i2, j2) = pair[1]

                if i1 < i2 and j1 > j2:
                    i_diff = i2 - i1
                    j_diff = j1 - j2

                    antinode_1 = (i1 - i_diff, j1 + j_diff)

                    while 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(
                        lines[0]
                    ):
                        if antinode_1 not in antinodes:
                            antinodes.append(antinode_1)

                        antinode_1 = (antinode_1[0] - i_diff, antinode_1[1] + j_diff)

                    antinode_2 = (i2 + i_diff, j2 - j_diff)
                    while 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(
                        lines[0]
                    ):
                        if antinode_2 not in antinodes:
                            antinodes.append(antinode_2)

                        antinode_2 = (antinode_2[0] + i_diff, antinode_2[1] - j_diff)

                elif i1 < i2 and j1 < j2:
                    i_diff = i2 - i1
                    j_diff = j2 - j1

                    antinode_1 = (i1 - i_diff, j1 - j_diff)
                    while 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(
                        lines[0]
                    ):
                        if antinode_1 not in antinodes:
                            antinodes.append(antinode_1)

                        antinode_1 = (antinode_1[0] - i_diff, antinode_1[1] - j_diff)

                    antinode_2 = (i2 + i_diff, j2 + j_diff)
                    while 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(
                        lines[0]
                    ):
                        if antinode_2 not in antinodes:
                            antinodes.append(antinode_2)

                        antinode_2 = (antinode_2[0] + i_diff, antinode_2[1] + j_diff)

                elif j1 == j2 and i1 < i2:
                    i_diff = i2 - i1

                    antinode_1 = (i1 - i_diff, j1)
                    while 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(
                        lines[0]
                    ):
                        if antinode_1 not in antinodes:
                            antinodes.append(antinode_1)

                        antinode_1 = (antinode_1[0] - i_diff, antinode_1[1])

                    antinode_2 = (i2 + i_diff, j2)

                    while 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(
                        lines[0]
                    ):
                        if antinode_2 not in antinodes:
                            antinodes.append(antinode_2)

                        antinode_2 = (antinode_2[0] + i_diff, antinode_2[1])

                elif i1 == i2 and j1 < j2:
                    j_diff = j2 - j1

                    antinode_1 = (i1, j1 - j_diff)
                    while 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(
                        lines[0]
                    ):
                        if antinode_1 not in antinodes:
                            antinodes.append(antinode_1)

                        antinode_1 = (antinode_1[0], antinode_1[1] - j_diff)

                    antinode_2 = (i2, j2 + j_diff)
                    while 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(
                        lines[0]
                    ):
                        if antinode_2 not in antinodes:
                            antinodes.append(antinode_2)

                        antinode_2 = (antinode_2[0], antinode_2[1] + j_diff)

    print(len(antinodes))
