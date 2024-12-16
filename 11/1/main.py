from tqdm import tqdm
import sys



def process_stone(stone):
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        return [stone[: len(stone) // 2], f"{int(stone[len(stone) // 2 :])}"]
    else:
        return [f"{int(stone) * 2024}"]


def blink(line):
    new_line = []
    for stone in tqdm(line):
        new_line.extend(process_stone(stone))

    return new_line


if __name__ == "__main__":
    if len(sys.argv) > 1:
        line = sys.argv[1].split(" ")

        for i in range(25):
            print(len(line))
            line = blink(line)

        print("STONES AFTER 25 BLINKS ==>", len(line))
    else:
        print("No input line provided")
