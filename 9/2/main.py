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

    return block_chain, j - 1


def find_empty_block(block_chain, length):
    arr1 = [EMPTY_FRAGMENT] * length
    arr2 = block_chain
    for i in range(len(arr2) - len(arr1) + 1):
        if arr1 == arr2[i : i + len(arr1)]:
            return i
    return -1


def find_file_block(block_chain, id):
    index = block_chain.index(id)
    count = 0
    for x in block_chain[index:]:
        if x == id:
            count += 1
        else:
            break

    return (index, count)


def defragment_file(block_chain, max_id):
    id = int(max_id)
    new_block_chain = block_chain

    while id > 0:
        print(id, end="\r")
        (index, count) = find_file_block(new_block_chain, f"{id}")
        empty_block_index = find_empty_block(new_block_chain, count)

        if index > empty_block_index > -1:
            for i in range(count):
                new_block_chain[empty_block_index + i] = f"{id}"
                new_block_chain[index + i] = EMPTY_FRAGMENT

        id -= 1

    return new_block_chain


def calculate_checksum(block_chain):
    checksum = 0
    for i, x in tqdm(enumerate(block_chain)):
        if x != EMPTY_FRAGMENT:
            checksum += int(x) * i

    return checksum


with open("input.txt", "r") as f:
    file_map = [line.strip() for line in f.readlines()][0]

    (translated_file, max_id) = translate_file_map(file_map)
    defragmented_file = defragment_file(translated_file, max_id)
    checksum = calculate_checksum(defragmented_file)

    print("CHECKSUM ==>", checksum)
