from helper_functions.io import read_input_file
from math import floor

DAY = '01'
modules = read_input_file(DAY, output_type='list')


def get_fuel(mod):
    return [max(floor(int(m) / 3) - 2, 0) for m in mod]


# part one
print(sum(get_fuel(modules)))

# part two
total = 0
while True:
    modules = get_fuel(modules)
    to_add = sum(modules)
    total += to_add
    if to_add == 0:
        break

print(total)
