from helper_functions.io import read_input_file
from helper_functions.intcode import Program

DAY = '21'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))


class SpringDroid(Program):
    WALK_INPUT = lambda: 

    def __init__(self, program):
        super().__init__(program)
        self.T = False
        self.J = False
        self.A = None
        self.B = None
        self.C = None
        self.D = None

    def walk(self):
        self.run(input_fn=self.WALK_INPUT)