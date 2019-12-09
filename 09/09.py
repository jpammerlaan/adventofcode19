from helper_functions.io import read_input_file
from intcode.program import Program

DAY = '09'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))

# part one
boost = Program(program=base_intcode.copy())
boost.run(1)
print(boost.get_output())

# part two
boost_two = Program(program=base_intcode.copy())
boost_two.run(2)
print(boost_two.get_output())
