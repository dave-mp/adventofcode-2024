from tqdm import tqdm

EMPTY_FRAGMENT = "."


def translate_file_map(file_map):
    block_chain = []

    j = 0
    for i, x in tqdm(enumerate(file_map)):
        block_id = f"{j}" if not (i % 2) else EMPTY_FRAGMENT
        block = [block_id] * int(x)
        block_chain.extend(block)
        j += 1 if block_id != EMPTY_FRAGMENT else 0

    return block_chain


def find_first_empty_fragment(block_chain):
    return block_chain.index(EMPTY_FRAGMENT)


def find_last_file_fragment(block_chain):
    condition = lambda x: x != EMPTY_FRAGMENT
    return (
        len(block_chain)
        - 1
        - next(i for i, x in enumerate(reversed(block_chain)) if condition(x))
    )


def defragment_file(block_chain):
    count = 0

    first_empty_fragment = find_first_empty_fragment(block_chain)
    last_file_fragment = find_last_file_fragment(block_chain)

    while first_empty_fragment < last_file_fragment:
        new_block_chain = block_chain
        new_block_chain[first_empty_fragment] = block_chain[last_file_fragment]
        new_block_chain[last_file_fragment] = EMPTY_FRAGMENT

        block_chain = new_block_chain

        first_empty_fragment = find_first_empty_fragment(block_chain)
        last_file_fragment = find_last_file_fragment(block_chain)

        count += 1
        print(count, end="\r")

    return block_chain


def calculate_checksum(block_chain):
    checksum = 0
    for i, x in tqdm(enumerate(block_chain)):
        if x != EMPTY_FRAGMENT:
            checksum += int(x) * i
        else:
            break

    return checksum


with open("input.txt", "r") as f:
    file_map = [line.strip() for line in f.readlines()][0]

    # block_chain = translate_file_map(file_map)
    # print("BLOCK CHAIN ==>", len(block_chain))

    checksum = calculate_checksum(defragment_file(translate_file_map(file_map)))

    print("CHECKSUM ==>", checksum)
