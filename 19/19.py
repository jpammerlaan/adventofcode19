from helper_functions.io import read_input_file
from helper_functions.intcode import Program

DAY = '19'
input_string = read_input_file(DAY)
intcode = list(map(int, input_string.split(',')))


def active(x, y):
    tractor = Program(intcode)
    inp = [x, y]
    tractor.run(input_fn=lambda: inp.pop())
    return tractor.get_output()[-1]


# part one
print(sum(active(x, y) for x in range(50) for y in range(50)))

x, y = 0, 0
while not active(x + 99, y):
    y += 1
    while not active(x, y + 99):
        x += 1
print(x * 10000 + y)
