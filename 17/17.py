from helper_functions.io import read_input_file
from helper_functions.intcode import Program
from queue import Queue
from collections import defaultdict
from copy import deepcopy
from time import sleep

DAY = '17'
input_string = read_input_file(DAY)
program = list(map(int, input_string.split(',')))

# part one
camera = Program(program=program)
camera.run_until_dead()
chars = [chr(i) for i in camera.get_output()]
chunked = ''.join(chars).split('\n')[:-2]
grid = defaultdict(str)
for y in range(len(chunked)):
    for x in range(len(chunked[y])):
        grid[(x, y)] = chunked[y][x]

total = 0
for (x, y) in list(grid.keys()):
    if (grid[(x, y)] == '#'
            and grid[(x - 1, y)] == '#'
            and grid[(x + 1, y)] == '#'
            and grid[(x, y - 1)] == '#'
            and grid[(x, y + 1)] == '#'):
        total += y * x
print(total)

# part two
inputs = {
    'main': "C,C,A,B,A,B,A,B,A,C\n",
    'A': "R,6,R,10,R,12,R,6\n",
    'B': "R,10,L,12,L,12\n",
    'C': "R,10,L,12,R,6\n",
    'video': 'n\n'
}
ascii_inputs = [ord(c) for s in inputs.values() for c in s]
robot = Program(program=program)
robot.program[0] = 2  # wake up the robot
robot.run_until_dead(input_fn=lambda: ascii_inputs.pop(0))
print(robot.get_output()[-1])

# Everything below this line is my initial attempt at solving the problem by code.
# This would probably have taken me a few more hours if I would have succeeded at all.
# Solving the problem by hand was about a million times easier, so I just settled for that!


class Robot(Program):
    TURNS = [None, '82', '76']  # go straight, then right, then left
    DIRECTIONS = {
        '^': (0, 1),
        '>': (1, 0),
        'v': (0, -1),
        '<': (-1, 0)
    }

    def __init__(self, program, grid, position):
        super().__init__(program)
        self.visited = defaultdict(list)
        self.grid = grid
        self.position = position
        self.orientation = '^'
        self.path = []
        self.visited = []
        self.to_visit = []

    def get_possible_directions(self):
        x, y = self.position
        return [k for k, v in self.DIRECTIONS.items() if self.grid[(x + v[0], y + v[1])] == '#']

    def turn(self, d):
        turns = defaultdict(str, {
            ('^', '<'): 'L',
            ('^', '>'): 'R',
            ('v', '>'): 'L',
            ('v', '<'): 'R',
            ('<', 'v'): 'L',
            ('<', '^'): 'R',
            ('>', '^'): 'L',
            ('>', 'v'): 'R',
        })
        turn_direction = turns[(self.orientation, d)]
        self.orientation = d
        self.path.append(turn_direction)
        return turn_direction

    def move_forward(self):
        # Determine number of steps to walk
        x, y = self.position
        dx, dy = self.DIRECTIONS[self.orientation]
        steps = 0
        while self.grid[(x + steps * dx, y + steps * dy)] == '#':
            steps += 1
        steps -= 1
        # Walk forward
        self.position = (x + steps * dx, y + steps * dy)
        self.path.append(steps)
        return steps


# part two
robot_pos = (int(chars.index('^') % (chars.index('\n') + 1)), int(chars.index('^') / (chars.index('\n') + 1)))
grid[robot_pos] = '#'  # replace the robot with a pound
init_robot = Robot(program=program, grid=grid, position=robot_pos)
init_robot.program[0] = 2  # wake up the robot
queue = Queue()
queue.put(init_robot)
i = 0
while not queue.empty():
    # take robot out of queue
    robot = queue.get()
    # move to next crossroads / corner
    robot.move_forward()
    # for each possible choice, add a copy of that program to the queue
    directions = robot.get_possible_directions()
    for d in directions:
        new_bot = deepcopy(robot)
        new_bot.turn(d)
        new_bot.choices.append((new_bot.position, d))
        queue.put(new_bot)
    print(robot.path, robot.orientation, directions)
    if i > 2:
        break
    i += 1
