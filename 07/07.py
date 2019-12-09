from helper_functions.io import read_input_file
from itertools import permutations

DAY = '07'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))


def get_op_modes(op_str):
    op_str = op_str.zfill(5)  # pad opcode to length 5 so we can always use it the same way
    modes = list(map(int, op_str[0:3]))  # get modes as ints
    return int(op_str[3:]), modes[::-1]  # reverse the modes list


class Program:
    NUM_PARAMS = [0, 3, 3, 1, 1, 2, 2, 3, 3]

    def __init__(self, intcode, phase, return_output):
        self.intcode = intcode
        self.phase = phase
        self.used_phase = False
        self.active = True
        self.input = None
        self.output = None
        self.pause_on_output = return_output
        self.idx = 0

    @staticmethod
    def _get_op_modes(op_str):
        op_str = op_str.zfill(5)  # pad opcode to length 5 so we can always use it the same way
        modes = list(map(int, op_str[0:3]))  # get modes as ints
        return int(op_str[3:]), modes[::-1]  # reverse the modes list

    def set_input(self, input):
        self.input = input

    def get_output(self):
        return self.output

    def get_active_status(self):
        return self.active

    def run(self):
        while self.intcode[self.idx] != 99:
            op, modes = self._get_op_modes(str(self.intcode[self.idx]))
            # Refactored my get_args() function after seeing the list comprehension from /u/lele3000:
            args = [self.intcode[self.idx + j + 1] if modes[j] else self.intcode[self.intcode[self.idx + j + 1]] for j
                    in range(self.NUM_PARAMS[op])]
            if op == 1:
                self.intcode[self.intcode[self.idx + 3]] = args[0] + args[1]
            elif op == 2:
                self.intcode[self.intcode[self.idx + 3]] = args[0] * args[1]
            elif op == 3:
                self.intcode[self.intcode[self.idx + 1]] = self.input if self.used_phase else self.phase
                self.used_phase = True
            elif op == 4:
                self.output = self.intcode[self.intcode[self.idx + 1]]
                if self.pause_on_output:
                    self.idx += self.NUM_PARAMS[op] + 1
                    return
            elif op == 5:
                # offset the increment at the end of this loop by subtracting 3
                self.idx = args[1] - 3 if args[0] != 0 else self.idx
            elif op == 6:
                # offset the increment at the end of this loop by subtracting 3
                self.idx = args[1] - 3 if args[0] == 0 else self.idx
            elif op == 7:
                self.intcode[self.intcode[self.idx + 3]] = 1 if args[0] < args[1] else 0
            elif op == 8:
                self.intcode[self.intcode[self.idx + 3]] = 1 if args[0] == args[1] else 0
            else:
                raise ValueError('Invalid operator code {}'.format(op))
            self.idx += self.NUM_PARAMS[op] + 1
        self.active = False
        return


def test_program_configuration(programs):
    active = True
    output = 0
    while active:
        for i, program in enumerate(programs):
            program.run()
            active = program.get_active_status()
            output = program.get_output()
            programs[(i + 1) % 5].set_input(output)
    return output


def find_highest(base_intcode, phase_range, loop):
    phase_perms = permutations(phase_range)
    highest = 0
    for phases in phase_perms:
        programs = [Program(intcode=base_intcode.copy(), phase=phase, return_output=loop) for phase in phases]
        programs[0].set_input(0)  # set initial input value
        current = test_program_configuration(programs)
        highest = max(current, highest)
    return highest


# part one
print(find_highest(base_intcode=base_intcode, phase_range=range(0, 5), loop=False))
# part two
print(find_highest(base_intcode=base_intcode, phase_range=range(5, 10), loop=True))
