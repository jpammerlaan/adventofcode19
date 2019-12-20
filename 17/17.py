from helper_functions.io import read_input_file
from helper_functions.intcode import Program

DAY = '17'
input_string = read_input_file(DAY)
program = list(map(int, input_string.split(',')))

# part one
camera = Program(program=program)
camera.run_until_dead()
chars = [chr(i) for i in camera.get_output()]
n = chars.index('\n') + 1
grid = [chars[i:i + n - 1] for i in range(0, len(chars), n)][:-1]
total = 0
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[y]) - 1):
        if (grid[y][x] == '#'
                and grid[y][x - 1] == '#'
                and grid[y][x + 1] == '#'
                and grid[y - 1][x] == '#'
                and grid[y + 1][x] == '#'):
            total += y * x

# part two
robot = Program(program=program)
robot.program[0] = 2  # wake up the robot
