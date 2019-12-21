from helper_functions.io import read_input_file
from helper_functions.intcode import Program
from queue import Queue
from collections import defaultdict

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


class Robot(Program):
    def __init__(self, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = defaultdict(list)
        self.position = position
        self.path = []


# part two
TURNS = [None, '82', '76']  # go straight, then right, then left
robot_pos = (0, 0)  # TODO fix this
robot = Robot(program=program, position=robot_pos)
robot.program[0] = 2  # wake up the robot
queue = Queue()
queue.put(robot)
# init the robot by going right; it's currently facing up
# TODO init robot
while not queue.empty():
    # move to next crossroads
    # remember path
    # for each possible choice, add a copy of that program to the queue
    pass
