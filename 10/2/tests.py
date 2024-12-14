import unittest
from main import get_score_sum, get_trail_goals, get_trail_heads, get_viable_moves

full_map_1 = [
    [8, 9, 0, 1, 0, 1, 2, 3],
    [7, 8, 1, 2, 1, 8, 7, 4],
    [8, 7, 4, 3, 0, 9, 6, 5],
    [9, 6, 5, 4, 9, 8, 7, 4],
    [4, 5, 6, 7, 8, 9, 0, 3],
    [3, 2, 0, 1, 9, 0, 1, 2],
    [0, 1, 3, 2, 9, 8, 0, 1],
    [1, 0, 4, 5, 6, 7, 3, 2],
]

full_map_2 = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [9, 9, 9, 9, 9, 9, 1, 8],
    [9, 9, 9, 9, 9, 9, 1, 9],
    [9, 9, 9, 9, 9, 9, 1, 1],
    [9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9],
]


class TestDefragmentFile(unittest.TestCase):
    def test_get_trail_heads(self):
        assert get_trail_heads(full_map_1) == [
            (0, 2),
            (0, 4),
            (2, 4),
            (4, 6),
            (5, 2),
            (5, 5),
            (6, 0),
            (6, 6),
            (7, 1),
        ]

    def test_get_viable_moves(self):
        assert get_viable_moves((0, 2), full_map_1) == [(0, 3), (1, 2)]

    def test_get_trail_goals(self):
        assert get_trail_goals((0, 2), full_map_2) == [(2, 7)]

    def test_get_score_sum(self):
        assert get_score_sum(get_trail_heads(full_map_1), full_map_1) == 36


if __name__ == "__main__":
    unittest.main()
