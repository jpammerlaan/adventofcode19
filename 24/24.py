from helper_functions.io import read_input_file
import numpy as np
import timeit

DAY = '24'
input_list = read_input_file(DAY, output_type='list')
d = {'.': 0, '#': 1}
grid = np.array([[d[k] for k in row] for row in input_list])
rows, cols = grid.shape


def tick(g):
    g2 = g.copy()
    for r in range(rows):
        for c in range(cols):
            g2[r, c] = update_cell(g, c, r)
    return g2


def update_cell(g, x, y):
    n = {
        (max(x - 1, 0), y),
        (min(x + 1, cols - 1), y),
        (x, max(y - 1, 0)),
        (x, min(y + 1, rows - 1))
    }.difference({(x, y)})  # make sure we don't count the cell itself, only neighbors
    xn, yn = zip(*n)
    bugs = (g[yn, xn] == 1).sum()
    return int(bugs == 1 or (g[y, x] == 0 and bugs == 2))


def calc_biodiversity(g):
    return sum(pow(2, i) if cell == 1 else 0 for i, cell in enumerate(g.flatten()))


def part_one(grid):
    seen, bio = [], calc_biodiversity(grid)
    while bio not in seen:
        seen.append(bio)
        grid = tick(grid)
        bio = calc_biodiversity(grid)
    return bio


# part one
print(part_one(grid))
