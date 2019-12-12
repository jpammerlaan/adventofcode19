from helper_functions.io import read_input_file
from helper_functions.intcode import Program

DAY = '11'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
directions = ['up', 'ri', 'do', 'le']

# part one
robot = Program(program=base_intcode.copy())
d = 0  # robot starts pointing up
# list of all turns we can make

# Let's start with a 100x100 grid of black squares
grid = [[0] * 100] * 100
x, y = 50, 50
visited = []
i = 0
while robot.is_alive():
    robot.run(grid[x][y])
    robot.run(None)  # run twice two get two outputs
    new_color, turn_right = robot.get_output()[-2:]
    grid[x][y] = new_color
    visited.append(tuple([x, y]))
    # print('Painting {} {}, turning {}.'.format(pos, 'black' if new_color == 0 else 'white',
    #                                            'right' if turn_right else 'left'))
    d = (d + 1) % 4 if turn_right else (d - 1) % 4
    x, y = x + dx[d], y + dy[d]
    i += 1

print(len(set(visited)))
# for x in range(len(grid)):
#     for y in range(len(grid[x])):
#         print('#' if grid[x][y] == 1 else ' ', end='')
#     print('')
