import unittest
from main import blink, process_stone


class TestDefragmentFile(unittest.TestCase):
    def test_process_stone_1(self):
        assert process_stone("17") == ["1", "7"]

    def test_process_stone_2(self):
        assert process_stone("2024") == ["20", "24"]

    def test_process_stone_3(self):
        assert process_stone("125") == ["253000"]

    def test_blink_1(self):
        assert blink(["125", "17"]) == ["253000", "1", "7"]

    def test_blink_2(self):
        assert blink(["253000", "1", "7"]) == ["253", "0", "2024", "14168"]


if __name__ == "__main__":
    unittest.main()
