import unittest
import cupy as cp
from main import blink, process_stone


class TestDefragmentFile(unittest.TestCase):
    def test_process_stone_1(self):
        ps = process_stone([17])
        assert cp.all(ps == cp.array([[1], [7]], dtype=cp.int64))

    def test_process_stone_2(self):
        ps = process_stone([1])
        assert cp.all(ps == cp.array([[2024], [-1]], dtype=cp.int64))

    def test_process_stone_3(self):
        ps = process_stone([125])
        assert cp.all(ps == cp.array([[253000], [-1]], dtype=cp.int64))

    def test_process_stone_4(self):
        ps = process_stone([0])
        assert cp.all(ps == cp.array([[1], [-1]], dtype=cp.int64))

    def test_blink_1(self):
        b = blink(cp.array([[125], [17], [17]], dtype=cp.int64))
        print(b)
        assert cp.all(b == cp.array([[253000], [1], [7], [1], [7]], dtype=cp.int64))

    def test_blink_2(self):
        b = blink(cp.array([[253000], [1], [7]], dtype=cp.int64))
        assert cp.all(b == cp.array([[253], [0], [2024], [14168]], dtype=cp.int64))


if __name__ == "__main__":
    unittest.main()
