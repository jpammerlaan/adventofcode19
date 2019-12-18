from helper_functions.io import read_input_file
from helper_functions.intcode import Program
from collections import defaultdict
from time import sleep

DAY = '15'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))


class Droid(Program):
    DX = (0, 1, 0, -1)
    DY = (-1, 0, 1, 0)
    DIRECTIONS = (1, 4, 2, 3)
    DIRECTIONS_STR = ('N', 'E', 'S', 'W')
    OUTPUT_MAP = {0: '#', 1: '.', 2: 'o', 3: 'x'}

    def __init__(self, program):
        super().__init__(program=program)
        self.d = 0
        self.x = 10
        self.y = 10
        self.path = []
        self.path_to_tank = []
        self.grid = defaultdict(lambda: ' ', {(self.x, self.y): 'x'})
        self.attempts = (3, 0, 1, 2)
        self.go_back = False

    def run(self, input_fn=None):
        i = 0
        while True:
            d = (self.d + self.attempts[i]) % 4
            out = super().run(input_fn=lambda: self.DIRECTIONS[d])  # run the Intcode program
            new_x = self.x + self.DX[d]
            new_y = self.y + self.DY[d]
            if self.grid[(new_x, new_y)] == ' ':
                self.grid[(new_x, new_y)] = self.OUTPUT_MAP[out]
            i += 1
            if out > 0:
                self.x, self.y = new_x, new_y
                self.d = d
                self.path.append(self.DIRECTIONS[d])
                if out == 2 and not self.go_back:  #  save the path to the oxygen tank and go back
                    self.path_to_tank = self.path.copy()
                    self.go_back = True
                if (self.x, self.y) == (10, 10) and self.go_back:
                    self.alive = False
                break

    def print_maze(self):
        coords = self.grid.keys()
        x_min, y_min = list(map(min, zip(*coords)))
        x_max, y_max = list(map(max, zip(*coords)))
        x_range = range(x_min - 1, x_max + 2)
        y_range = range(y_min - 1, y_max + 2)
        print('\n'.join([''.join([self.grid[(x, y)] for x in x_range]) for y in y_range]))


droid = Droid(program=base_intcode.copy())
# part one
droid.run_until_dead()
path_to_tank = ''.join([str(x) for x in droid.path_to_tank])
print(len(path_to_tank))
# reduce the droid path by filtering out excess paths (NS/SN/WE/EW parts)
for _ in range(len(path_to_tank)):
    path_to_tank = path_to_tank.replace('12', '').replace('21', '').replace('34', '').replace('43', '')
print(len(path_to_tank))

# part two
droid_path = droid.path
print(droid.path)