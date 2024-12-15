import numpy as np


def print_area(area):
    print("_____________")
    for y in area:
        print(''.join(y))
    print("_____________")


def make_move(line):
    line = line[:np.where(line == '#')[0][0]]
    if '.' not in line:
        return line
    first_dot = np.where(line == '.')[0][0]
    line = np.delete(line, first_dot)
    line = np.insert(line, 0, '.')
    return line


def move(area, direction):
    position = np.where(area == '@')
    position = int(position[0][0]), int(position[1][0])
    match direction:
        case '<':  # Get row, moving left (x-)
            row = area[position[0]][:position[1] + 1][::-1]
            row = make_move(row)[::-1]
            area[position[0]][position[1] + 1 - len(row):position[1] + 1] = row
        case '>':  # Get row, moving right (x+)
            row = area[position[0]][position[1]:]
            row = make_move(row)
            area[position[0]][position[1]:position[1] + len(row)] = row
        case '^':  # Get col, moving up (y-)
            col = area[:position[0] + 1, position[1]][::-1]
            col = make_move(col)[::-1]
            area[position[0] + 1 - len(col):position[0] + 1, position[1]] = col
        case 'v':  # Get col, moving down (y+)
            col = area[position[0]:, position[1]]
            col = make_move(col)
            area[position[0]:len(col) + position[0], position[1]] = col


with open('big.txt') as txt:
    txt = txt.read().split("\n\n")
    area = np.array([list(row) for row in txt[0].split("\n")])
    directions = list(txt[1].replace("\n", ""))
    for d in directions:
        move(area, d)
    block_locations = np.where(area == 'O')
    total = 0
    for i in range(len(block_locations[0])):
        total += 100 * block_locations[0][i] + block_locations[1][i]
    print(f"Part 1: {total}")
