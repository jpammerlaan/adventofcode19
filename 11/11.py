from helper_functions.io import read_input_file
from helper_functions.intcode import Program

DAY = '11'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
directions = ['up', 'ri', 'do', 'le']
colors = ['black', 'white']

# part one
robot = Program(program=base_intcode.copy())
d = 0  # robot starts pointing up

grid = [[0] * 100] * 100
x, y = 50, 50
visited = set()
while True:
    new_color = robot.run(grid[y][x])
    if new_color is None:
        break
    grid[y][x] = new_color
    visited.add((x, y))
    turn_right = robot.run()
    d = (d + 1) % 4 if turn_right else (d + 3) % 4
    print(new_color, turn_right)
    print('Painting {} {}, turning {}. Direction is now {}'.format((x, y), colors[new_color],
                                                                   'right' if turn_right else 'left', directions[d]))
    x += dx[d]
    y += dy[d]
    print(x, y)

print(len(set(visited)))
# for x in range(len(grid)):
#     for y in range(len(grid[x])):
#         print('#' if grid[x][y] == 1 else ' ', end='')
#     print('')
