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
        if cell == '@':  # mark the start position
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
            if 'a' <= grid[p] <= 'z' and grid[p] not in keys:
                keys[grid[p]] = dist[p], p
            bfs.append(p)
    return keys


def dijkstra(grid, pos, curr, unv, vis):
    nodes = get_reachable(grid, pos, vis)
    for key in nodes.keys():
        if key in vis:
            continue
        unv[key] = min(unv[key], unv[curr] + nodes[key])


def get_best_path(grid, pos, keys):
    best = ([], 10_000)
    paths_to_test = deque([([], pos, 0)])
    i = 1
    while paths_to_test:
        base_path, base_pos, base_dist = paths_to_test.popleft()
        r = get_reachable(grid, base_pos, base_path)
        # print(f'base path: {base_path}, curr pos: {base_pos}, curr steps: {base_dist}, reachable from here: {r}')
        for key in r.keys():
            # print(f'testing key {key}...')
            if key in base_path:
                continue
            key_dist, key_pos = r[key]
            path = base_path.copy()
            path.append(key)
            dist = base_dist + key_dist
            p = (path, key_pos, dist)
            # print(f'Adding {p} to paths to test.')
            paths_to_test.append(p)
        if len(to_get - set(base_path)) == 0:
            if base_dist < best[1]:
                best = (base_path, base_dist)

        if i % 100_000 == 0:
            print(f'tested {i} paths. {len(paths_to_test)} paths left to test.')
            return paths_to_test
        i += 1
    return best


to_get = {key: get_reachable() for pos, key in grid.items() if ('a' <= key <= 'z')}
# dijkstra(grid, pos, '@', to_get, [])
best = get_best_path(grid, pos, to_get)
print(best)

# paths = get_paths(grid, to_get, pos, [], set(), 0)
