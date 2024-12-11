def char_at(grid, coords):
    x, y = coords
    if y < 0 or y >= len(grid):
        return ''
    if x < 0 or x >= len(grid[y]):
        return ''
    return grid[y][x]


def check_direction(direction, grid, coords, word, current_char=0):
    new_coords = (coords[0] + direction[0], coords[1] + direction[1])
    current_char += 1
    if char_at(grid, new_coords) == word[current_char]:
        if current_char == len(word) - 1:
            return True
        else:
            return check_direction(direction, grid, new_coords, word, current_char)
    return False


directions = [
    (0, +1), (0, -1),
    (+1, +1), (+1, 0), (+1, -1),
    (-1, +1), (-1, 0), (-1, -1)
]
words = ['XMAS']
with open("big4.txt") as f:
    grid = [list(line.strip()) for line in f]

total1 = 0
total2 = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        # Part 1
        for word in words:
            if grid[y][x] == word[0]:
                for direction in directions:
                    total1 += 1 if check_direction(direction, grid, (x, y), word) else 0
        # Part 2
        if grid[y][x] == 'A':
            xmas1 = char_at(grid, (x - 1, y - 1)) + 'A' + char_at(grid, (x + 1, y + 1))
            xmas2 = char_at(grid, (x - 1, y + 1)) + 'A' + char_at(grid, (x + 1, y - 1))
            total2 += 1 if (xmas1 == 'MAS' or xmas1 == 'SAM') and (xmas2 == 'MAS' or xmas2 == 'SAM') else 0

print("Part 1: ", total1)
print("Part 2: ", total2)
