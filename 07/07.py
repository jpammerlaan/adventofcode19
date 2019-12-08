from helper_functions.io import read_input_file
from itertools import permutations

DAY = '07'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))


def get_op_modes(op_str):
    op_str = op_str.zfill(5)  # pad opcode to length 5 so we can always use it the same way
    modes = list(map(int, op_str[0:3]))  # get modes as ints
    return int(op_str[3:]), modes[::-1]  # reverse the modes list


def run_program(intcode, phase, input_val):
    i = 0
    num_params = [0, 3, 3, 1, 1, 2, 2, 3, 3]
    return_val = 0
    used_phase = False

    while intcode[i] != 99:
        op, modes = get_op_modes(str(intcode[i]))
        # Refactored my get_args() function after seeing the list comprehension from /u/lele3000:
        args = [intcode[i + j + 1] if modes[j] else intcode[intcode[i + j + 1]] for j in range(num_params[op])]
        if op == 1:
            intcode[intcode[i + 3]] = args[0] + args[1]
        elif op == 2:
            intcode[intcode[i + 3]] = args[0] * args[1]
        elif op == 3:
            intcode[intcode[i + 1]] = input_val if used_phase else phase
            used_phase = True
        elif op == 4:
            return_val = intcode[intcode[i + 1]]
        elif op == 5:
            i = args[1] - 3 if args[0] != 0 else i  # offset the increment at the end of this loop by subtracting 3
        elif op == 6:
            i = args[1] - 3 if args[0] == 0 else i  # offset the increment at the end of this loop by subtracting 3
        elif op == 7:
            intcode[intcode[i + 3]] = 1 if args[0] < args[1] else 0
        elif op == 8:
            intcode[intcode[i + 3]] = 1 if args[0] == args[1] else 0
        else:
            raise ValueError('Invalid operator code {}'.format(op))
        i += num_params[op] + 1
    return return_val


def find_highest(base_intcode, phase_range):
    phase_perms = permutations(phase_range)
    highest = 0
    for phases in phase_perms:
        input_val = 0
        for phase in phases:
            input_val = run_program(base_intcode.copy(), phase, input_val)
        highest = input_val if input_val > highest else highest
    return highest


# part one
print(find_highest(base_intcode=base_intcode, phase_range=range(0, 5)))
# part two
# print(find_highest(phase_range=range(5, 10)))
