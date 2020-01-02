from helper_functions.io import read_input_file
from collections import deque
from collections import defaultdict

DAY = '20'
# maze = read_input_file(DAY, output_type='list')
maze = """         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       """.split('\n')


def get_distances(grid, start):
    x_max, y_max = len(maze[0]), len(maze)
    bfs = deque([start])
    dist = {start: 0}
    portals = {}
    while bfs:
        x, y = bfs.popleft()
        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]
        for p in neighbors:
            xp, yp = p
            if not (1 <= xp <= x_max - 1 and 1 <= yp <= y_max - 1):  # stay within bounds
                continue
            if grid[yp][xp] in ['#', ' ']:  # stop when wall is found
                continue
            if grid[yp][xp] == '.' and p in dist:
                continue
            dist[p] = dist[(x, y)] + 1
            if 'A' <= grid[yp][xp] <= 'Z':
                # Found a portal, note the distance
                portal = grid[yp][xp]
                wrong_one = True
                for xn, yn in [(xp + 1, yp), (xp - 1, yp), (xp, yp + 1), (xp, yp - 1)]:
                    if 'A' <= grid[yn][xn] <= 'Z':
                        portal += grid[yn][xn]
                    if grid[yn][xn] == '.':
                        wrong_one = False
                if wrong_one:
                    continue
                portals[portal] = dist[p] - 1, p
                continue
            bfs.append(p)
    return portals


def get_portal_positions(grid, portal):
    if portal == 'AA':
        return [(9, 2)]
    elif portal == 'ZZ':
        return [(13, 16)]


portal_distances = defaultdict(dict)
aa_pos = get_portal_positions(maze, 'AA').pop()
zz_pos = get_portal_positions(maze, 'ZZ').pop()
portal_distances[aa_pos] = get_distances(maze, aa_pos)
for p in portal_distances[aa_pos].values():
    portal_distances[p] = get_distances(maze, p[1])
