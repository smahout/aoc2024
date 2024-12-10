def get_neighbours(map, y, x, increase=1):
    value = map[y][x]
    result = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for d in directions:
        new_y, new_x = y + d[0], x + d[1]
        if new_y in map and new_x in map[new_y] and map[new_y][new_x] == value + increase:
            result.append((new_y, new_x))
    return result

# Part 1
def get_peaks_for_trailhead(map, y, x):
    if map[y][x] == 9:
        return [(y, x)]
    neighbours = get_neighbours(map, y, x)
    if len(neighbours) == 0:
        return []
    results = []
    for neighbouring_y, neighbouring_x in neighbours:
        [results.append(entry) for entry in get_peaks_for_trailhead(map, neighbouring_y, neighbouring_x)]
    return results

# Part 2
def get_all_different_trails(map, y, x):
    if map[y][x] == 9:
        return 1
    neighbours = get_neighbours(map, y, x)
    if len(neighbours) == 0:
        return 0
    return sum([get_all_different_trails(map, neighbouring_y, neighbouring_x) for neighbouring_y, neighbouring_x in neighbours])

topographic_map = {y: {x: int(height) for x, height in enumerate(list(line.strip()))} for y, line in enumerate(open("big.txt").readlines())}
trailheads = [(y, x) for y in topographic_map.keys() for x in topographic_map[y].keys() if topographic_map[y][x] == 0]

print(sum([len(set(get_peaks_for_trailhead(topographic_map, y, x))) for y, x in trailheads])) # Part 1
print(sum([get_all_different_trails(topographic_map, y, x) for y, x in trailheads])) # Part 2
