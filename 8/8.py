def is_in_map(y, x, map):
    return 0 <= y < len(map) and 0 <= x < len(map[0])

with open("big.txt") as f:
    grid = [list(l.strip()) for l in f.readlines()]

antennas = [(y, x,col) for y, row in enumerate(grid) for x, col in enumerate(row) if col != '.']

for a1 in antennas:
    y1, x1, c1 = a1
    for a2 in antennas:
        if a1 is a2:
            continue
        y2, x2, c2 = a2
        if c1 == c2:
            grid[y2][x2] = "#"  # In part 2 every antenna that is in line with another antenna is also a node
            grid[y1][x1] = "#"  # In part 2 every antenna that is in line with another antenna is also a node
            y_diff, x_diff = y2-y1, x2-x1
            anti_y2, anti_x2 = y2+y_diff, x2+x_diff
            anti_y1, anti_x1 = y1+y_diff*-1, x1+x_diff*-1
            while is_in_map(anti_y1, anti_x1, grid): # While loop for part 2, only once for part 1
                grid[anti_y1][anti_x1] = "#"
                anti_y1, anti_x1 = anti_y1 + y_diff * -1, anti_x1 + x_diff * -1
            while is_in_map(anti_y2, anti_x2, grid): # While loop for part 2, only once for part 1
                grid[anti_y2][anti_x2] = "#"
                anti_y2, anti_x2 = anti_y2 + y_diff, anti_x2 + x_diff

[print(''.join(l)) for l in grid]
print(sum([1 for l in grid for c in l if c == '#']))