class Flowerbed:
    def __init__(self, flower, y, x, grid):
        self.flower = flower
        self.start_y = y
        self.start_x = x
        self.area = 0
        self.perimeter = 0
        self.north_edges = {str(i): [] for i in range(-1, len(grid[0])+1)}
        self.south_edges = {str(i): [] for i in range(-1, len(grid[0])+1)}
        self.west_edges = {str(i): [] for i in range(-1, len(grid)+1)}
        self.east_edges = {str(i): [] for i in range(-1, len(grid)+1)}

    def sides(self):
        self.north_edges = {key: sorted(items) for key, items in self.north_edges.items()}
        self.south_edges = {key: sorted(items) for key, items in self.south_edges.items()}
        self.west_edges = {key: sorted(items) for key, items in self.west_edges.items()}
        self.east_edges = {key: sorted(items) for key, items in self.east_edges.items()}

        sides = 0
        sides += sum([1 if i == 0 or self.north_edges[y][i-1] + 1 != self.north_edges[y][i] else 0 for y in self.north_edges for i in range(len(self.north_edges[y]))])
        sides += sum([1 if i == 0 or self.south_edges[y][i-1] + 1 != self.south_edges[y][i] else 0 for y in self.south_edges for i in range(len(self.south_edges[y]))])
        sides += sum([1 if i == 0 or self.west_edges[x][i-1] + 1 != self.west_edges[x][i] else 0 for x in self.west_edges for i in range(len(self.west_edges[x]))])
        sides += sum([1 if i == 0 or self.east_edges[x][i-1] + 1 != self.east_edges[x][i] else 0 for x in self.east_edges for i in range(len(self.east_edges[x]))])
        return sides

    def __str__(self):
        northedges = sum(1 for y in self.north_edges for _ in self.north_edges[y])
        southedges = sum(1 for y in self.south_edges for _ in self.south_edges[y])
        westedges = sum(1 for x in self.west_edges for _ in self.west_edges[x])
        eastedges = sum(1 for x in self.east_edges for _ in self.east_edges[x])
        return f"Flowerbed(flower:{self.flower},y:{self.start_y},x:{self.start_x},area:{self.area},perimeter:{self.perimeter},north:{northedges},east:{eastedges},south:{southedges},west:{westedges},all:{northedges+eastedges+southedges+westedges}"

def is_in_map(y, x, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def find_neighbouring_flowers(grid, y, x):
    north, east, south, west = (0 + x, y - 1), (x + 1, 0 + y), (0 + x, 1 + y), (x - 1, 0 + y)
    north = (north[1], north[0]) if is_in_map(north[1], north[0], grid) else None
    east = (east[1], east[0]) if is_in_map(east[1], east[0], grid) else None
    south = (south[1], south[0]) if is_in_map(south[1], south[0], grid) else None
    west = (west[1], west[0]) if is_in_map(west[1], west[0], grid) else None
    return north, east, south, west  # returns (y, x)


def define_flowerbed(grid, x, y, visited, to_visit=None):
    if to_visit is None:
        to_visit = [(y, x)]

    flowerbed = Flowerbed(grid[y][x], y, x, grid)
    while len(to_visit) > 0:
        y, x = to_visit.pop()
        if (y, x) in visited:
            continue
        flowerbed.area += 1
        visited.append((y, x))
        north, east, south, west = find_neighbouring_flowers(grid, y, x)
        if north is not None:
            if grid[north[0]][north[1]] == flowerbed.flower and north not in visited:
                to_visit.append(north)
            elif grid[north[0]][north[1]] != flowerbed.flower:
                flowerbed.perimeter += 1
                flowerbed.north_edges[str(north[0])].append(north[1])
        else:
            flowerbed.perimeter += 1
            flowerbed.north_edges["-1"].append(x)
        if east is not None:
            if grid[east[0]][east[1]] == flowerbed.flower and east not in visited:
                to_visit.append(east)
            elif grid[east[0]][east[1]] != flowerbed.flower:
                flowerbed.perimeter += 1
                flowerbed.east_edges[str(east[1])].append(east[0])
        else:
            flowerbed.perimeter += 1
            flowerbed.east_edges[str(len(grid[0]))].append(y)
        if south is not None:
            if grid[south[0]][south[1]] == flowerbed.flower and south not in visited:
                to_visit.append(south)
            elif grid[south[0]][south[1]] != flowerbed.flower:
                flowerbed.perimeter += 1
                flowerbed.south_edges[str(south[0])].append(south[1])
        else:
            flowerbed.perimeter += 1
            flowerbed.south_edges[str(len(grid))].append(x)
        if west is not None:
            if grid[west[0]][west[1]] == flowerbed.flower and west not in visited:
                to_visit.append(west)
            elif grid[west[0]][west[1]] != flowerbed.flower:
                flowerbed.perimeter += 1
                flowerbed.west_edges[str(west[1])].append(west[0])
        else:
            flowerbed.perimeter += 1
            flowerbed.west_edges["-1"].append(y)
    return flowerbed


grid = [[char for char in list(line.strip())] for line in open("big.txt").readlines()]
visited = []
flowerbeds = []
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if (y, x) not in visited:
            flowerbeds.append(define_flowerbed(grid, x, y, visited))

counta = 0
countb = 0
for flowerbed in flowerbeds:
    print(flowerbed, flowerbed.area * flowerbed.sides(), flowerbed.sides())
    counta += flowerbed.area * flowerbed.perimeter
    countb += flowerbed.area * flowerbed.sides()

print(f"Part 1: {counta}")
print(f"Part 2: {countb}")
