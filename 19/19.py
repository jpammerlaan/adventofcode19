from collections import defaultdict
from helper_functions.io import read_input_file
from helper_functions.io import print_binary_grid
from helper_functions.intcode import Program

DAY = '19'
input_string = read_input_file(DAY)
intcode = list(map(int, input_string.split(',')))


def active(x, y):
    tractor = Program(intcode)
    inp = [y, x]  # apparently I'm reversing x and y somewhere, so... there. I fixed it.
    tractor.run(input_fn=lambda: inp.pop())  # Oh. Here it is. Well, there you go!
    return tractor.get_output()[-1]


# part one
print(sum(active(x, y) for x in range(50) for y in range(50)))

x, y = 0, 0
while not active(x + 99, y):
    y += 1
    while not active(x, y + 99):
        x += 1
print(x * 10_000 + y)
