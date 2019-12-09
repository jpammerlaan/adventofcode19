from helper_functions.io import read_input_file
from intcode.program import Program

DAY = '05'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))

# part one
p = Program(program=base_intcode.copy())
p.run(1)
print(p.get_output())

# part two
p = Program(program=base_intcode.copy())
p.run(5)
print(p.get_output())
