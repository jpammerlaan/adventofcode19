from helper_functions.io import read_input_file, print_binary_grid
from helper_functions.intcode import Program

DAY = '11'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))


def paint(start_value, X, Y):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    robot = Program(program=base_intcode.copy())
    d = 0  # robot starts pointing up
    grid = [[0 for _ in range(X)] for _ in range(Y)]
    x, y = int(X/2), int(Y/2)
    grid[y][x] = start_value
    visited = set()
    while True:
        new_color = robot.run(grid[y][x])
        if not robot.is_alive():
            break
        grid[y][x] = new_color
        visited.add((x, y))
        turn_right = robot.run()
        d = (d + 1) % 4 if turn_right else (d + 3) % 4
        x += dx[d]
        y += dy[d]

    return visited, grid


# part one
panels, _ = paint(start_value=0, X=200, Y=200)
print(len(panels))

# part two
_, grid = paint(start_value=1, X=120, Y=15)
print_binary_grid(grid)
