from helper_functions.io import read_input_file

DAY = '05'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))


def get_op_modes(op_str):
    op_str = op_str.zfill(5)  # pad opcode to length 5 so we can always use it the same way
    modes = list(map(int, op_str[0:3]))  # get modes as ints
    return int(op_str[3:]), modes[::-1]  # reverse the modes list


def run_program(intcode, input_val):
    i = 0
    num_params = [0, 3, 3, 1, 1, 2, 2, 3, 3]

    while intcode[i] != 99:
        op, modes = get_op_modes(str(intcode[i]))
        # Refactored my get_args() function after seeing the list comprehension from /u/lele3000:
        args = [intcode[i + j + 1] if modes[j] else intcode[intcode[i + j + 1]] for j in range(num_params[op])]
        if op == 1:
            intcode[intcode[i + 3]] = args[0] + args[1]
        elif op == 2:
            intcode[intcode[i + 3]] = args[0] * args[1]
        elif op == 3:
            intcode[intcode[i + 1]] = input_val
        elif op == 4:
            intcode[0] = intcode[intcode[i + 1]]  # use intcode[0] as output value since it's never (re)used
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
    return intcode[0]


# part one
print(run_program(intcode=base_intcode.copy(), input_val=1))
# part two
print(run_program(intcode=base_intcode.copy(), input_val=5))
