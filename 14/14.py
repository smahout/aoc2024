import math
import re
from PIL import Image
import numpy as np

class Guard:
    def __init__(self, x, y, vx, vy):
        self.x = int(x)
        self.y = int(y)
        self.vx = int(vx)
        self.vy = int(vy)
    def step(self, gx, gy):
        self.x += self.vx
        self.y += self.vy
        self.x = self.x if self.x < gx else self.x - gx
        self.y = self.y if self.y < gy else self.y - gy
        self.x = self.x if 0 <= self.x else self.x + gx
        self.y = self.y if 0 <= self.y else self.y + gy

    def __repr__(self):
        return f"g(x {self.x} y {self.y} vx {self.vx} vy {self.vy})"

guards = [Guard(g[0], g[1], g[2], g[3]) for g in [re.findall('-{0,1}\d+', line.strip()) for line in open("big.txt")]]
grid_x, grid_y = 101, 103
steps = 10000
p1_grid = [[0 for x in range(grid_x)] for y in range(grid_y)]

for i in range(steps):
    grid = [[0 for x in range(grid_x)] for y in range(grid_y)]
    for g in guards:
        g.step(grid_x, grid_y)
        grid[g.y][g.x] += 1

    if i == 100 - 1:
        p1_grid = grid
    image = Image.fromarray(np.array(grid).astype(np.uint8) * 255, mode='L')
    image.convert('1')
    image.save(f'images/{i}.png')

grid = p1_grid
q1 = sum([grid[y][x] for y in range(math.floor(grid_y / 2)) for x in range(math.floor(grid_x / 2))])
q2 = sum([grid[y][x] for y in range(math.floor(grid_y / 2) + 1, grid_y) for x in range(math.floor(grid_x / 2))])
q3 = sum([grid[y][x] for y in range(math.floor(grid_y / 2)) for x in range(math.floor(grid_x / 2) + 1, grid_x)])
q4 = sum([grid[y][x] for y in range(math.floor(grid_y / 2) + 1, grid_y) for x in range(math.floor(grid_x / 2) + 1, grid_x)])
print(q1 * q2 * q3 * q4)