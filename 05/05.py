from helper_functions.io import read_input_file

DAY = '05'
input_string = read_input_file(DAY)
# input_string = "1002,4,3,4,33"
base_intcode = list(map(int, input_string.split(',')))


def get_arg(intcode, i, mode):
    print('mode {}, index {}, value {}'.format(mode, i, intcode[i] if mode == 0 else i))
    if mode == 0:
        return intcode[i]
    else:
        return i


def get_op_modes(op_str):
    op_str = op_str.zfill(4)  # pad opcode to length 5
    modes = list(map(int, op_str[0:2]))  # get modes as integers
    return int(op_str[2:]), modes[::-1]  # reverse the modes list


def run_program2(base_intcode, input_val):
    intcode = base_intcode.copy()
    i = 0
    while True:
        # print('Iterating... i={}'.format(i))
        # print("Intcode: {}".format(intcode[i:]))
        # print("Relevant bit: {}".format(intcode[i:i + 4]))
        op, modes = get_op_modes(str(intcode[i]))
        # print(op, modes)
        if op <= 2:
            args = intcode[i + 1:i + 3]
            for j, mode in enumerate(modes):
                args[j] = intcode[args[j]] if mode == 0 else args[j]
            # print("Args: {}".format(args))
            if op == 1:
                intcode[i + 3] = args[0] + args[1]
            if op == 2:
                intcode[i + 3] = args[0] * args[1]
            i += 4
        elif op == 3:
            intcode[intcode[i + 1]] = input_val
            i += 2
        elif op == 4:
            print(intcode[i + 1])
            i += 2
        else:
            assert op == 99
            break


run_program2(base_intcode=base_intcode, input_val=1)
