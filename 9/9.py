from copy import copy

def add_to_dict_list(value, key, dict, sorting=False):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)
    if sorting:
        dict[key] = (sorted(dict[key]))

disk_part1 = [int(i / 2) if i % 2 == 0 else '.' for i, num in enumerate(list(open("big.txt").read())) for x in range(int(num))]
disk_part2 = copy(disk_part1)

# Part 1
checksum = 0

for spot, value in enumerate(disk_part1):
    if value == '.' :
        v = disk_part1.pop()
        while v == '.' and spot < len(disk_part1):
            v = disk_part1.pop()
        if v == '.':
            continue
        disk_part1[spot] = v
    checksum += spot * disk_part1[spot]
print(checksum)

# Part 2
highest_file = max([num for num in disk_part2 if num != '.'])
empty_blocks = {}
file_id_count = {}
first_occurrence = {}
start = 0
length = 0
for i, v in enumerate(disk_part2):
    if v not in file_id_count:
        file_id_count[v] = 1
        first_occurrence[v] = i
    else:
        file_id_count[v] += 1
    if v == '.':
        start = i if start is None else start
        length += 1
    elif start is not None:
        add_to_dict_list(start, length, empty_blocks)
        start = None
        length = 0

empty_blocks.pop(0)
while disk_part2[len(disk_part2) - 1] == '.':
    disk_part2.pop()

for value in list(set([num for num in disk_part2 if num != '.']))[::-1]:
    block_required = file_id_count[value]
    value_index = first_occurrence[value]
    available_blocks = [(empty_blocks[key][0], key) for key in empty_blocks if key >= block_required and len(empty_blocks[key]) > 0]
    if len(available_blocks) == 0:
        continue
    available_blocks = sorted(available_blocks, key=lambda block: block[0])
    empty_index, empty_block_length = available_blocks[0]
    if value_index <= empty_index:
        continue
    empty_blocks[empty_block_length].pop(0)
    add_to_dict_list(value_index, block_required, empty_blocks, True)

    while value in disk_part2:
        disk_part2[disk_part2.index(value)] = '.'
    for x in range(block_required):
        disk_part2[empty_index + x] = value
    if empty_block_length - block_required > 0:
        new_index = empty_index + block_required
        new_length = empty_block_length - block_required
        add_to_dict_list(new_index, new_length, empty_blocks, True)

checksum = 0
for i, v in enumerate(disk_part2):
    if v != '.':
        checksum += i * int(v)
print(checksum)