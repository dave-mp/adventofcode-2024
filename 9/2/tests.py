import unittest
from main import (
    translate_file_map,
    find_empty_block,
    find_file_block,
    defragment_file,
    calculate_checksum,
)


class TestDefragmentFile(unittest.TestCase):
    def test_translate_file_map(self):
        tfm = translate_file_map("2333133121414131402")
        assert tfm == (
            [
                "0",
                "0",
                ".",
                ".",
                ".",
                "1",
                "1",
                "1",
                ".",
                ".",
                ".",
                "2",
                ".",
                ".",
                ".",
                "3",
                "3",
                "3",
                ".",
                "4",
                "4",
                ".",
                "5",
                "5",
                "5",
                "5",
                ".",
                "6",
                "6",
                "6",
                "6",
                ".",
                "7",
                "7",
                "7",
                ".",
                "8",
                "8",
                "8",
                "8",
                "9",
                "9",
            ],
            9,
        )

    def test_find_first_empty_fragment(self):
        assert (
            find_empty_block(
                [
                    "0",
                    "0",
                    ".",
                    ".",
                    ".",
                    "1",
                    "1",
                    "1",
                    ".",
                    ".",
                    ".",
                    "2",
                    ".",
                    ".",
                    ".",
                    "3",
                    "3",
                    "3",
                    ".",
                    "4",
                    "4",
                    ".",
                    "5",
                    "5",
                    "5",
                    "5",
                    ".",
                    "6",
                    "6",
                    "6",
                    "6",
                    ".",
                    "7",
                    "7",
                    "7",
                    ".",
                    "8",
                    "8",
                    "8",
                    "8",
                    "9",
                    "9",
                ],
                3,
            )
            == 2
        )

    def test_find_file_block(self):
        assert find_file_block(
            [
                "0",
                "0",
                ".",
                ".",
                ".",
                "1",
                "1",
                "1",
                ".",
                ".",
                ".",
                "2",
                ".",
                ".",
                ".",
                "3",
                "3",
                "3",
                ".",
                "4",
                "4",
                ".",
                "5",
                "5",
                "5",
                "5",
                ".",
                "6",
                "6",
                "6",
                "6",
                ".",
                "7",
                "7",
                "7",
                ".",
                "8",
                "8",
                "8",
                "8",
                "9",
                "9",
            ],
            "9",
        ) == (40, 2)

    def test_defragment_file(self):
        df = defragment_file(
            [
                "0",
                "0",
                ".",
                ".",
                ".",
                "1",
                "1",
                "1",
                ".",
                ".",
                ".",
                "2",
                ".",
                ".",
                ".",
                "3",
                "3",
                "3",
                ".",
                "4",
                "4",
                ".",
                "5",
                "5",
                "5",
                "5",
                ".",
                "6",
                "6",
                "6",
                "6",
                ".",
                "7",
                "7",
                "7",
                ".",
                "8",
                "8",
                "8",
                "8",
                "9",
                "9",
            ],
            "9",
        )
        assert df == list("00992111777.44.333....5555.6666.....8888..")

    def test_calculate_checksum(self):
        assert calculate_checksum("00992111777.44.333....5555.6666.....8888..") == 2858


if __name__ == "__main__":
    unittest.main()