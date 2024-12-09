from copy import copy

top = None
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
used_numbers = []
highest_file = max([num for num in disk_part2 if num != '.']) # should be a cheaper way for this

while disk_part2[len(disk_part2) - 1] == '.':
    disk_part2.pop()
for value in list(set([num for num in disk_part2 if num != '.']))[::-1]:
    block_required = disk_part2.count(value)
    start_empty_block = None
    space = None
    for x, is_this_a_dot in enumerate(disk_part2[:disk_part2.index(value)]):
        if is_this_a_dot == '.':
            start_empty_block = x
            space = None
            for y, is_this_also_a_dot in enumerate(disk_part2[start_empty_block:]):
                if is_this_also_a_dot != '.':
                    space = y
                    break
            if space >= block_required:
                break
    if value % 100 == 0:
        print(f"Looking for {value}, block_required {block_required}, found {space} at {start_empty_block}")
    if space is not None and space >= block_required:
        # print("Found space!", space, block_required, value, start_empty_block)
        while value in disk_part2:
            disk_part2[disk_part2.index(value)] = '.'
        for x in range(block_required):
            disk_part2[start_empty_block + x] = value
            # print(disk_part2, x)


checksum = 0
for i, v in enumerate(disk_part2):
    if v != '.':
        checksum += i * int(v)
print(disk_part2)
print(checksum)
print(used_numbers)