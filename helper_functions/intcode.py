class Program:
    NUM_PARAMS = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]

    def __init__(self, program):
        self.program = program + [0 for _ in range(10000)]  # pad the intcode with an arbitrarily long list
        self.output = []
        self.alive = True
        self.relative_base = 0
        self.idx = 0

    @staticmethod
    def _get_op_modes(op_str):
        op_str = op_str.zfill(5)  # pad opcode to length 5 so we can always use it the same way
        modes = list(map(int, op_str[0:3]))  # get modes as ints
        return int(op_str[3:]), modes[::-1]  # reverse the modes list

    def is_alive(self):
        return self.alive

    def get_output(self):
        return self.output

    def __get_param(self, p, mode):
        if mode == 2:
            return self.relative_base + self[p]
        elif mode == 0:
            return self[p]
        else:
            return p

    def __getitem__(self, index):
        return self.program[index]

    def __setitem__(self, index, val):
        self.program[index] = val

    def run_until_dead(self, input_val=None):
        while self.is_alive():
            self.run(input_val)

    def run(self, input_fn=input):
        while self[self.idx] != 99:
            try:
                op, modes = self._get_op_modes(str(self[self.idx]))
                params = [self.__get_param(self.idx + j + 1, modes[j]) for j in range(self.NUM_PARAMS[op])]
                if op == 1:
                    self[params[2]] = self[params[0]] + self[params[1]]
                elif op == 2:
                    self[params[2]] = self[params[0]] * self[params[1]]
                elif op == 3:
                    self[params[0]] = input_fn()
                elif op == 4:
                    self.output.append(self[params[0]])
                    self.idx += self.NUM_PARAMS[op] + 1
                    return self.output[-1]
                elif op == 5:
                    if self[params[0]] != 0:
                        self.idx = self[params[1]] - 3
                elif op == 6:
                    if self[params[0]] == 0:
                        self.idx = self[params[1]] - 3
                elif op == 7:
                    self[params[2]] = int(self[params[0]] < self[params[1]])
                elif op == 8:
                    self[params[2]] = int(self[params[0]] == self[params[1]])
                elif op == 9:
                    self.relative_base += self[params[0]]
                else:
                    raise ValueError('Invalid operator code {}'.format(op))
                self.idx += self.NUM_PARAMS[op] + 1
            except Exception as e:
                print(f'params: {params}')
                print(f'input_fn: {input_fn}')
                raise e
        self.alive = False
