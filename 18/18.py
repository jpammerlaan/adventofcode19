from helper_functions.io import read_input_file
from collections import defaultdict, deque

DAY = '18'
input_maze = read_input_file(DAY, output_type='list')

# Create the grid of the maze
grid = defaultdict(str)
pos = None
for y, row in enumerate(input_maze):
    for x, cell in enumerate(list(row)):
        grid[(x, y)] = cell
        if cell == '@':
            grid[(x, y)] = '.'
            pos = (x, y)


def get_reachable(grid, s, have):
    x_max, y_max = max(p[0] for p in grid.keys()), max(p[1] for p in grid.keys())
    bfs = deque([s])
    dist = {s: 0}
    keys = {}
    while bfs:
        x, y = bfs.popleft()
        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]
        # print(neighbors)
        for p in neighbors:
            xn, yn = p
            if not (0 <= xn <= x_max and 0 <= yn <= y_max):
                continue
            if grid[p] == '#':
                continue
            if 'A' <= grid[p] <= 'Z' and grid[p].lower() not in have:
                continue
            if grid[p] == '.' and p in dist:
                continue
            dist[p] = dist[(x, y)] + 1
            # print(p, dist[p], grid[p])
            if 'a' <= grid[p] <= 'z' and grid[p] not in keys:
                keys[grid[p]] = dist[p], p
            bfs.append(p)
    return keys


def get_paths(grid, to_get, pos, path, have, steps):
    # TODO this works not
    reachable = get_reachable(grid, pos, have)
    print(f'have {path}, can reach {list(reachable.keys())}, took {steps} steps so far.')
    for key in reachable.keys():
        if key in path:
            continue
        s, new_pos = reachable[key]
        new_path = path.copy()
        new_path.append(key)
        path, have, steps = get_paths(grid, to_get, new_pos, new_path, set(new_path), steps + s)

    return path, have, steps


to_get = set([key for key in grid.values() if 'a' <= key <= 'z'])
paths = get_paths(grid, to_get, pos, [], set(), 0)
