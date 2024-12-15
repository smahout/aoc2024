import numpy as np


def print_area(area):
    print("_____________")
    for y in area:
        print(''.join(y))
    print("_____________")


def move_horizontally(line):
    line = line[:np.where(line == '#')[0][0]]
    if '.' not in line:
        return line
    first_dot = np.where(line == '.')[0][0]
    line = np.delete(line, first_dot)
    line = np.insert(line, 0, '.')
    return line


def move_vertically(area, position, direction):
    next_row = position[0] + 1 if direction == 'v' else position[0] - 1
    next_block = area[next_row][position[1]]
    match next_block:
        case '[':  # Get column + 1 to the right
            move_vertically_with_boxes(area, position[0], position[1], 'R', direction)
        case ']':  # Get column + 1 to the left
            move_vertically_with_boxes(area, position[0], position[1], 'L', direction)
        case '.':
            area[next_row][position[1]] = '@'
            area[position[0]][position[1]] = '.'
        case '#':
            pass


def move_vertically_with_boxes(area, row, column, left_right, direction):
    left, right = (column - 1, column) if left_right == 'L' else (column, column + 1)
    can_move_boxes, boxes = can_move_vertically(area, left, right, row, direction)
    if can_move_boxes:
        new_row = -1 if direction == '^' else 1
        for box in boxes:
            area[box[0]][box[1]] = '.'
            area[box[0]][box[2]] = '.'
        for box in boxes:
            area[box[0] + new_row][box[1]] = '['
            area[box[0] + new_row][box[2]] = ']'
        area[row + new_row][column] = '@'
        area[row][column] = '.'


def can_move_vertically(area, left, right, row, direction):
    next_row = row - 1 if direction == '^' else row + 1
    if area[row][left] == '[':
        results = [(row, left, right)]
    else:
        results = []
    can_move = True
    if area[next_row][left] == ']':  # Box to our left
        new_results = can_move_vertically(area, left - 1, left, next_row, direction)
        results += new_results[1]
        can_move = can_move and new_results[0]
    if area[next_row][right] == '[':  # Box to our right
        new_results = can_move_vertically(area, right, right + 1, next_row, direction)
        results += new_results[1]
        can_move = can_move and new_results[0]
    if area[next_row][right] == ']':  # Box right on top / below
        new_results = can_move_vertically(area, left, right, next_row, direction)
        results += new_results[1]
        can_move = can_move and new_results[0]
    if area[next_row][left] == '#' or area[next_row][right] == '#':
        return False, set(results)
    return can_move, set(results)


def move(area, direction):
    position = np.where(area == '@')
    position = int(position[0][0]), int(position[1][0])
    match direction:
        case '<':  # Get row, moving left (x-)
            row = area[position[0]][:position[1] + 1][::-1]
            row = move_horizontally(row)[::-1]
            area[position[0]][position[1] + 1 - len(row):position[1] + 1] = row
        case '>':  # Get row, moving right (x+)
            row = area[position[0]][position[1]:]
            row = move_horizontally(row)
            area[position[0]][position[1]:position[1] + len(row)] = row
        case '^':  # Get col, moving up (y-)
            move_vertically(area, position, '^')
        case 'v':  # Get col, moving down (y+)
            move_vertically(area, position, 'v')


with open('big.txt') as txt:
    txt = txt.read().split("\n\n")
    area = np.array([list(row
                          .replace('#', '##')
                          .replace('O', '[]')
                          .replace('.', '..')
                          .replace('@', '@.')) for row in txt[0].split("\n")])

    directions = list(txt[1].replace("\n", ""))
    for d in directions:
        move(area, d)
    block_locations = np.where(area == '[')
    total = 0
    for i in range(len(block_locations[0])):
        total += 100 * block_locations[0][i] + block_locations[1][i]
    print(total)
