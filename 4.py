from numpy import flip, array, fliplr, array2string

words = ["XMAS"] # I thought there would be multiple words in part 2
grid = array([list(line.strip()) for line in open("inputs/big4.txt").readlines()])
lines = []
lr_grid = fliplr(grid)
[(lines.append(grid[:, i]), lines.append(flip(grid[:, i]))) for i in range(grid.shape[0])] # |
[(lines.append(grid[i, :]), lines.append(flip(grid[i, :]))) for i in range(grid.shape[1])] # -
[(lines.append(grid.diagonal(-i)), lines.append(flip(grid.diagonal(-i)))) for i in range(0-grid.shape[1], grid.shape[0])] # \
[(lines.append(lr_grid.diagonal(-i)), lines.append(flip(lr_grid.diagonal(-i)))) for i in range(0-grid.shape[1], grid.shape[0])] # /
strings = [''.join(line.tolist()) for line in lines]
print("Part 1: ", sum([sum([line.count(word) for line in strings]) for word in words]))

xmas = 0
for row in range(1, grid.shape[1] - 1):
    for col in range(1, grid.shape[0] - 1):
        if grid[row][col] == 'A':
            diagonal1 = (grid[row+1][col+1], grid[row-1][col-1])
            diagonal2 = (grid[row+1][col-1], grid[row-1][col+1])
            xmas += 1 if (diagonal1 == ('M','S') or diagonal1 == ('S', 'M')) and (diagonal2 == ('M', 'S') or diagonal2 == ('S', 'M')) else 0
print("Part 2: ", xmas)