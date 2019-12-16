from helper_functions.io import read_input_file
from helper_functions.intcode import Program

DAY = '09'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))

# part one
boost = Program(program=base_intcode.copy())
print(boost.run(input_fn=lambda: 1))

# part two
boost_two = Program(program=base_intcode.copy())
print(boost_two.run(input_fn=lambda: 2))
