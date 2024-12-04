from numpy import flip, array, fliplr

words = ["XMAS"]
grid = array([list(line.strip()) for line in open("input_big.txt").readlines()])
lines = []
lr_grid = fliplr(grid)
[(lines.append(grid[:, i]), lines.append(flip(grid[:, i]))) for i in range(grid.shape[0])] # |
[(lines.append(grid[i, :]), lines.append(flip(grid[i, :]))) for i in range(grid.shape[1])] # -
[(lines.append(grid.diagonal(-i)), lines.append(flip(grid.diagonal(-i)))) for i in range(0-grid.shape[1], grid.shape[0])] # \
[(lines.append(lr_grid.diagonal(-i)), lines.append(flip(lr_grid.diagonal(-i)))) for i in range(0-grid.shape[1], grid.shape[0])] # /
strings = [''.join(line.tolist()) for line in lines]
print(sum([sum([line.count(word) for line in strings]) for word in words]))

xmas = 0
for row in range(1, grid.shape[1] - 1):
    for col in range(1, grid.shape[0] - 1):
        if grid[row][col] == 'A':
            diag1 = (grid[row+1][col+1], grid[row-1][col-1])
            diag2 = (grid[row+1][col-1], grid[row-1][col+1])
            if (diag1 == ('M','S') or diag1 == ('S', 'M')) and (diag2 == ('M', 'S') or diag2 == ('S', 'M')):
                xmas += 1
print(xmas)