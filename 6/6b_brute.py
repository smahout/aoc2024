from copy import deepcopy


def get_next_step(position, direction):
    match direction:
        case '^':
            return position[0] - 1, position[1]
        case '>':
            return position[0], position[1] + 1
        case 'v':
            return position[0] + 1, position[1]
        case '<':
            return position[0], position[1] - 1


def is_in_map(position, map):
    return 0 <= position[0] < len(map) and 0 <= position[1] < len(map[0])


def next_direction(direction):
    match direction:
        case '^':
            return '>'
        case '>':
            return 'v'
        case 'v':
            return '<'
        case '<':
            return '^'


def next_position(map, position, direction):
    next_position = get_next_step(position, direction)
    if in_map := is_in_map(next_position, map):
        while '#' in map[next_position[0]][next_position[1]]:
            direction = next_direction(direction)
            next_position = get_next_step(position, direction)
        position = next_position
    return in_map, position, direction


def gets_stuck(map, position, direction):
    in_map = True
    while in_map:
        if direction in map[position[0]][position[1]]:
            return True
        map[position[0]][position[1]].append(direction)
        in_map, position, direction = next_position(map, position, direction)
    return False


def solve_map(source_map, position, direction):
    guard_map = [[[col] for col in row] for row in deepcopy(source_map)]
    count = 0
    for y in range(len(guard_map)):
        for x in range(len(guard_map[y])):
            if '#' and '^' not in guard_map[y][x]:
                copy = deepcopy(guard_map)
                copy[y][x].append('#')
                if gets_stuck(copy, (position[0] - 1, position[1]), direction):
                    count += 1
                    guard_map[y][x].append('O')
    print(count)
    for row in guard_map:
        for i, col in enumerate(row):
            row[i] = ''.join(col)
        print('\t'.join(row))


guard_map = [list(l.strip()) for l in open("small6.txt")]
position = [(i, row.index('^')) for i, row in enumerate(guard_map) if '^' in row][0]
direction = '^'

solve_map(guard_map, position, direction)
