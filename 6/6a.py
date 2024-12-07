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

def solve_map(map, position, direction):
    in_map = True
    while in_map:
        map[position[0]][position[1]] = 'X'
        in_map, position, direction = next_position(map, position, direction)

guard_map = [list(l.strip()) for l in open("big6.txt")]
position = [(i, row.index('^')) for i, row in enumerate(guard_map) if '^' in row][0]

solve_map(guard_map, (position[0]-1,position[1]), '^')

[print(''.join(r)) for r in guard_map]
print(sum([r.count('X') for r in guard_map]))